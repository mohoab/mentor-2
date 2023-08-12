from django.db import models as md , models
from django.contrib.auth.models import User
#############################################################
class skills(md.Model):
    title = md.CharField(max_length=100)
    
    def __str__(self):
        return self.title
##############################################################
class category(md.Model):
    name = md.CharField(max_length=100)


    def __str__(self):
        return self.name
#############################################################
class trainers(md.Model):
    info = md.ForeignKey( User , on_delete=md.CASCADE)
    skills = md.ManyToManyField(skills)
    description = md.TextField()
    image = models.ImageField(upload_to='trainer', default='trainer/teacher.png')
    twitter = models.CharField(max_length=255, default='#')
    facebook = models.CharField(max_length=255, default='#')
    instagram = models.CharField(max_length=255, default='#')
    linkdin = models.CharField(max_length=255, default='#')
    status = models.BooleanField(default=False)
    updated_datetime = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        self.info.username



#############################################################
class course(md.Model):
    title = md.CharField(max_length=100)
    content = md.TextField()
    price = md.IntegerField(default=0)
    image = md.ImageField(upload_to='course' , default = 'course/default.jpg')
    cg = md.ManyToManyField(category) #category connect to category model
    status = md.BooleanField(default = True )
    counted_view=md.IntegerField()
    counted_like= md.IntegerField()
    created_date=md.DateTimeField(auto_now_add=True)
    update_date = md.DateTimeField(auto_now=True)
    trainer = md.ForeignKey(trainers , on_delete=md.CASCADE)


    class Meta :
         ordering =['-created_date']


    def __str__(self):
        return self.title
    def capt(self):
        return self.title.capitalize()
    def content(self):
        return self.content[:50]

###################################################################