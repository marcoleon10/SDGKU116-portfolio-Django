from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .forms import ContactForm

def send_email(request):
    if request.method == 'POST':
        
        name = 'Prueba1'
        email = request.POST.get('email', '')
        subject = 'Prueba'
        
        full_message = f"From: {name} <{email}>\n\n"
        try:
            send_mail(
                subject,
                full_message,
                email,
                ['marco.leon11@uabc.edu.mx'],  
                fail_silently=False,
            )
            success = True
            messages.success(request, 'Email sent successfully!')
        except Exception as e:
            error = True
            messages.error(request, 'Failed to send email.')

    return render(request, 'base.html')



