from django.forms import ModelForm

from .models import Pet


class PetForm(ModelForm):
    class Meta:
        model = Pet
        fields = [
            'name',
            'group',
            'image'
        ]
        labels = {
            'name': ('Имя'),
            'group': ('Группа'),
        }
        help_texts = {
            'name': ('Имя питомца'),
            'group': ('Группа, к которой будет относиться питомец')
        }
