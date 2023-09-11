from django.shortcuts import render
from .models import Contact, Review, Slider, OurService, AboutUs, WhyChooseUs

def Homepage(request):
    contact = Contact.objects.first()
    review = Review.objects.all()
    slider = Slider.objects.all()
    our_service = OurService.objects.all()
    aboutus = AboutUs.objects.first()
    whychoose = WhyChooseUs.objects.all()
    context = {
        'slider':slider,
        'contact':contact,
        'review':review,
        'our_service':our_service,
        'aboutus':aboutus,
        'whychoose':whychoose,
    }
    return render(request, 'home.html', context)


