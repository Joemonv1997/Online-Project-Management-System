from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Sprint(models.Model):
    sprint_id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100,null=False,unique=True)
    Start_date = models.DateField(blank=True,null=True)
    End_date = models.DateField(blank=True,null=True)
    
    def __str__(self):
        return self.Name

class Project(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100,null=False,unique=True)
    sprint_id=models.ForeignKey("Sprint", on_delete=models.CASCADE,default='',related_name="SprintValue")
    Manager=models.ForeignKey(User, default='',on_delete=models.CASCADE)
    def __str__(self):
        return f'Model with Name {self.Name} is created'
class Ticket(models.Model):
    ticket_id=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=300,null=True,blank=False)
    sprint_id=models.ForeignKey("Sprint", on_delete=models.CASCADE,default='')
    project_id=models.ForeignKey("Project", on_delete=models.CASCADE)
    assignee=models.ForeignKey(User, default='',on_delete=models.CASCADE,related_name='assignee')
    reporter=models.ForeignKey(User, default='',on_delete=models.CASCADE,related_name='reporter')
    def __str__(self):
        return self.Name
