from django import forms
from.models import comment
class commentform(forms.ModelForm):
    class Meta:
     model:comment
     field=['email','name']
    def clean_email(self):
        email=self.cleaned_data.get('email')
        if not  "gmail" in email:
            raise forms.ValidationError("please enter.gov domain")
        return email
