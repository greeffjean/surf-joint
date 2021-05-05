from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Locations, Members, Products
from .forms import forms
from django.contrib.auth import logout as log_out
from django.conf import settings
from django.http import HttpResponseRedirect
from urllib.parse import urlencode


def get_context():
    context = {
        'members': Members.objects.all(),
        'locations': Locations.objects.all(),
        'products': Products.objects.all()
    }

    return context


def logout(request):
    log_out(request)
    return_to = urlencode({'returnTo': request.build_absolute_uri('/')})
    logout_url = 'https://%s/v2/logout?client_id=%s&%s' % \
                 (settings.SOCIAL_AUTH_AUTH0_DOMAIN, settings.SOCIAL_AUTH_AUTH0_KEY, return_to)
    return HttpResponseRedirect(logout_url)


def index(request):
    user = request.user
    if user.is_authenticated:
        return redirect(home)
    else:
        return render(request, 'index.html')


@login_required
def home(request):
    user = request.user
    auth0user = user.social_auth.get(provider='auth0')
    userdata = {
        'user_id': auth0user.uid,
        'name': user.first_name,
        'picture': auth0user.extra_data['picture'],
        'email': auth0user.extra_data['email'],
    }

    def format_img_url(url):
        new_str = str(url)
        new_url = new_str.replace('report', '..')

        return new_url

    context = get_context()

    members_list = [{
        'name': member.name,
        'surname': member.surname,
        'age': member.age,
        'surf_experience': member.surf_experiece
    } for member in context['members']]

    location_list = [{
        'country': location.country,
        'city': location.city,
        'beach_name': location.beach_name,
        'annual_shark_attacks': location.anual_shark_attacks,
        'required_experience': location.required_experience,
    } for location in context['locations']]

    product_list = [{
        'item': product.item,
        'category': product.category,
        'price': product.price,
        'images': format_img_url(product.images)
    } for product in context['products']]

    return render(request, 'home.html', {
        'members': members_list,
        'locations': location_list,
        'products': product_list,
        'auth0User': auth0user,
        'userdata': userdata
    })


@login_required
def members(request):
    return render(request, 'members.html')


@login_required
def products(request):
    return render(request, 'products.html')


@login_required
def locations(request):
    return render(request, 'locations.html')


@login_required
def add_member(request):
    form = forms.Add_Member()
    return render(request, 'add_member.html', {'form': form})


@login_required
def add_product(request):
    form = forms.Add_Product()
    return render(request, 'add_product.html', {'form': form})


@login_required
def add_location(request):
    form = forms.Add_Location()
    return render(request, 'add_location.html', {'form': form})


@login_required
def save_product(request):
    if request.method == 'POST':
        form = forms.Add_Product(request.POST, request.FILES)
        if form.is_valid():
            item = form.cleaned_data['item']
            category = form.cleaned_data['category']
            price = form.cleaned_data['price']
            used = form.cleaned_data['used']
            warranty = form.cleaned_data['warranty']
            images = form.cleaned_data['images']
            date_posted = form.cleaned_data['date_posted']

            Products.objects.create(
                item=item,
                category=category,
                price=price,
                used=used,
                warranty=warranty,
                images=images,
                date_posted=date_posted
            )

        return render(request, 'products.html')
