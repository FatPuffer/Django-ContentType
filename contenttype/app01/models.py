from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class CommonCourse(models.Model):
    """
    普通课程
    """
    title = models.CharField(max_length=32)


class DegreeCourse(models.Model):
    """
    学位课程
    """
    title = models.CharField(max_length=32)


class PricePolicy(models.Model):
    """价格策略"""
    price = models.IntegerField()
    period = models.IntegerField()

    # 关联ContentType表：table_name_id
    content_type = models.ForeignKey(ContentType, verbose_name='关联的表名称')
    object_id = models.IntegerField(verbose_name='关联表中的数据行ID')





