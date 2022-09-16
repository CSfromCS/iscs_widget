from django.db import models

class WidgetUser(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    id_num = models.CharField(max_length=7, default="123456")
    email = models.EmailField(
        max_length=256, default="john.appleseed@gmail.com")
        
    def __str__(self):
        return self.first_name + " " + self.last_name

    @property
    def id(self):
        return WidgetUser.objects.all().count()