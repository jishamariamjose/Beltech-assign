from django.shortcuts import render

from django.http import HttpResponse
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from .serializers import EmployeeSerializer
from .models import EmployeeSchema
from rest_framework.decorators import api_view
import json
import datetime
from django.utils import timezone
from datetime import date, timedelta
from django.db.models import Q

@api_view(['GET'])
def employee_list(request):
    if request.method == 'GET':
        from_date = timezone.now() - datetime.timedelta(days=14)
        
        #Query to fetch record with employees joined before 14 days and not in department 'Beltech'
        employees = EmployeeSchema.objects.filter(Q(DateCreated__lt=from_date) & ~Q(Department='Beltech')).order_by('-Score')
        employees_serializer = EmployeeSerializer(employees, many=True)
        employees_list = json.loads(json.dumps(employees_serializer.data))
        
        #Query to fetch record with employees joined in last 14 days
        employees_latest = EmployeeSchema.objects.filter(Q(DateCreated__gte=from_date) & Q(DateCreated__lte=timezone.now()) & ~Q(Department='Beltech'))
        employees_latest_serializer = EmployeeSerializer(employees_latest, many=True)
        employees_latest_list = json.loads(json.dumps(employees_latest_serializer.data))
        
        #Query to fetch record with employees in department 'Beltech'
        employees_Beltech = EmployeeSchema.objects.filter(Department='Beltech')
        employees_Beltech_serializer = EmployeeSerializer(employees_Beltech, many=True)
        employees_Beltech_list = json.loads(json.dumps(employees_Beltech_serializer.data))
        
        #Create a list of two element array for insertion at position 5,6,7,8 
        res_Beltech=[]
        res_latest=[]
        for index in employees_Beltech_list:
            if employees_Beltech_list:
                insert_beltech=employees_Beltech_list[:2]
                res_Beltech.append(insert_beltech)
                employees_Beltech_list=employees_Beltech_list[2:]
        
        for index in employees_latest_list:
            if employees_latest_list:
                insert_latest=employees_latest_list[:2]
                res_latest.append(insert_latest)
                employees_latest_list=employees_latest_list[2:]

        x=0
        y=0
        res = []
        N=4
        #Append elements from 'Beltech' emplyee list at position 5 and 6
        #Append elements from 'last 14 days joined' employee list at position 6 and 7
        #Append orginal employees_list at rest of the positions
        for idx, element in enumerate(employees_list):           
            # if index multiple of N
            if idx % N == 0:
                if x < len(res_Beltech) and res_Beltech[x] and idx!=0:
                    for element_in in res_Beltech[x]:
                        res.append(element_in)
                        print(".....index ele in beltech... ",res.index(element_in))
                    x=x+1
                if y < len(res_latest) and res_latest[y] and idx!=0:
                    for element_in in res_latest[y]:
                        res.append(element_in)
                        print(".....index ele in latest... ",res.index(element_in))
                    y=y+1
            res.append(element)
            print(".....index element... ",res.index(element))
        

        return JsonResponse({'employees':res}, safe=False)
        # 'safe=False' for objects serialization


def employee_detail_new(request):
    if request.method == 'GET': 

        # sixe, start, end : for slicing 20 elements based on chunk value
        size = 20
        start = 0
        end = 0
        if 'chunk' in request.GET:
            chunk = int(request.GET['chunk'])
        
        #Query to fetch all elements from databse
        employees = EmployeeSchema.objects.all()
        employees_serializer = EmployeeSerializer(employees, many=True);
        employees_data = list(employees_serializer.data)

        #calculate slice start and end position wrt chunk value
        start=(start+size)*(chunk-1)
        end=(end+size)*(chunk)
        send_data=employees_data[start:end]

        return JsonResponse({'employees':send_data}, safe=False)

