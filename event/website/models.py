from django.db import models 
from django.contrib.auth.models import User

#Family

class Family(models.Model):
    event_type = models.CharField(max_length = 300)
    desc = models.TextField()
    image = models.ImageField(upload_to = "family_images")
    food = models.ForeignKey('website.Food', on_delete = models.CASCADE, default = "")
    decoration = models.CharField(max_length = 500)
    user = models.ForeignKey(User, on_delete = models.CASCADE, default = " ")

    def __str__(self):
        return self.event_type
    
    
 #Charity 
    
class Charity(models.Model):
    event_type = models.CharField(max_length = 300)
    desc = models.TextField()
    image = models.ImageField(upload_to = "charity_images")
    food = models.ForeignKey('website.Food', on_delete = models.CASCADE, default = "")
    decoration = models.CharField(max_length = 500)
    chief_guest = models.CharField(max_length = 100)
    sponsor = models.CharField(max_length = 100)
    user = models.ForeignKey(User, on_delete = models.CASCADE, default = " ")

    def __str__(self):
        return self.namevent_type
    
    
#Business

class Business(models.Model):    
    event_type = models.CharField(max_length = 300)
    desc = models.TextField()
    image = models.ImageField(upload_to = 'business_image')
    food = models.ForeignKey('website.Food', on_delete = models.CASCADE, default = "")
    chief_guest = models.CharField(max_length = 100)
    user = models.ForeignKey(User, on_delete = models.CASCADE, default = " ")
    
    def __str__(self):
        return self.event_type
    
    
#Culture

class Culture(models.Model):
    event_type = models.CharField(max_length = 300)
    desc = models.TextField()
    image = models.ImageField(upload_to = 'culture_image')
    food = models.ForeignKey('website.Food', on_delete = models.CASCADE, default = "")
    chief_guest = models.CharField(max_length = 100)
    user = models.ForeignKey(User, on_delete = models.CASCADE, default = " ")
    
    def __str__(self):
        return self.event_type
    
class Food(models.Model):
    package = models.CharField(max_length = 200)
    item1 = models.CharField(max_length = 50)
    item2 = models.CharField(max_length = 50)
    item3 = models.CharField(max_length = 50)
    item4 = models.CharField(max_length = 50)
    pack_price = models.IntegerField()
    
    def __str__(self):
        return self.package
    
    
    
class Venue(models.Model):
    name = models.CharField(max_length = 50)
    address = models.CharField(max_length = 500)
    capacity = models.IntegerField()
    desc = models.TextField()
    image = models.ImageField(upload_to = "venue")
    price = models.IntegerField()
    
    def __str__(self):
        return self.name
    
#Book Event

class Book_event(models.Model):
    name = models.CharField(max_length = 100)
    mobile = models.CharField(max_length = 14)
    email = models.EmailField()
    people = models.IntegerField()
    date = models.DateField()
    event = models.CharField(max_length = 100)
    food =  models.ForeignKey('website.Food', on_delete = models.CASCADE, default = "")
    address = models.CharField(max_length = 500)
    venue = models.ForeignKey(Venue, on_delete = models.CASCADE, default = " ")
    message = models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE, default='')
    bill = models.IntegerField()
    
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
