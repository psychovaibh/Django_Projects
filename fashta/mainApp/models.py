from django.db import models


class maincategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30,unique=True)

    def __str__(self):
        return str(self.id) + "~ `" + self.name +"`"
    


class subcategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30,unique=True)

    def __str__(self):
        return str(self.id) + "~ `" + self.name +"`"

    

class brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30,unique=True)
    pic = models.ImageField(upload_to="uploads/brand")

    def __str__(self):
        return str(self.id) + "~ `" + self.name +"`"

    
class product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    maincategoryproduct = models.ForeignKey(maincategory,on_delete=models.CASCADE)
    subcategoryproduct = models.ForeignKey(subcategory,on_delete=models.CASCADE)
    brandproduct = models.ForeignKey(brand,on_delete=models.CASCADE)
    baseprice = models.IntegerField()
    discount = models.IntegerField()
    finalprice = models.IntegerField()
    stock = models.BooleanField(default=True)
    color = models.CharField(max_length=20)
    size = models.CharField(max_length=10)
    description = models.TextField(default="This is Sample Product")
    pic1 = models.ImageField(upload_to="uploads/product")
    pic2 = models.ImageField(upload_to="uploads/product",default=None,blank=True,null=True)
    pic3 = models.ImageField(upload_to="uploads/product",default=None,blank=True,null=True)
    pic4 = models.ImageField(upload_to="uploads/product",default=None,blank=True,null=True)


    def __str__(self):
        return str(self.id) + "~ `" + self.name + "`"
    

class buyer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=30,unique=True)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=15,default="")
    address = models.TextField(default="",null=True,blank=True)
    pin = models.IntegerField(default=None,null=True,blank=True)
    city = models.CharField(max_length=30,default="",null=True,blank=True)
    state = models.CharField(max_length=30,default="",null=True,blank=True)
    pic = models.ImageField(upload_to="uploads/users", default="" ,blank=True,null=True)

    def __str__(self):
        return str(self.id) + "~ `" + self.name + "`" + self.username


class wishlist(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(product,on_delete=models.CASCADE)
    buyer = models.ForeignKey(buyer,on_delete=models.CASCADE)

    def __str_(self):
        return str(self.id)+ "~ `"+ self.buyer.username + "`"