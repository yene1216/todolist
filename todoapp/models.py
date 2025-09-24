from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Todolist(models.Model):
    title=models.CharField(max_length=155)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    completed=models.BooleanField(default=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} {self.description} {self.created_at} {self.completed} {self.user}"