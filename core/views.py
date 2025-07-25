from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import QuickQuoteForm
from .models import QuoteRequest, CalculateModel

def home(request):
    if request.method == "POST":
        form = QuickQuoteForm(request.POST)
        if form.is_valid():            
            quote = QuoteRequest(
                industry=form.cleaned_data["industry"],
                num_executives=form.cleaned_data["num_executives"],
                num_employees=form.cleaned_data["num_employees"],
                avg_employee_pay=form.cleaned_data["avg_employee_pay"],
                company_email = form.cleaned_data['company_email'],
                user_ip=request.META.get("REMOTE_ADDR"),  
            )
            quote.save()
            return redirect("core:home")
    else:
        form = QuickQuoteForm()
    return render(request, "home.html", {"form": form}) 


def AnnualTaxCalculation(request):
    quote = QuoteRequest.objects.latest('id')  # or .get(id=...) as needed
    an = quote.avg_employee_pay

    if 0 < an < 25000:
        annual_tax = an * 0.075
    elif 25001 < an < 48000:
        annual_tax = an * 0.1304
    else:
        annual_tax = an * 0.17

    pay_after_tax = an - annual_tax

    return render(request, 'your_template.html', {
        'annual_tax': annual_tax,
        'pay_after_tax': pay_after_tax,
        'an': an
    })






# def AnnualTaxCalculation(request):
#     try:
#         quote = QuoteRequest.objects.latest('id') 
#         an = float(quote.avg_employee_pay)  
#     except QuoteRequest.DoesNotExist:
#         return render(request, 'data.html', {'error': 'No data found.'})
#     except ValueError:
#         return render(request, 'data.html', {'error': 'Invalid number format in avg_employee_pay.'})
    
#     if an > 0 and an < 25000:
#         annual_tax = an * 0.075
#     elif an < 48000:
#         annual_tax = an * 0.1304
#     elif an < 55000:
#         annual_tax = an * 0.1538
#     elif an < 70000:
#         annual_tax = an * 0.1897
#     else:
#         annual_tax = an * 0.2188

#     pay_after_tax = an - annual_tax

#     context = {
#         'annual_tax': round(annual_tax, 2),
#         'pay_after_tax': round(pay_after_tax, 2),
#         'avg_employee_pay': an
#     }

#     return render(request, 'data.html', context)
    
    