from django.db import models

# Create your models here.

class aboutPageContent(models.Model):
    class Meta():
        db_table = 'aboutpagecontent'
        ordering = ['id']
    name = models.CharField(max_length=120)
    heading = models.CharField(max_length=120,blank=True)
    paragraph = models.TextField(blank=True)
    img = models.ImageField(upload_to='about_img',blank=True)
    img_width = models.CharField(max_length=20, default=0)
    img_height = models.CharField(max_length=20, default=0)
    def __str__(self):
        return self.name

class homePageContent(models.Model):
    class Meta():
        db_table = 'homepagecontent'
        ordering = ['id']

    name = models.CharField(max_length=120)
    heading = models.CharField(max_length=120, blank=True)
    paragraph = models.TextField(blank=True)
    img = models.ImageField(upload_to='home_img',blank=True)
    img_width = models.CharField(max_length=20, default=0)
    img_height = models.CharField(max_length=20, default=0)
    def __str__(self):
        return self.name

class Articles(models.Model):
    class Meta():
        db_table = 'articles'
        ordering = ['-date']
    title = models.CharField(max_length=120)
    post = models.TextField()
    date = models.DateTimeField()
    img = models.ImageField(upload_to='articles_img',blank=True)
    img_width = models.CharField(max_length=20, default=0)
    img_height = models.CharField(max_length=20, default=0)

    def __str__(self):
        return self.title
