from django.db import models 
from django.contrib.auth.models import User

#Family

class Family(models.Model):
    event_type = models.CharField(max_length = 300)
    desc = models.TextField()
    image = models.ImageField(upload_to = "family_images")
    food = models.CharField(max_length = 200)
    decoration = models.CharField(max_length = 500)
    user = models.ForeignKey(User, on_delete = models.CASCADE, default = " ")

    def __str__(self):
        return self.name
    
    
 #Charity 
    
class Charity(models.Model):
    event_type = models.CharField(max_length = 300)
    desc = models.TextField()
    image = models.ImageField(upload_to = "charity_images")
    food = models.CharField(max_length = 200)
    decoration = models.CharField(max_length = 500)
    chief_guest = models.CharField(max_length = 100)
    sponsor = models.CharField(max_length = 100)
    user = models.ForeignKey(User, on_delete = models.CASCADE, default = " ")

    def __str__(self):
        return self.name
    
    
#Business

class Business(models.Model):    
    event_type = models.CharField(max_length = 300)
    desc = models.TextField()
    image = models.ImageField(upload_to = 'business_image')
    food = models.CharField(max_length = 200)
    chief_guest = models.CharField(max_length = 100)
    user = models.ForeignKey(User, on_delete = models.CASCADE, default = " ")
    
    def __str__(self):
        return self.name
    
    
#Culture

class Culture(models.Model):
    event_type = models.CharField(max_length = 300)
    desc = models.TextField()
    image = models.ImageField(upload_to = 'culture_image')
    food = models.CharField(max_length = 200)
    chief_guest = models.CharField(max_length = 100)
    user = models.ForeignKey(User, on_delete = models.CASCADE, default = " ")
    
    def __str__(self):
        return self.name
    
    
    
class Venue(models.Model):
    name = models.CharField(max_length = 50)
    address = models.CharField(max_length = 500)
    capacity = models.IntegerField()
    desc = models.TextField()
    image = models.ImageField(upload_to = "venue")
    
    def __str__(self):
        return self.name
    
#Book Event

class Book_event(models.Model):
    name = models.CharField(max_length = 100)
    mobile = models.CharField(max_length = 14)
    email = models.EmailField()
    location = models.CharField(max_length = 100)
    people = models.IntegerField()
    date = models.DateField()
    event = models.CharField(max_length = 100)
    food = models.CharField(max_length = 100)
    address = models.CharField(max_length = 500)
    venue = models.ForeignKey(Venue, on_delete = models.CASCADE, default = " ")
    message = models.TextField()
    
    def __str__(self):
        return self.name
        
#Contact us

class Contact_us(models.Model):
    name = models.CharField(max_length = 50)
    mobile = models.CharField(max_length = 14)
    email = models.EmailField()
    message = models.TextField()
    
    def __str__(self):
        return self.name 
    
    
    
    