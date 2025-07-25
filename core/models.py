from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class QuoteRequest(models.Model):
    industry = models.CharField(max_length=100)
    num_executives = models.IntegerField()
    num_employees = models.IntegerField()
    avg_employee_pay = models.IntegerField()  
    user_ip = models.GenericIPAddressField()  
    created_at = models.DateTimeField(auto_now_add=True)
    company_email = models.EmailField(default='abc@gmail.com')


    def __str__(self):
        return f"Quote from {self.company_email}"
    
class CalculateModel(models.Model):
    quote = models.OneToOneField(QuoteRequest, on_delete=models.CASCADE)
    annual_tax = models.IntegerField()
    pay_after_tax = models.IntegerField()


