from django.db import models


class Course(models.Model):
    """
    ��ͨ�γ�
    """
    title = models.CharField(max_length=32)


class DegreeCourse(models.Model):
    """
    ѧλ�γ�
    """
    title = models.CharField(max_length=32)


class PricePolicy(models.Model):
    """�۸����"""
    price = models.IntegerField()
    period = models.IntegerField()

    table_name = models.CharField(verbose_name='�����ı�����')
    object_id = models.CharField(verbose_name='�������е������е�ID')







