from django.db import models

class HomePage(models.Model):
    main_image = models.ImageField(upload_to="home_page")
    main_image_alt = models.CharField(max_length=250)
    header = models.CharField(max_length=250)
    logo = models.ImageField(upload_to="home_page")
    about_us = models.TextField()
    card_one = models.CharField(max_length=250)
    card_one_description = models.TextField()
    card_one_image = models.ImageField(upload_to="home_page")
    card_two = models.CharField(max_length=250)
    card_two_description = models.TextField()
    card_two_image = models.ImageField(upload_to="home_page")
    card_three = models.CharField(max_length=250)
    card_three_description = models.TextField()
    card_three_image = models.ImageField(upload_to="home_page")
    preporyka1 = models.CharField(max_length=250)
    preporyka2 = models.CharField(max_length=250)
    preporyka3 = models.CharField(max_length=250)

    def __str__(self):
        return "This page have to be only one and edit only"