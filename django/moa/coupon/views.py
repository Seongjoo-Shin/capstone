# from django.shortcuts import render

# # Create your views here.
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse 
from django.views.decorators.csrf import csrf_exempt 
from .models import Coupon
from account.models import Customer
from .serializers import CouponSerializer
from rest_framework.parsers import JSONParser
from fuser.models import Fuser
from management.models import Manager

@csrf_exempt
def coupon(request) : # in mobile app
    if request.method == "GET" :
        data = JSONParser().parser(request.data)
        try :
            obj = Coupon.object.get(customer = data['customer'],store =data['store'] )
        except :
            return HttpResponse(status=400)

        serializer = CouponSerializer(obj)
        return JsonResponse(serializer.data, status=201)


# on computer
def aboutcoupon(request):
    customers = Coupon.objects.all()
    context= {'customers':customers}
    
    session_id = request.session.session_key
    user = request.session['user']

    contents = {'user': user, 'session_id': session_id}

    if request.method == "POST":
        find_user_id = request.POST.get('userid', None)
        find_user_phone = request.POST.get('userphone', None)
        

        current_cnt = Coupon.objects.get(customer_id=find_user_id)
        cafe = Fuser.objects.get(user_id='무중카페').cafe_name 
        stamp = Manager.objects.get(cafe_name=cafe).cafe_stamp
    
        if request.POST.get('save_coupon'):        
            current_cnt.current_cnt = current_cnt.current_cnt + 1
            current_cnt.save()
            return render(request, 'aboutcoupon.html', {'current_cnt':current_cnt.current_cnt})            
        
        elif request.POST.get('use_coupon'):
            if current_cnt.current_cnt >= stamp:
                avail = current_cnt.current_cnt // stamp
                messages.info(request, '사용 가능 %d'%(avail))
                current_cnt.current_cnt = current_cnt.current_cnt - stamp
                current_cnt.save()
                return render(request, 'aboutcoupon.html', {'current_cnt':current_cnt.current_cnt})
            else:
                return render(request, 'aboutcoupon.html', {'current_cnt':current_cnt.current_cnt})
            


    return render(request, 'aboutcoupon.html', contents)