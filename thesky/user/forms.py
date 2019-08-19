from django import forms
from django.contrib.auth.models import User


class Usercreationform(forms.ModelForm):
    username=forms.CharField(max_length=30,label='اسم المستخدم')
    email = forms.EmailField( label='البريد الالكتروني')
    first_name = forms.CharField( label='اسم الاول')
    last_name = forms.CharField( label='اسم الثاني')
    age=forms.CharField(label='لعمر')
    password1 = forms.CharField(min_length=8,widget=forms.PasswordInput() ,label='كلمة المرور')
    password2 = forms.CharField(min_length=8,widget=forms.PasswordInput(),label='تاكيد كلمة المرور')

    class Meta:
        model=User
        fields=('username','email','first_name','last_name','age','password1','password2')
    def clean_password2(self):
        cd=self.cleaned_data
        if cd['password1']!=cd['password2']:
            raise forms.ValidationError('كلمة المرور غير متطابقة')
        return cd['password2']

    def clean_username(self):
        cd = self.cleaned_data
        if User.objects.filter(username=cd['username']).exists():
            raise forms.ValidationError('يوجد مستخدم بهذه الاسم')
        return cd['username']
