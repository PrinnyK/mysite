# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.

class article(models.Model):
	#博文
	title = models.CharField('标题', max_length=150)
	content = models.TextField('内容', )
	date = models.DateTimeField('发表时间', auto_now=True)
	category = models.ForeignKey('category', verbose_name='标签')
	#'category'是类名，并非名称

	def __str__(self):
		return self.title

class category(models.Model):
	#标签
	title = models.CharField('标签', max_length=50)

	def __str__(self):
		return self.title
