from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm

def contact_view(request):
    success = False
    error = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            full_message = f"From: {name} <{email}>\n\n{message}"
            try:
                send_mail(
                    subject,
                    full_message,
                    email,
                    ['marco.leon11@uabc.edu.mx'],  # Replace with your email
                    fail_silently=False,
                )
                success = True
            except Exception as e:
                error = True
    else:
        form = ContactForm()
    
    return render(request, 'contact/contact.html', {'form': form, 'success': success, 'error': error})
