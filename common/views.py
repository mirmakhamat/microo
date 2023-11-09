from django.shortcuts import render
from .models import Service, Microphone, Feedback, About, Info

from .forms import CallBackForm, SubscriptionForm


def index(request):
    services = Service.objects.all()
    about = About.objects.first()
    mics = Microphone.objects.all()
    feedback = Feedback.objects.all()
    info = Info.objects.first()

    if request.method == "POST" and "callback" in request.POST:
        callback_form = CallBackForm(data=request.POST)

        if callback_form.is_valid():
            callback_form.save()

    if request.method == "POST" and "subscription" in request.POST:
        subscription_form = SubscriptionForm(data=request.POST)

        if subscription_form.is_valid():
            subscription_form.save()

    return render(request, 'index.html', {
        'services': services,
        'about': about,
        'mics': mics,
        'feedback': feedback,
        'info': info,
    })


def about(request):
    about = About.objects.first() 
    info = Info.objects.first()
    if request.method == "POST" and "subscription" in request.POST:
        subscription_form = SubscriptionForm(data=request.POST)

        if subscription_form.is_valid():
            subscription_form.save()

    return render(request, 'about.html', {'about': about, 'info': info})


def contact(request):
    info = Info.objects.first()
    if request.method == "POST" and "callback" in request.POST:
        callback_form = CallBackForm(data=request.POST)

        if callback_form.is_valid():
            callback_form.save()

    if request.method == "POST" and "subscription" in request.POST:
        subscription_form = SubscriptionForm(data=request.POST)

        if subscription_form.is_valid():
            subscription_form.save()


    return render(request, 'contact.html', {'info': info})


def services(request):
    all_services = Service.objects.all()
    info = Info.objects.first()
    if request.method == "POST" and "subscription" in request.POST:
        subscription_form = SubscriptionForm(data=request.POST)

        if subscription_form.is_valid():
            subscription_form.save()

    return render(request, 'services.html', {'services': all_services, 'info': info})


def shop(request):
    mics = Microphone.objects.all()
    info = Info.objects.first()
    if request.method == "POST" and "subscription" in request.POST:
        subscription_form = SubscriptionForm(data=request.POST)

        if subscription_form.is_valid():
            subscription_form.save()

    return render(request, 'shop.html', {'mics': mics, 'info': info})
