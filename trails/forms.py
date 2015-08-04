from django import forms

class TrailImageForm(forms.Form):
    image = forms.FileField(label='Select a profile Image')