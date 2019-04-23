from django.shortcuts import render, HttpResponse
from .models import DegreeCourse, PricePolicy, ContentType


def test(request):
    # 1.为学位课"python全栈添加一个价格策略，一个月9.9"
    d_obj = DegreeCourse.objects.filter(title='python').first()
    PricePolicy.objects.create(price=9.9, period=1, content_obj=d_obj)

    return HttpResponse('OK')

