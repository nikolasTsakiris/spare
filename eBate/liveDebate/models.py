# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models.signals import post_init

from django.db import models

# Create your models here.


class DeBox(models.Model):
	#author = models.ForeignKey(Account)
	#content = models.TextField()

	#created_at = models.DateTimeField(auto_now_add=True)
	#update_at = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return '{0}'.format(self.content)

"""class Debater(models.Model):
    username = models.ForeignKey('auth.User')
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
"""


"""    def idBlessing(self):
        self.id = 

post_init.connect(idBlessing, Debater)


"""



