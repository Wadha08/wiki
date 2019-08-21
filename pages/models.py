from django.db import models




class Page(models.Model):
	title = models.CharField(max_length=30)
	content = models.TextField()
	last_update = models.DateTimeField(auto_now=True)

	def get_absolute_url(self):
		from django.urls import reverse
		return reverse('page_detail', args=[str(self.id)])




# Create your models here.
