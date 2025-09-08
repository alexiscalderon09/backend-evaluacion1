from django.shortcuts import render
from .utils import calcular_anios_experiencia, top_skills
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Proyecto
from .forms import ProyectoForm


def landing(request):
    perfil = {
        "nombre": "Alexis José Calderón Díaz",
        "rol": "Desarrollador de software (ecosistema Microsoft) · Backend .NET · Frontend Vue/TS",
        "resumen": (
            "Desarrollador en Santiago de Chile. Experiencia construyendo APIs en .NET, "
            "frontends con Vue 3/TypeScript y despliegues en Docker/Dokploy. Interesado en "
            "arquitecturas limpias, logging, y buenas prácticas CI/CD."
        ),
        "ubicacion": "Santiago, Chile",
        "contacto": {
            "email": "alexisjosecalderondiaz@gmail.com",
            "telefono": "+56 9 8550 0554",
            "github": "https://github.com/Alexis-Calderon",
            "linkedin": "https://www.linkedin.com/in/alexis-jose-calderon-diaz/",
        },
        "habilidades": [
            "C# / .NET",
            "ASP.NET Core",
            "Entity Framework",
            "SQL avanzado",
            "Vue 3 / TypeScript",
            "Docker / Dokploy",
            "Nginx",
            "PostgreSQL",
            "REST APIs",
            "Tests y CI/CD",
        ],
        "proyectos": [
            {
                "nombre": "WebProduccion",
                "descripcion": "Frontend Vue 3 + API .NET; despliegue con Dokploy, Nginx y R2 (S3).",
            },
            {
                "nombre": "API Reportes RDLC (.NET)",
                "descripcion": "Endpoint que genera PDF vía RDLC; exploración SSRS/Jasper/BIRT.",
            },
        ],
        "experiencia": [
            {
                "empresa": "Freelance",
                "cargo": "Desarrollador Backend .NET",
                "detalle": "APIs en .NET 7/8/9, EF Core, autenticación JWT, despliegues Docker.",
            },
        ],
        "educacion": [
            {
                "institucion": "INACAP",
                "titulo": "Analista Programador",
                "periodo": "2024 — 2025",
            }
        ],
    }

    anios = calcular_anios_experiencia(2020)
    perfil["experiencia_anios"] = anios
    perfil["habilidades_top"] = top_skills(perfil["habilidades"], 6)

    return render(
        request,
        "landing.html",
        {
            "perfil": perfil,
        },
    )


class ProyectoList(ListView):
    model = Proyecto
    template_name = "proyectos/list.html"
    context_object_name = "proyectos"


class ProyectoCreate(CreateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = "proyectos/form.html"
    success_url = reverse_lazy("proyecto_list")


class ProyectoUpdate(UpdateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = "proyectos/form.html"
    success_url = reverse_lazy("proyecto_list")


class ProyectoDelete(DeleteView):
    model = Proyecto
    template_name = "proyectos/confirm_delete.html"
    success_url = reverse_lazy("proyecto_list")
