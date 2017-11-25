# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Course(models.Model):
	STATUS = {
		('G', 'General'), # General = General + Restricted
		('R', 'Restricted'), # Only Restricted
	}
	# Hidden id: course_id is the PK.
	subject = models.CharField(max_length=20, blank=True, verbose_name="Subject Code") # ie) CPSC
	course = models.CharField(max_length=20, blank=True, verbose_name="Course Code") # ie) 110
	section = models.CharField(max_length=20, blank=True, verbose_name="Section Code") # ie) L1A
	activity = models.CharField(max_length=20, blank=True, verbose_name="Activity Type") # ie) Lab
	url = models.CharField(max_length=100, blank=True, verbose_name="URL") # ie) https://courses.students.ubc.ca/cs/main?pname=subjarea&tname=subjareas&req=5&dept=CPSC&course=110&section=L1A
	status = models.CharField(max_length=20, choices=STATUS, verbose_name="Status") # ie) G

class User(models.Model):
	course = models.ForeignKey(Course)
	email = models.EmailField(max_length=70,blank=False)
