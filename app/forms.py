from django.forms import ModelForm
from app.models import Motos

# Create the form class.
class MotosForm(ModelForm):
    class Meta:
        model = Motos
        fields = ['modelo', 'marca', 'ano']
