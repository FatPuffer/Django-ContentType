from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


class CommonCourse(models.Model):
    """
    普通课程
    """
    title = models.CharField(max_length=32)
    # 仅用于反向查找，该课程对应的所有价格策略
    price_policy_list = GenericRelation('PricePolicy')


class DegreeCourse(models.Model):
    """
    学位课程
    """
    title = models.CharField(max_length=32)
    # 仅用于反向查找，该课程对应的所有价格策略
    price_policy_list = GenericRelation('PricePolicy')


class PricePolicy(models.Model):
    """价格策略"""
    price = models.IntegerField()
    period = models.IntegerField()

    # 关联ContentType表：table_name_id
    content_type = models.ForeignKey(ContentType, verbose_name='关联的表名称')
    object_id = models.IntegerField(verbose_name='关联表中的数据行ID')

    # 帮助快速实现content_type操作：快速插入数据
    content_obj = GenericForeignKey('content_type', 'object_id')




