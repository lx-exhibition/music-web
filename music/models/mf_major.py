from .m_major import *
from django.forms import ModelForm

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = '__all__'