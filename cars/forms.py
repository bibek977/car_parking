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
                "required":"liscense no is required"
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

class SpaceModelForm(forms.ModelForm):
    
    class Meta:
        model = Space
        fields = "__all__"
       

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
                    # 'placeholder':"NA2PA2325",
                    "class":"form-control"
                }
            ),
            "car":forms.Select(
                attrs={
                    # 'placeholder':"Toyata",
                    "class":"form-control"
                }
            ),
            # "date":forms.SelectDateWidget(
            #     attrs={
            #         # 'placeholder':"black",
            #         "class":"form-control"
            #     }
            # ),
        }