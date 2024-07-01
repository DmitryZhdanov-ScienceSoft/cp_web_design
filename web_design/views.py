from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import WebsiteBriefForm


def health_check(request):
    return render(request, 'health_check.html')

def website_brief(request):
    if request.method == 'POST':
        form = WebsiteBriefForm(request.POST)
        if form.is_valid():
            # Обработка данных формы
            # Например, отправка email или сохранение в базу данных
            send_email_with_form_data(form.cleaned_data)
            return redirect('thank_you')  # Перенаправление на страницу благодарности
    else:
        form = WebsiteBriefForm()

    return render(request, 'website_brief.html', {'form': form})


def send_email_with_form_data(data):
    subject = 'Новый бриф на разработку сайта'
    message = '\n'.join([f'{key}: {value}' for key, value in data.items()])
    from_email = 'signmark@craftpodium.com'
    recipient_list = ['signmar@gmail.com']

    send_mail(subject, message, from_email, recipient_list)


def thank_you(request):
    return render(request, 'thank_you.html')
