from django.db import models

# Create your models here.
class about(models.Model):
    about_paragraph=models.TextField(blank=True,null=True)

    def __str__(self):
         return self.about_paragraph
class products(models.Model):
    CATEGORY = (
            
            ('Kids Apparel','Kids Apparel'),
            ('Women Apparel','Women Apparel'),
            ('Men Apparel','Men Apparel'),
            )
    thumbnail=models.ImageField(upload_to="media/",max_length=250,null=True,default=None)
    products_name=models.TextField(blank=True,null=True)
    category =models.CharField(max_length=200,null=False,choices=CATEGORY)
    products_img1=models.ImageField(upload_to="media/",max_length=250,null=True,default=None)
    products_img2=models.ImageField(upload_to="media/",max_length=250,null=True,default=None)
    products_img3=models.ImageField(upload_to="media/",max_length=250,null=True,default=None)
    products_img4=models.ImageField(upload_to="media/",max_length=250,null=True,default=None)
    products_img5=models.ImageField(upload_to="media/",max_length=250,null=True,default=None)
    products_img6=models.ImageField(upload_to="media/",max_length=250,null=True,default=None)
    products_img7=models.ImageField(upload_to="media/",max_length=250,null=True,default=None)
    products_img8=models.ImageField(upload_to="media/",max_length=250,null=True,default=None)
    products_img9=models.ImageField(upload_to="media/",max_length=250,null=True,default=None)
    products_img10=models.ImageField(upload_to="media/",max_length=250,null=True,default=None)
    products_img11=models.ImageField(upload_to="media/",max_length=250,null=True,default=None)
    products_img12=models.ImageField(upload_to="media/",max_length=250,null=True,default=None)
    products_img13=models.ImageField(upload_to="media/",max_length=250,null=True,default=None)
    products_img14=models.ImageField(upload_to="media/",max_length=250,null=True,default=None)
    products_img15=models.ImageField(upload_to="media/",max_length=250,null=True,default=None)
    products_img16=models.ImageField(upload_to="media/",max_length=250,null=True,default=None)
    products_img17=models.ImageField(upload_to="media/",max_length=250,null=True,default=None)
    products_img18=models.ImageField(upload_to="media/",max_length=250,null=True,default=None)
    products_img19=models.ImageField(upload_to="media/",max_length=250,null=True,default=None)
    products_img20=models.ImageField(upload_to="media/",max_length=250,null=True,default=None)
    products_img21=models.ImageField(upload_to="media/",max_length=250,null=True,default=None)
    products_img22=models.ImageField(upload_to="media/",max_length=250,null=True,default=None)
    products_img23=models.ImageField(upload_to="media/",max_length=250,null=True,default=None)
    products_img24=models.ImageField(upload_to="media/",max_length=250,null=True,default=None)
    products_img25=models.ImageField(upload_to="media/",max_length=250,null=True,default=None)
    products_img26=models.ImageField(upload_to="media/",max_length=250,null=True,default=None)
    products_img27=models.ImageField(upload_to="media/",max_length=250,null=True,default=None)
    products_img28=models.ImageField(upload_to="media/",max_length=250,null=True,default=None)
    products_img29=models.ImageField(upload_to="media/",max_length=250,null=True,default=None)
    products_img30=models.ImageField(upload_to="media/",max_length=250,null=True,default=None)
    

    

class whywe(models.Model):
    whywe_halfheading=models.TextField(blank=True,null=True)
    whywe_secondhalfheading=models.TextField(blank=True,null=True)
    whywe_paragraph=models.TextField(blank=True,null=True)
    whywe_images=models.ImageField(upload_to="media/",blank=True,null=True)
    
    def __str__(self):
         return self.whywe_paragraph




class certificates(models.Model):
    
    certificates_names=models.TextField(blank=True,null=True)
    delay=models.IntegerField(default="150",blank=True,null=True)
    certificates_images=models.ImageField(upload_to="media/",null=True,blank=True)
    def __str__(self):
         return self.certificates_names


    
class services(models.Model):
    service_icon=models.TextField(blank=True,null=True)
    service_heading=models.TextField(blank=True,null=True)
    service_minidescrip=models.TextField(blank=True,null=True)
    service_majordescrip=models.TextField(blank=True,null=True)
    delay=models.IntegerField(default="150",blank=True,null=True)
    services_images=models.ImageField(upload_to="media/",null=True,blank=True)
    def __str__(self):
        return self.service_heading
    

    
    
    








        