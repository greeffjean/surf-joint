from django.urls import path, include


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('members/', views.members, name='members'),
    path('locations/', views.locations, name='locations'),
    path('products/', views.products, name='products'),
    path('add_member/', views.add_member, name='add_member'),
    path('add_location/', views.add_location, name='add_location'),
    path('add_product/', views.add_product, name='add_product'),
    path('save_product/', views.save_product, name='save_product'),
    path('logout', views.logout),
    path('', include('django.contrib.auth.urls')),
    path('', include('social_django.urls')),
]
