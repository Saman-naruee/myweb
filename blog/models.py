from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = "DF", "Draft"
        PUBLISHED = "PB", "Published"
        REJECTED = "RJ", "Rejected"
    # Relations
    auther = models.ForeignKey(User, on_delete= models.CASCADE, related_name = "user_posts")
    # Data fields
    Title = models.CharField(max_length = 250)
    Description = models.TextField()
    Slug = models.SlugField(max_length= 250)
    Publish = models.DateTimeField(default= timezone.now)
    Created = models.DateTimeField(auto_now_add = True)
    Updated = models.DateTimeField(auto_now = True)
    # Choice fields
    status = models.CharField(max_length= 2, choices= Status.choices , default = Status.DRAFT)

    class Meta:
        ordering = ['-Publish']
        indexes = [
            models.Index(fields=['-Publish'], name='publish_idx'),
        ]
    def __str__(self) -> str:
        return self.Title
    
