from django.db import models

# Create your models here.
class Project(models.Model):
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=200)


	def __str__(self):
		return self.title

class tasks(models.Model):
	project = models.ForeignKey(Project, null=True,blank=True, on_delete=models.CASCADE, related_name="tasks")
	title = models.CharField(max_length=200)
	done = models.BooleanField(default=False)


	def __str__(self):
		return self.title