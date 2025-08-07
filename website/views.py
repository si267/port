from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail 


def index(request):
    return render(request, 'website/index.html')
def base(request):
    return render(request,'website/base.html')
def about(request):
    skills = ['HTML', 'CSS', 'JavaScript', 'Python', 'Django', 'Git', 'SQL']
    return render(request, 'website/about.html', {'skills': skills})
def project(request):
    return render(request,'website/project.html')
def contact(request):
    return render(request, 'website/contact.html')


def experience_view(request):
    return render(request, 'website/experience.html')





def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save to DB
        Contact.objects.create(name=name, email=email, message=message)

        # ✅ Show success message
        messages.success(request, 'Your message was sent successfully!')

        return redirect('contact')  # stays on same page

    return render(request, 'website/contact.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        Contact.objects.create(name=name, email=email, message=message)

        # ✅ Send email
        send_mail(
            subject=f"New Contact Message from {name}",
            message=f"Name: {name}\nEmail: {email}\nMessage:\n{message}",
            from_email='sivasankari1456@gmail.com',
            recipient_list=['sivasankari1456@gmail.com'],  # you can add more emails
            fail_silently=False,
        )

         # ✅ Thank-you email to the user
        send_mail(
            subject='Thank you for contacting me!',
            message=f"Hi {name},\n\nThank you for reaching out to me. I have received your message and will get back to you as soon as possible.\n\nWarm regards,\nSiva Sankari",
            from_email='sivasankari1456@gmail.com',
            recipient_list=[email],
            fail_silently=False,
        )

        messages.success(request, 'Your message was sent successfully!')
        return redirect('contact')

    return render(request, 'website/contact.html')



