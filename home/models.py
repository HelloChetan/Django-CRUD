from django.db import models
class Student(models.Model):
        name = models.CharField(max_length=100)
        age = models.IntegerField()
        address = models.CharField(max_length = 100, blank=True, null=True)
        email = models.EmailField()

class Product(models.Model):
    pass

class Car(models.Model):
      name = models.CharField(max_length=100)
      speed = models.IntegerField(default=50)

      def __str__(self):
          return self.name
      
class Bike(models.Model):
     name = models.CharField(max_length=100)
     milage = models.IntegerField(default = 50)
    

     def __str__(self):
        return f"{self.name} - {self.milage}"

      



# Create your models here.
