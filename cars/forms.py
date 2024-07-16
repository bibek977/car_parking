from django import forms
from cars.models import *



class CarsModelForm(forms.ModelForm):
    
    class Meta:
        model = Cars
        fields = [
            'brand',
            'color',
            'liscense_no'
        ]
        labels = {
            "brand":"Car Brand",
            "color":"Car Color",
            "liscense_no":"liscence No"
        }
        help_text = {
            "liscense_no":"Enter Alphanumeric Liscense plate number"
        }
        error_messsages = {
            "liscense_no": {
                "required":"liscense no is required",
            }
        }
        widgets = {
            "liscense_no":forms.TextInput(
                attrs={
                    'placeholder':"NA2PA2325",
                    "class":"form-control"
                }
            ),
            "brand":forms.TextInput(
                attrs={
                    'placeholder':"Toyata",
                    "class":"form-control"
                }
            ),
            "color":forms.TextInput(
                attrs={
                    'placeholder':"black",
                    "class":"form-control"
                }
            ),
        }
    def clean_liscense_no(self):
        liscense_no = self.cleaned_data['liscense_no']
        if Cars.objects.filter(liscense_no=liscense_no).exists():
            raise ValidationError(f"{liscense_no} is already exists")
        return liscense_no

class SpaceModelForm(forms.ModelForm):
    
    class Meta:
        model = Space
        fields = "__all__"

    def clean_space_box(self):
        space_box = self.cleaned_data['space_box']
        if Space.objects.filter(space_box=space_box).exists():
            raise ValidationError(f"{space_box} is already exists")
        return space_box
       

class ParkModelForm(forms.ModelForm):

    class Meta:
        model = ParkSlot
        # fields = "__all__"
        fields = [
            'car',
            'space',
            'date',
        ]
        labels = {
            "car":"Car No",
            "space":"Park spot",
            "date":"Parked Date"
        }
        help_text = {
            "space":"Enter Alphanumeric Liscense plate number"
        }
        error_messsages = {
            "space": {
                "required":"space no is required"
            }
        }
        widgets = {
            "space":forms.Select(
                attrs={
                    "class":"form-control"
                }
            ),
            "car":forms.Select(
                attrs={
                    "class":"form-control"
                }
            ),
        }

    def clean(self):
        cleaned_data = super().clean()
        car = cleaned_data.get("car")
        space = cleaned_data.get("space")
        c = Cars.objects.get(liscense_no=car)
        s = Space.objects.get(space_box=space)
        if c.status:
            raise ValidationError(f"{c} is already researved")
        if s.status:
            raise ValidationError(f"{s} is already occupied")
        return cleaned_data