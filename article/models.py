from django.db import models
from time import time
from django.utils import timezone


def get_upload_file_name(instance, filename):
    #return "uploaded_files/%s_%s" % (str(time()).replace('.','_'), filename)
    return "uploaded_files/%s" % (filename)


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    notes = models.CharField(max_length=500, default="none")
    algorithm = models.CharField(max_length=200)
    angle_start = models.FloatField()
    angle_end = models.FloatField()
    angle_step = models.FloatField()
    save_to = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published', default=timezone.now())
    likes = models.IntegerField(default=0)
    upload_file = models.FileField(upload_to=get_upload_file_name)

    #def get_name(self, request):
    #    self.myname = request.user.username
    #    return

    myname = models.CharField(max_length=200, default="none")  ###username

    def __unicode__(self):
        return self.title


class JobData(models.Model):
    job_id = models.IntegerField()
    tool_name = models.CharField(max_length=200)
    tool_id = models.IntegerField()

    def __unicode__(self):
        return self.title



class Comment(models.Model):
    name = models.CharField(max_length=200)
    body = models.TextField()

    article = models.ForeignKey(Article)


