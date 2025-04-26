from django.shortcuts import redirect, render

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
                'kiemdegeralde@gmail.com',  # Remplace par ton adresse
                ['kiemdegeralde@gmail.com'],  # Adresse de réception
                fail_silently=False,
            )
            return redirect('index')
    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form})