from django.db import models

class Event(models.Model):
	'''
	A lecture, lesson, game etc. A thing which you attend
	'''
	title = models.CharField(max_length=200)
	description = models.TextField('text')
	contact = models.CharField(max_length=200)

	def __unicode__(self):
		return self.title


class Location(models.Model):
	"""The locaion of the event"""
	venue = models.CharField(max_length=200)

	def __unicode__(self):
		return self.venue


class Timeslot(models.Model):
	"""The time slot of the event at the location"""
	start_time = models.DateTimeField()
	duration = models.IntegerField()
	event = models.ForeignKey(Event)
	location = models.ForeignKey(Location)
