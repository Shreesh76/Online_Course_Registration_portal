from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.core.validators import MinValueValidator, RegexValidator
from PIL import Image
from django.utils.timezone import now


class Courses(models.Model):
    name = models.CharField(max_length=500)
    desp = models.TextField()
    image = models.ImageField(upload_to='courses')
    time_to_cover = models.CharField(max_length=50)
    teacher = models.ForeignKey("teachers",on_delete=models.CASCADE)
    fee = models.FloatField()
    students = models.ManyToManyField("Profile")

    class Meta:
        app_label = 'validate'

    def __str__(self):
        return self.name
    

class teachers(models.Model):
    name = models.CharField(max_length=500)
    desp = models.TextField()
    qualification = models.TextField()
    image = models.ImageField(upload_to='profile_pics')
    department_name = models.ForeignKey("Department",on_delete=models.CASCADE)

    class Meta:
        app_label = 'validate'

    def __str__(self):
        return self.name
    

class Department(models.Model):
    name = models.CharField(max_length=500)
    desp = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to='profile_pics',null=True,blank=True)

    class Meta:
        app_label = 'validate'

    def __str__(self):
        return f"{self.name}"
    


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Name = models.CharField(default = "First Name",max_length=50)
    Roll_No = models.CharField(default = "ABC120",max_length=10)
    Year = models.CharField(default = "First Year", choices = (("First Year","First Year"), 
                                                               ("Second Year","Second Year"),
                                                               ("Third Year","Third Year"),
                                                               ("Final Year","Final Year")), 
                                                               max_length=50)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    department = models.ForeignKey("Department", on_delete=models.CASCADE)
    validated = models.BooleanField(default=False)

    class Meta:
        app_label = 'validate'

    def __str__(self):
        return self.user.username
        
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    