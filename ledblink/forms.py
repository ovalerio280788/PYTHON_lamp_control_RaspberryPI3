from django import forms

from ledblink.models import ControlLamp


class UserLedBlinkForm(forms.ModelForm):

    class Meta:
        model = ControlLamp
        fields = ('state',)
