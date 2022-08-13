
from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
 
def one_week():
    return timezone.now()+timezone.timedelta(days=7)

class todoList(models.Model):
    title=models.CharField(max_length=100,unique=True)

    def get_absolute_url(self):
        return reverse("list", args=[self.id])
    
    def __str__(self):
        return self.title

class todoItem(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=200,null=True,blank=True)
    created_date=models.DateTimeField(auto_now_add=True)
    due_date=models.DateTimeField(default=one_week)
    
    def get_absolute_url(self):
        return reverse("item-update", kwargs=[str(self.todoList.id),str(self.id)])

    def __str__(self):
        return f"{self.title}: due{self.due_date}"
    class  meta:
        ordering=["due_date"]
