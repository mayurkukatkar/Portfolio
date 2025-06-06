from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=100)
    bio = RichTextField()
    profile_image = models.ImageField(upload_to='profile/')
    resume = models.FileField(upload_to='resumes/')
    contact_email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    tech_stack = models.CharField(max_length=255)
    image = models.ImageField(upload_to='projects/')
    github_link = models.URLField()
    live_link = models.URLField()
    tags = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('database', 'Database'),
        ('devops', 'DevOps'),
        ('other', 'Other'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    level = models.IntegerField(help_text='Skill level from 1-100')
    icon = models.ImageField(upload_to='skills/')
    
    def __str__(self):
        return f"{self.name} ({self.category})"
    
    class Meta:
        ordering = ['category', 'name']

class Experience(models.Model):
    TYPE_CHOICES = [
        ('work', 'Work'),
        ('edu', 'Education'),
    ]
    
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    description = RichTextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    current = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.title} at {self.company}"
    
    class Meta:
        ordering = ['-start_date']

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    message = RichTextField()
    image = models.ImageField(upload_to='testimonials/', null=True, blank=True)
    
    def __str__(self):
        return f"Testimonial from {self.name}"

class Blog(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    content = RichTextField()
    cover_image = models.ImageField(upload_to='blogs/')
    tags = models.CharField(max_length=255)
    meta_title = models.CharField(max_length=255)
    meta_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    class Meta:
        ordering = ['-created_at']

class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Message from {self.name} on {self.submitted_at.strftime('%Y-%m-%d')}"
    
    class Meta:
        ordering = ['-submitted_at']

class GlobalSetting(models.Model):
    site_title = models.CharField(max_length=255)
    site_description = models.TextField()
    footer_text = models.CharField(max_length=255)
    social_links = models.JSONField()
    
    def __str__(self):
        return "Global Settings"
    
    class Meta:
        verbose_name = "Global Setting"
        verbose_name_plural = "Global Settings"
