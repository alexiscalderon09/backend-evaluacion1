from django import forms
from .models import Proyecto


class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ["nombre", "descripcion", "url"]
        labels = {
            "nombre": "Nombre del proyecto",
            "descripcion": "Descripción",
            "url": "URL (opcional)",
        }
        help_texts = {
            "descripcion": "Breve resumen del proyecto (qué hace, stack, rol).",
            "url": "Enlace público al repositorio o demo.",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        base = (
            "block w-full rounded-xl border border-gray-300 bg-white px-4 py-2 "
            "shadow-sm focus:outline-none focus:ring-2 focus:ring-gray-900/20 "
            "focus:border-gray-900 placeholder-gray-400"
        )

        for name, field in self.fields.items():
            prev = field.widget.attrs.get("class", "")
            field.widget.attrs["class"] = (prev + " " + base).strip()

        self.fields["nombre"].widget.attrs.update(
            {
                "placeholder": "Ej. WebProduccion",
                "autofocus": "autofocus",
            }
        )
        self.fields["descripcion"].widget.attrs.update(
            {
                "placeholder": "App Vue 3 + API .NET desplegada con Dokploy…",
                "rows": 4,
            }
        )
        self.fields["url"].widget.attrs.update(
            {
                "placeholder": "https://…",
            }
        )
