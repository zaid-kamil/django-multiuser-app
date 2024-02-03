from django.db import models
from django.contrib.auth.models import User, Group


class ManagerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='manager/', default='default.jpg')
    position = models.CharField(max_length=100, default='Manager')
    # other details

    def __str__(self):
        return self.user.username
    
class EmployeeProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='employee/', default='default.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    position = models.CharField(max_length=100, default='Employee')
    manager = models.ForeignKey(ManagerProfile, on_delete=models.CASCADE, default=None, null=True, blank=True)
    # other details

    def __str__(self):
        return self.user.username
    
class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='customer/', default='default.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # other details

    def __str__(self):
        return self.user.username

    



