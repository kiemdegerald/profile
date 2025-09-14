from django.shortcuts import redirect, render
from django.contrib import messages
from django.core.mail import send_mail

from .forms import ContactForm

# Create your views here.
def index(request):
    return render(request, 'index.html')



def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            full_message = f"Message de {name} ({email}):\n\n{message}"

            send_mail(
                subject,
                full_message,
                email,  # Email du visiteur (expéditeur réel)
                ['kiemdegeralde@gmail.com'],  # Votre email (récepteur)
                fail_silently=False,
            )
            # Message de succès
            messages.success(request, f'Votre message a été envoyé avec succès à Kiemde Gerald ! Nous vous répondrons dans les plus brefs délais.')
            return redirect('index')
    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form})