from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Managers
class PublishedManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(status = Post.Status.PUBLISHED)

# Create your models here.
class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = "DF", "Draft"
        PUBLISHED = "PB", "Published"
        REJECTED = "RJ", "Rejected"
    # Relations
    Author = models.ForeignKey(User, on_delete= models.CASCADE, default= 1, related_name = "user_posts")
    # Data fields
    Title = models.CharField(max_length = 250)
    Description = models.TextField()
    Slug = models.SlugField(max_length= 250)
    Publish = models.DateTimeField(default= timezone.now)
    Created = models.DateTimeField(auto_now_add = True)
    Updated = models.DateTimeField(auto_now = True)
    # Choice fields
    status = models.CharField(max_length= 2, choices= Status.choices , default = Status.DRAFT)

    objects = models.Manager() # Original manager
    Published = PublishedManager()# my own manager

    class Meta:
        ordering = ['-Publish']
            # models.Index(fields = ['-Publish'], name='publish_idx')
        indexes = [
            models.Index(fields = ['-Publish'], name='publish_idx')
        ]
    def __str__(self) -> str:
        return self.Title
    
