from django.db import models

# Create your models here.
# for Contact
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name
# for login
class User1(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name

# for signup
class User(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    password = models.CharField(max_length=20)
    repeat = models.CharField(max_length=20)

    def __str__(self):
        return self.fname

#for signup
class image(models.Model):
    image=models.ImageField(upload_to='shop/display/',blank='True')
   

'''class birthday(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    address = models.CharField(max_length=70, default="")
    address2 = models.CharField(max_length=500, default="")
    city = models.CharField(max_length=70, default="")

    def __str__(self):
        return self.name'''


# for bithday
class birth(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    address = models.CharField(max_length=70, default="")
    address2 = models.CharField(max_length=500, default="")
    city = models.CharField(max_length=70, default="")

    def __str__(self):
        return self.name


# for graduation
class greduation(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    address = models.CharField(max_length=70, default="")
    address2 = models.CharField(max_length=500, default="")
    city = models.CharField(max_length=70, default="")

    def __str__(self):
        return self.name

# for wedding
class weds(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    address = models.CharField(max_length=70, default="")
    address2 = models.CharField(max_length=500, default="")
    city = models.CharField(max_length=70, default="")

    def __str__(self):
        return self.name