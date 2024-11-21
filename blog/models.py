from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import RegexValidator

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
    Author = models.ForeignKey(User, on_delete= models.CASCADE, default= 1, related_name = "user_posts", verbose_name = 'نویسنده')
    # Data fields
    Title = models.CharField(max_length = 250, verbose_name = "عنوان")
    Description = models.TextField(verbose_name = 'توضیحات')
    Slug = models.SlugField(max_length= 250)
    Publish = jmodels.jDateTimeField(default= timezone.now, verbose_name = 'زمان انتشار')
    Created = jmodels.jDateTimeField(auto_now_add = True)
    Updated = jmodels.jDateTimeField(auto_now = True)
    # Choice fields
    status = models.CharField(max_length= 2, choices= Status.choices , default = Status.DRAFT, verbose_name = 'وضعیت') 

    # objects = models.Manager() # Original manager
    objects = PublishedManager()
    Published = PublishedManager()# my own manager

    class Meta:
        ordering = ['-Publish']
            # models.Index(fields = ['-Publish'], name='publish_idx')
        indexes = [
            models.Index(fields = ['-Publish'], name='publish_idx')
        ]
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'




    def __str__(self) -> str:
        return self.Title
    
    def get_absolute_url(self):
        return reverse('blog:post_detail', args= [str(self.id)])
    
    def save(self, *args, **kwargs):
        if not self.id:  # Newly created object
            self.slug = slugify(self.Title)
        super().save(*args, **kwargs)

class Ticket(models.Model):
    message = models.TextField(verbose_name = 'پیام')
    email = models.EmailField(verbose_name = 'ایمیل')
    name = models.CharField(max_length= 250, verbose_name = 'نام')
    subject = models.CharField(max_length= 250, verbose_name = 'موضوع')
    phone = models.CharField(
        max_length= 11,
        verbose_name = 'شماره تلفن',
        help_text= 'شماره تلفن باید 11 رقم باشد',
        validators=[
            RegexValidator(
                regex=r'^09\d{9}$', 
                message='شماره تلفن باید با 09 شروع شود و جمعا 11 رقم باشد.',
            ),
        ]
    )

    def __str__(self) -> str:
        return str(self.subject)
    
    class Meta:
        verbose_name = 'تیکت'
        verbose_name_plural = 'تیکت ها'

