from django.shortcuts import render, HttpResponse
from .models import DegreeCourse, PricePolicy, ContentType


def test(request):
    # 1.Ϊѧλ��"pythonȫջ���һ���۸���ԣ�һ����9.9"
    d_obj = DegreeCourse.objects.filter(title='python').first()
    print(d_obj)
    # ��ȡȫջ�γ̶�Ӧ��id���
    d_id = d_obj.id
    # ��ȡ������Ӧid
    c_obj = ContentType.objects.filter(model='degreecourse').first()
    c_id = c_obj.id
    # ��Ӽ۸����
    PricePolicy.objects.create(price=9.9, period=1, object_id=d_id, content_type_id=c_id)

    return HttpResponse('OK')

