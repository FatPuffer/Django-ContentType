from django.shortcuts import render, HttpResponse
from .models import DegreeCourse, PricePolicy, CommonCourse


def test(request):
    # 1.Ϊѧλ��"pythonȫջ���һ���۸���ԣ�һ����9.9"
    d_obj = DegreeCourse.objects.filter(title='python').first()
    PricePolicy.objects.create(price=9.9, period=1, content_obj=d_obj)

    return HttpResponse('OK')


def test1(request, id):
    # 1.����ѧλ�γ�ID��ȡ�γ̣�����ȡ�ÿγ̶�Ӧ�����м۸����
    course = DegreeCourse.objects.filter(id=id).first()
    # �����б�
    price_policys = course.price_policy_list.all()
    print(price_policys)

    return HttpResponse('OK')
