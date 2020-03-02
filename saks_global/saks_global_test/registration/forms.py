from django import forms  
from registration.models import Registration  
class RegistrationForm(forms.ModelForm):  
    class Meta:  
        model = Registration  
        fields = "__all__" 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })    
 