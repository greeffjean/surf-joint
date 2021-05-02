from django import forms


class Add_Member(forms.Form):
    name = forms.CharField(max_length=60)
    surname = forms.CharField(max_length=60)
    age = forms.IntegerField()
    address = forms.CharField(max_length=100)
    surf_experiece = forms.CharField(max_length=30)
    date_joined = forms.DateTimeField()

class Add_Location(forms.Form):
    country = forms.CharField(max_length=60)
    city = forms.CharField(max_length=60)
    beach_name = forms.CharField(max_length=60)
    ocean = forms.CharField(max_length=60)
    nearest_airport = forms.CharField(max_length=60)
    shark_activity = forms.CharField(max_length=60)
    anual_shark_attacks = forms.IntegerField()
    required_experience = forms.CharField(max_length=60)

class Add_Product(forms.Form):
    item = forms.CharField(max_length=60)
    category = forms.CharField(max_length=60)
    price = forms.CharField(max_length=60)
    used = forms.CharField(max_length=60)
    warranty = forms.CharField(max_length=60)
    images = forms.FileField(allow_empty_file=True)
    date_posted = forms.DateTimeField(widget=forms.SelectDateWidget())

        
    