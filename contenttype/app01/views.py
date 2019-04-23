from django.shortcuts import render, HttpResponse
from .models import DegreeCourse, PricePolicy, CommonCourse


def test(request):
    # 1.为学位课"python全栈添加一个价格策略，一个月9.9"
    d_obj = DegreeCourse.objects.filter(title='python').first()
    PricePolicy.objects.create(price=9.9, period=1, content_obj=d_obj)

    return HttpResponse('OK')


def test1(request, id):
    # 1.根据学位课程ID获取课程，并获取该课程对应的所有价格策略
    course = DegreeCourse.objects.filter(id=id).first()
    # 对象列表
    price_policys = course.price_policy_list.all()
    print(price_policys)

    return HttpResponse('OK')
