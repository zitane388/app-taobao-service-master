from django.db import models

# Create your models here.

class User_Info(models.Model):
    email = models.CharField(max_length=(320))
    nickname = models.CharField(max_length=(30))
    admin = models.BooleanField()
    admin_email = models.CharField(max_length=(320))
    tax = models.FloatField(default = 1.2)
    goods_max = models.IntegerField(default = 9999999)
    goods_day = models.IntegerField(default = 90)
    three_day = models.IntegerField(default = 3)
    six_mon_s = models.IntegerField(default = 1)
    six_mon_e = models.IntegerField(default = 10)
    review_s = models.IntegerField(default = 0)
    review_e = models.IntegerField(default = 10)
    price_max = models.IntegerField(default = 9999999)
    price_min = models.IntegerField(default = 1)
    problem_product = models.BooleanField(default = True)
    status = models.CharField(max_length=(50),default = '')
    jab = models.BooleanField(default = False)
    margin = models.IntegerField(default = 20)
    
class Prohibition(models.Model):
    email = models.CharField(max_length=(320))
    admin_email = models.CharField(max_length=(320))
    keyword = models.CharField(max_length=(100))
    
    
class Naver_Product(models.Model):
    admin_email = models.CharField(max_length=(320),default = '')
    title = models.CharField(max_length=(300),default = '')
    price = models.IntegerField(default = 0)
    delivery = models.IntegerField(default = 0)
    price_sum_delivery = models.IntegerField(default = 0)
    org_thumbnail = models.CharField(max_length=(2000),default = '')
    sub_thumbnail = models.CharField(max_length=(2000),default = '')
    img_detailed = models.CharField(max_length=(2000),default = '')
    cannel_id = models.CharField(max_length=(300),default = '')
    product_id = models.CharField(max_length=(300),default = '')
    date = models.DateField()
    img_width = models.IntegerField(default = 0)
    img_height = models.IntegerField(default = 0)
    three_day = models.IntegerField(default = 0)
    six_mon = models.IntegerField(default = 0)
    review = models.IntegerField(default = 0)
    review_score = models.CharField(max_length=(100),default = '')
    cannel_product_id = models.CharField(max_length=(300),default = '')


class Sourcing(models.Model):
    org_title = models.CharField(max_length=(300))
    tag = models.CharField(max_length=(300))
    constructor = models.CharField(max_length=(300))
    manager = models.CharField(max_length=(300))
    change_thumbnail = models.CharField(max_length=(2000))
    status = models.IntegerField(default = 0)
    date = models.DateTimeField()
    cannel_id = models.CharField(max_length=(100))
    product_id = models.CharField(max_length=(300),default = '')
    admin_email = models.CharField(max_length=(320))
    item_id = models.CharField(max_length=(300))
    
class Sourcing_Product(models.Model):
    sourcing_id = models.ForeignKey(Sourcing, on_delete=models.CASCADE)
    title = models.CharField(max_length=(300))
    korTitle = models.CharField(max_length=(300))
    margin = models.IntegerField(default = 0)
    weightPrice = models.IntegerField(default = 0)
    weight = models.IntegerField(default = 0)
    memo = models.CharField(max_length=(1000))
    isClothes = models.BooleanField(default = False)	
    isShoes = models.BooleanField(default = False)		
    brand = models.CharField(max_length=(300))
    class Meta:
        db_table = 'sourcing_product'
        
class Sourcing_Option_Category(models.Model):
    sourcing_id = models.ForeignKey(Sourcing, on_delete=models.CASCADE)
    pid = models.CharField(max_length=(300))
    ctg_name = models.CharField(max_length=(300))
    ctg_korTypeName = models.CharField(max_length=(2000))
    vid = models.CharField(max_length=(300))
    name = models.CharField(max_length=(300))
    korTypeName = models.CharField(max_length=(300))
    image = models.CharField(max_length=(2000))
    select = models.BooleanField(default = False)
    class Meta:
        db_table = 'sourcing_option_category'

class Sourcing_Option_Deep_Category(models.Model):
    sourcing_id = models.ForeignKey(Sourcing, on_delete=models.CASCADE)
    ids = models.CharField(max_length=(300))
    sale_price = models.CharField(max_length=(300))
    origin_price = models.CharField(max_length=(300))
    skuid = models.CharField(max_length=(300))
    stock = models.CharField(max_length=(300))
    class Meta:
        db_table = 'sourcing_option_deep_category'    
    
class Main_Images(models.Model):
    sourcing_id = models.ForeignKey(Sourcing, on_delete=models.CASCADE)
    src = models.CharField(max_length=(2000))
    class Meta:
        db_table = 'main_images'        
class Content_Images(models.Model):
   sourcing_id = models.ForeignKey(Sourcing, on_delete=models.CASCADE)
   src = models.CharField(max_length=(2000))
   class Meta:
        db_table = 'content_images'
        
class Product(models.Model):
    #관리자 메일
    email = models.CharField(max_length=(320))
    #마켓 영어 제목
    etitle = models.CharField(max_length=(50))
    #상품번호
    product_num = models.IntegerField()
    
class Problem_Product(models.Model):
    #관리자 메일
    admin_email = models.CharField(max_length=(320))
    #상품번호
    product_num = models.CharField(max_length=(100))    

class Secret_Key(models.Model):
    admin_email = models.CharField(max_length=(320))
    key = models.CharField(max_length=(1000))  
    
    
    