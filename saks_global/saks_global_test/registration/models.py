from django.db import models

class Registration(models.Model):
    full_name = models.CharField(max_length=255, blank = False, null = False)
    email = models.EmailField()
    username = models.CharField(max_length=255, blank = False, null = False)    
    phone_number = models.CharField(max_length=20, blank = True, null = False)
    present_address = models.CharField(max_length=350, blank = True, null = False)
    permanent_address = models.CharField(max_length=350, blank = True, null = False)
    nid_number = models.CharField(max_length=12, blank = True, null = False)

    class Meta:  
      db_table = "registration"  
