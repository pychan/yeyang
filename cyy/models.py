from django.db import models
# Create your models here.
class Article(models.Model):
	content				= models.TextField(blank=True)
	pic_addr			= models.ImageField(upload_to='picture/',blank=True)
	tags				= models.CharField(blank=True,max_length=100)
	date_time			= models.DateField(auto_now_add=True)
	comment_count		= models.IntegerField(blank=True)
    	
	def __unicode__(self):
		return self.content


class Comment(models.Model):
	article				= models.ForeignKey(Article)
	msg					= models.TextField()
	from_addr			= models.CharField(max_length=50)		
	to_addr				= models.CharField(max_length=50)
	post_time			= models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.msg
