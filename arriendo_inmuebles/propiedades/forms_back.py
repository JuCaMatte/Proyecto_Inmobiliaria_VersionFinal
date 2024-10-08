# forms.py en la aplicación propiedades
from django import forms
from .models import Propiedad, Comuna


# class ContactForm(forms.Form):
#    nombre = forms.CharField(label="Nombre", max_length=100)
#    email = forms.EmailField(label="Correo Electrónico")
#    mensaje = forms.CharField(label="Mensaje", widget=forms.Textarea)


class ContactoForm(forms.Form):
    nombre = forms.CharField(
        label="Nombre",
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    email = forms.EmailField(
        label="Email", widget=forms.EmailInput(attrs={"class": "form-control"})
    )
    mensaje = forms.CharField(
        label="Mensaje", widget=forms.Textarea(attrs={"class": "form-control"})
    )


class PropiedadForm(forms.ModelForm):
    class Meta:
        model = Propiedad
        fields = [
            "nombre",
            "descripcion",
            "tamaño",
            "estacionamientos",
            "habitaciones",
            "baños",
            "direccion",
            "comuna",
            "tipo",
            "precio_arriendo",
        ]
        # comuna = forms.ModelChoiceField(queryset=Comuna.objects.all())
        widgets = {
            "descripcion": forms.Textarea(attrs={"rows": 3}),
            "tamaño": forms.NumberInput(attrs={"step": 0.01}),
            "precio_arriendo": forms.NumberInput(attrs={"step": 0.01}),
            "comuna": forms.Select(),  # Personaliza el widget si es necesario
        }

    # Si necesitas hacer validaciones personalizadas, puedes añadir métodos aquí
    def clean_precio_arriendo(self):
        precio_arriendo = self.cleaned_data.get("precio_arriendo")
        if precio_arriendo <= 0:
            raise forms.ValidationError(
                "El precio de arriendo debe ser mayor que cero."
            )
        return precio_arriendo
