from django import forms
from .models import Help

class UploadFileForm(forms.Form):
    file = forms.FileField()
    
class HelpForm(forms.ModelForm):
    class Meta:
        model = Help 
        fields = ('name','mail', 'detail')
        widgets = {
            'detail': forms.Textarea(attrs={'rows': 6, 'cols': 40}),
        }