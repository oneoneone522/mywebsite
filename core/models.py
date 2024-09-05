from django.db import models

class WebServices(models.Model):
    serviece_type = models.CharField(max_length=50, blank=False)
    content = models.CharField()
    price = models.IntegerField(blank=False)

class ClientInfo(models.Model):
    CONTACT_CHOICES = [
        ('interested', '有興趣，可以再後續規劃與詳談'),
        ('no_contact', '不用聯繫我，先參考即可'),
    ]
    WEB_TYPE_CHOICES = [
        ('single_page', '一頁式網站'),
        ('template_corporate', '套版形象網站'),
        ('half_template_corporate', '半套版形象網站'),
    ]
    
    contact_choice = models.CharField(max_length=20, choices=CONTACT_CHOICES,  default='no_contact', blank=False)
    web_type = models.CharField(max_length=50, choices=WEB_TYPE_CHOICES, blank=True)
    name = models.CharField(max_length=50, blank=False)
    phone_num = models.CharField(max_length=10, blank=False)
    Line_ID = models.CharField(max_length=50, blank=False)
    email_add = models.EmailField(max_length=254, unique=True, blank=False)
    industry = models.CharField(max_length=100, blank=True)
    ps = models.TextField(max_length=500, blank=True)
