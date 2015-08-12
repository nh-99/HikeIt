from django import forms

class TrailImageForm(forms.Form):
    trail = forms.CharField(max_length=256)
    lat = forms.CharField(max_length=50)
    long = forms.CharField(max_length=50)
    image = forms.FileField(label='Select a trail image')
