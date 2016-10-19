from django.forms import ModelForm
from core.models import Watch

class WatchForm(ModelForm):
    class Meta:
        model = Watch
        fields = ['page', 'email']
