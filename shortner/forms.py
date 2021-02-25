from django import forms
from .models import Link

class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        #fields = '__all__'
        fields = {'longLink':forms.URLField(),}
        widgets = {
            'longLink': forms.TextInput(attrs={'class': 'input is-primary'}),
        }
         
