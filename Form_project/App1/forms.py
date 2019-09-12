from django import forms

#create your forms here

class empform(forms.Form):
    firstname=forms.CharField()
    lastname=forms.CharField()
    contact=forms.IntegerField()
    email=forms.EmailField()
    location=forms.CharField()
