# coding:utf-8
from django.contrib.auth.models import User 
from django.db import models
class Block(models.Model):
	name = models.CharField(u"版块名称",max_length=50)  #这里写name就好了，不用写block_name ,block类就是一个命名空间的作用 block = Block(...) block.name
	desc = models.CharField(u"版块描述",max_length=100)
	manager = models.ForeignKey(User,verbose_name="管理员")
	
	create_timestamp = models.DateTimeField(auto_now_add = True)
	last_update_timestamp = models.DateTimeField(auto_now = True)
	
	def __unicode__(self):
		return self.name
	
	class Meta:
		verbose_name = u"板块"
		verbose_name_plural = u"板块"	
		
# Create your models here.

