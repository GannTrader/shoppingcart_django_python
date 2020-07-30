from django.db import models

# Create your models here.
class products(models.Model):
	title = models.CharField(max_length = 255)
	description = models.TextField()
	image = models.FileField()
	price = models.IntegerField()

	def __str__ (self):
		return self.title