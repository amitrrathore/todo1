from django import forms
from .models import todo

class todoform(forms.ModelForm):
    # content=forms.CharField.widget(attrs=) {'class':'form-control'}
    class Meta:
        model = todo
        fields=['content']


class editform(forms.ModelForm):
    # content=forms.CharField.widget(attrs=) {'class':'form-control'}
    class Meta:
        model = todo
        fields='__all__'
        widgets={
            'content':forms.TextInput(attrs={'class':'form-control'}),
            'completed':forms.CheckboxInput(attrs={'class':'mt-4 mb-4'})
        }