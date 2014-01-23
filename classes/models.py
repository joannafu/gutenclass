from django.db import models

class Class(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField()
    room = models.CharField(max_length=255)
    outline = models.FileField(upload_to='lessons/')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name=u'Class'
        verbose_name_plural=u'Classes'