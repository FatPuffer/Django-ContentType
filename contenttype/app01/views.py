from django.shortcuts import render, HttpResponse
from .models import DegreeCourse, PricePolicy, ContentType


def test(request):
    # 1.为学位课"python全栈添加一个价格策略，一个月9.9"
    d_obj = DegreeCourse.objects.filter(title='python').first()
    print(d_obj)
    # 获取全栈课程对应的id编号
    d_id = d_obj.id
    # 获取表名对应id
    c_obj = ContentType.objects.filter(model='degreecourse').first()
    c_id = c_obj.id
    # 添加价格策略
    PricePolicy.objects.create(price=9.9, period=1, object_id=d_id, content_type_id=c_id)

    return HttpResponse('OK')

