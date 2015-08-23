from django import forms

class TrailImageForm(forms.Form):
    image = forms.FileField(label='Select a trail image')
    
class TrailReviewForm(forms.Form):
    review_text = forms.CharField()
