from django.db import models

import uuid
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User,default="")
    username = models.CharField(max_length = 20, help_text = "Enter your name:First Name and Second Name.")
    #comment = models.ManyToManyField("Comment",help_text = "Write your comment for the post.")
    #email = models.EmailField(max_length = 50,help_text = "Enter your e-mail:")
    description = models.TextField(help_text = "Please describe yourself so other can know you.", blank =True)
    phone = models.IntegerField(help_text = "Please enter you phone number.",null=True)
    time = models.DateTimeField(auto_now_add = True)
    userid = models.UUIDField(primary_key = True, default = uuid.uuid4, help_text="Unique ID for this particular user.")

    YEAR_IN_SCHOOL_CHOICES = (
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
    )

    grade = models.CharField(max_length=2, choices=YEAR_IN_SCHOOL_CHOICES, default='FRESHMAN')
    major = models.CharField(max_length = 20, help_text="Please enter your major.",blank=False)

    #class Meta:
        #ordering = ["username"]

    #def get_absolute_url(self):
        #return reverse('user-detail', args=[str(self.id)])
    
    #def __str__(self):
        #return '%s %s %s' % (self.username,self.time, self.userid)

def create_profile(sender, **kwargs):
#if the user is created:
    if kwargs['created']:
    #associate the user being created with that profile when it created account it puts on
        user_profile = UserProfile.objects.create(user = kwargs['instance'])
post_save.connect(create_profile,sender = User)
    

# Required for unique comment instances
class Comment(models.Model):
    context = models.TextField(help_text ="Write your comment.",blank = True)
    #picture = models.ImageField(upload_to = 'photo')
    video = models.URLField(blank=True)
    time = models.DateTimeField(auto_now_add = True)
    #comment = models.ForeignKey('Post', null=True) 
    class Meta:
        ordering = ["time"]

    # Methods
    def get_absolute_url(self):
         return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        return '%s, %s' % (self.context,self.time)

class Post(models.Model):
    title = models.CharField(max_length = 20, help_text ="Your post title.",blank = True)
    context = models.TextField(help_text ="What is in your mind?",blank = True)
    time = models.DateTimeField(auto_now_add = True)
    #picture = models.ImageField(upload_to = 'photo')
    video = models.URLField(blank=True)
   # author = models.ForeignKey('auth.User')

    TYPE_OF_POST = (
        ("---","---"),
        ('clubinfo', 'ClubInfo'),
        ('courseinfo', 'CourseInfo'),
        ('lookforride', 'FreeRide'),
        ('tutor', 'TutorInfo'),
        ('rent', 'RentInfo')
    )
    PostType = models.CharField(max_length=50, choices=TYPE_OF_POST, default='---')

    class Meta:
        ordering = ["time"]
    # Methods
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        return '%s, %s, %s' % (self.title,self.context,self.time)
