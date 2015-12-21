import django.forms
class ImageUploadForm(forms.Form):
    iamge = forms.ImageField()