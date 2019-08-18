from django.shortcuts import render

from blog.models import BlogPost

from .forms import ContactForm



def home_page(request):
    my_title = 'Welcome to Bhanu\'s Python blog'

    qs= BlogPost.objects.all()[:5]
    context = {'object_list': qs, 'title': my_title}

    return render(request,"home.html", context)


def contact_page(request):
    title = 'Contact us'

    form = ContactForm(request.POST or None)
    if form.is_valid():
        form = ContactForm()
    context = {'form': form,'title':title}
    print(request.POST)
    return render(request,"form.html", context)


def about_page(request):
    my_title = 'My about Page'
    context = {'title': my_title}
    return render(request,"about.html", context)


def home_view1(request):
    return render(request,"home1.html", {})