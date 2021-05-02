from django.shortcuts import render
from .models import Locations, Members, Products
from .forms import forms


def get_context():
    context = {
        'members': Members.objects.all(),
        'locations': Locations.objects.all(),
        'products': Products.objects.all()
    }

    return context

def home(request):
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
        'anual_shark_attacks': location.anual_shark_attacks,
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
        'products': product_list
    })


def members(request):
    return render(request, 'members.html')


def products(request):
    return render(request, 'products.html')


def locations(request):
    return render(request, 'locations.html')


def add_member(request):
    form = forms.Add_Member()
    return render(request, 'add_member.html', {'form': form})


def add_product(request):
    form = forms.Add_Product()
    return render(request, 'add_product.html', {'form': form})


def add_location(request):
    form = forms.Add_Location()
    return render(request, 'add_location.html', {'form': form})


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
