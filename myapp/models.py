from django.db import models
from django.contrib.auth.models import User

class Person(User):
    cName = models.CharField(max_length=20, default='')
    cCellphone = models.CharField(max_length=10, default='')

    class Meta:
        permissions = (
            ("Can_enter_stock6", "Can enter stock6"),
            ("Can_enter_stock6 DB", "Can enter stock6 DB"),
            ("Can_enter_stockPERseg", "Can enter stockPERseg"),
            ("Can_enter_stockPERseg DB", "Can enter stockPERseg DB"),
            ("Can_enter_All", "Can enter All"), 
            ("Can_enter_PaidUsersOnly", "Can enter PaidUsersOnly"),  
            ("Can_enter_AdminOnly", "Can enter AdminOnly"),
            ("Can_enter_VIPsOnly", "Can enter VIPsOnly"),                
            ("Can_enter_stockKn", "Can enter stockKn"),
            ("Can_enter_usersmain_test168", "Can enter usersmain_test168"),

        )
    def __str__(self):
        return self.cName

class NewsUnit(models.Model):
    catego = models.CharField(max_length=10, default='')
    nickname = models.CharField(max_length=20, default='')
    title = models.CharField(max_length=50, default='')
    message = models.TextField(max_length=100, default='')
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.title
    
# Create your models here.
class Stock6Sign202404(models.Model):  
    cStockID = models.CharField(max_length=5, default='')
    cStockName = models.CharField(max_length=5, default='')
    
    
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    
    cSign1 = models.CharField(max_length=10, default='')
    cSign2 = models.CharField(max_length=10, default='')
    cSign3 = models.CharField(max_length=10, default='')
    cSign4 = models.CharField(max_length=10, default='')
    cSign5 = models.CharField(max_length=10, default='')
    cSign6 = models.CharField(max_length=10, default='')
    cAverageScore = models.CharField(max_length=15, default='')  #不能改成FloatField，會發生錯誤
    cLossGain  = models.CharField(max_length=15, default='')  #不能改成FloatField，會發生錯誤

    sCore2403= models.CharField(max_length=10, default='')
    sCore2402= models.CharField(max_length=10, default='')
    sCore2401= models.CharField(max_length=10, default='')
    sCore2312= models.CharField(max_length=10, default='')
    sCore2311= models.CharField(max_length=10, default='')
    sCore2310= models.CharField(max_length=10, default='')
    sCore2309= models.CharField(max_length=10, default='')
    sCore2308= models.CharField(max_length=10, default='')
    sCore2307= models.CharField(max_length=10, default='')
    sCore2306= models.CharField(max_length=10, default='')
    sCore2305= models.CharField(max_length=10, default='')
    sCore2304= models.CharField(max_length=10, default='')







    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID
    
class StockPERseg202404(models.Model):
    cStockID = models.CharField(max_length=5, default='')
    cStockName = models.CharField(max_length=5, default='')



    cRev_Predict = models.CharField(max_length=15, default='') #預估未來營收
    cNet_Predict = models.CharField(max_length=15, default='') #預估未來淨利
    cCapital_stock = models.CharField(max_length=15, default='') #最新股本
    cPredict_EPS = models.CharField(max_length=15, default='') #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15, default='') #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15, default='') #預估未來最低價    
    cLatest_price = models.CharField(max_length=25, default='') #目前最新成交價
    cNew_up_profit = models.CharField(max_length=25, default='') #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=25, default='') #預估未來往下空間    
    
    cRisk_reward = models.FloatField(max_length=20, default='') #預估風險報酬比率  #20201202 可以使用Float


    cPredict_high_price_down30 = models.CharField(max_length=15, default='') #預估未來最高價
    cPredict_low_price_down30 = models.CharField(max_length=15, default='') #預估未來最低價      
    cNew_up_profit_down30 = models.CharField(max_length=25, default='') #預估未來往上空間
    cNew_down_loss_down30 = models.CharField(max_length=25, default='') #預估未來往下空間
    cRisk_reward_down30 = models.FloatField(max_length=20, default='') #預估風險報酬比率  #20201202 可以使用Float


    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID