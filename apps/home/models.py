from django.db import models

# Create your models here.


class Contact(models.Model):
    company_name = models.CharField(max_length=100, blank=True, null=True)
    logo = models.ImageField(blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    additional_email = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    address_line_2 = models.CharField(max_length=200, null=True, blank=True)
    about_us = models.TextField(blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    youtube = models.CharField(max_length=100, blank=True, null=True)
    linkedin = models.CharField(max_length=100, blank=True, null=True)
    instagram = models.CharField(max_length=100, blank=True, null=True)
    tiktok = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.company_name


class Slider(models.Model):
    title = models.CharField(max_length=250, blank=True,null=True)
    sub_title = models.CharField(max_length=250, blank=True,null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    cta = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.title


class AboutUs(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    contact = models.CharField(max_length=200, blank=True,null=True)
    cta = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title


class OurService(models.Model):
    title = models.CharField(max_length=100,blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    cta = models.CharField(max_length=50, blank=True, null=True, default='READ MORE')
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    photo = models.ImageField(blank=True, null=True, default='https://cdn-icons-png.flaticon.com/512/21/21104.png')
    name = models.CharField(max_length=100, blank=True, null=True)
    review = models.TextField(blank=True, null=True)
    designation = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.name


class WhyChooseUs(models.Model):
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    numbers = models.PositiveIntegerField(null=True, blank=True, default="100")
    decription = models.CharField(max_length=250,null=True, blank=True)

    def __str__(self):
        return self.title


