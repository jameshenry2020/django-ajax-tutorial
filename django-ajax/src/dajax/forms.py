from django import forms
from .models import HotelRoom


class  RoomForm(forms.ModelForm):
    class  Meta:
        model = HotelRoom
        fields =  '__all__'