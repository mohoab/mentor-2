from django.db import models as md , models
class service(md.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date= models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    class Meta :
        ordering = ['-created_date']