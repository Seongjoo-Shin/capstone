from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Customer
from .serializers import CustomerSerializer, NoPasswordSerializer,IdSerializer,PasswordSerializer
from rest_framework.parsers import JSONParser

@csrf_exempt
def customer_list(request) :
    #회원가입
    if request.method == 'POST' :
        data = JSONParser().parse(request)
        serializer = CustomerSerializer(data=data)
        if serializer.is_valid() :
            serializer.save()
            return HttpResponse(status=200)
        return HttpResponse(status=400)
    #id or 폰번 or 이메일 중복체크 
    elif request.method == 'GET' :
        info = int(request.GET.get('info',None))
        data = request.GET.get('data',None)

        if info == 0 : #id중복
            if (Customer.objects.filter(user_id=data).count()) == 0 :
                return HttpResponse(status=200) #중복아님
            else :
                return HttpResponse(status=400) #중복
        elif info == 1 : #이메일 중복
            if (Customer.objects.filter(email=data).count()) == 0 :
                return HttpResponse(status=200)
            else :
                return HttpResponse(status=400)
        elif info == 2 : #폰번호 중복
            if (Customer.objects.filter(phone=data).count()) == 0 :
                return HttpResponse(status=200)
            else :
                return HttpResponse(status=400)
        
        return HttpResponse(status = 401) #들어오는 정보 잘못됨. 0,1,2 중 하나여야됨
    

@csrf_exempt
def customer(request,user_id) :
    try :
        obj = Customer.objects.get(user_id = user_id)
    except : 
        return HttpResponse(status=400)

    #유저 정보 조회
    if request.method == "GET" :
        serializer = NoPasswordSerializer(obj)
        return JsonResponse(serializer.data, status = 200)

    #비밀번호 변경
    elif request.method == "PUT" :
        data = JSONParser().parse(request) 
        existing_pw = data['existing_pw']
        new_pw = data['new_pw']

        print("obj_id : " + obj.user_id)
        print("existing_pw : " + existing_pw)
        print("new_pw : " + new_pw)

        if obj.password == existing_pw :
            if existing_pw != new_pw :
                obj.password = new_pw
                obj.save()
                return HttpResponse(status = 200)
            else :
                return HttpResponse(status = 401) # 기존의 비밀번호랑 같음
        else :
            return HttpResponse(status = 402) #현재 비밀번호 틀림



@csrf_exempt
#로그인
def login(request) :
    if request.method == 'POST' :
        data = JSONParser().parse(request)
        search_id = data['user_id']
        
        try :
            obj = Customer.objects.get(user_id=search_id)
        except :
            return HttpResponse(status=404)
            #404 - id 없음


        if data['password'] == obj.password :
            serializer = IdSerializer(obj)
            return JsonResponse(serializer.data,status=200)
        else :
            return HttpResponse(status=400)
            #password 불일치

def find_pw(request) :
    if request.method == "GET" :
        user_id = request.GET.get('user_id',None)
        name = request.GET.get('name',None)
        birth = request.GET.get('birth',None)

        try :
            obj = Customer.objects.get(user_id = user_id, name = name, birth = birth)
        except :
            return HttpResponse(status = 400) #정보 불일치

        serializer = PasswordSerializer(obj)
        return JsonResponse(serializer.data)


def find_id(request) :
    if request.method == "GET" :
        name = request.GET.get('name',None)
        phone = request.GET.get('phone',None)

        try :
            obj = Customer.objects.get(name = name, phone = phone)
        except :
            return HttpResponse(status = 400) #정보 불일치

        serializer = IdSerializer(obj)
        return JsonResponse(serializer.data)