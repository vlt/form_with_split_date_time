from django import forms

from .models import (
    Universe,
)


class UniverseForm(forms.ModelForm):
    begin = forms.SplitDateTimeField(
    )

    class Meta:
        model = Universe
        fields = [
            "begin",
        ]
