from django.db import models
from django.utils.text import slugify
from django.utils.crypto import get_random_string
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length = 200)
    slug = models.SlugField(unique=True, blank=True,null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            while Category.objects.filter(slug=self.slug).exists():
                self.slug= f'{slugify(self.title)}-{get_random_string(4)}'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title     


    class Meta:
        verbose_name_plural = "Categories"


class BlogPost(models.Model):
    STATUS = [
        ('draft', 'Draft'),
        ('published', 'Publish')
    ]



    title = models.CharField(max_length = 200)
    slug = models.SlugField(unique=True, blank=True,null=True)
    featured = models.ImageField(upload_to='blog/', blank=True, null=True)
    #content = RichTextField()
    content = RichTextUploadingField()
    created = models.DateTimeField(auto_now_add=True)  
    updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices = STATUS, default='draft')
    meta_title = models.CharField(max_length=200, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            while BlogPost.objects.filter(slug=self.slug).exists():
                self.slug= f'{slugify(self.title)}-{get_random_string(4)}'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title    


    class Meta:
        verbose_name_plural = "All Posts" 

class Comment(models.Model):
    BlogPost = models.ForeignKey(BlogPost,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)



  







