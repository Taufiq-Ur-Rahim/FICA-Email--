from django import forms
from .models import QuoteRequest
class QuickQuoteForm(forms.ModelForm):
    class Meta:
      model = QuoteRequest
      fields = ['industry', 'num_executives', 'num_employees', 'avg_employee_pay']
      widgets = {
          'industry': forms.Select(attrs={'class': 'form-control'}),
          'num_executives': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of Executives'}),
          'num_emplyees': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of Employees'}),
          'avg_employee_pay': forms.Select(attrs={'class': 'form-control'}),
      }
    INDUSTRY_CHOICES = [
                        ('choose', "----Choose----"),
                        ("tech", "Technology"),
                         ("health", "Healthcare"),
                         ("agriculture", "Agriculture"),
                         ("construction", "Construction"),
                         ("edu", "Education"),
                         ("food service", "Food Serrvice"),
                         ("govt","Government"),
                         ]
                         
     
    PAY_RANGE_CHOICES = [ ('0', '-----  Select Pay Range-----'),
                          ('28000',"$15,000-$28,000 Annually"),
                          ("45000", "$28,001-45,000 Annually"),
                          ("55000", '$45,001-$55,000 Annually'),
                          ('70000', '$55,001-$70,000 Annually'),
                          ('80000', '$70,001+ Annually'),
                          ]

    industry = forms.ChoiceField(choices=INDUSTRY_CHOICES, initial="choose")
    num_executives = forms.IntegerField(min_value=0)
    num_employees = forms.IntegerField(min_value=0)
    avg_employee_pay = forms.ChoiceField(choices=PAY_RANGE_CHOICES, initial='0')
    company_email = forms.EmailField()


    