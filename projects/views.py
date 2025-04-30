from django.shortcuts import render, redirect
from datetime import datetime
from django.http import FileResponse
from django.conf import settings
from django.contrib import messages
import os



def descargar_cv(request):
    filepath = os.path.join(settings.STATIC_ROOT, 'cv/LeandroEmanuelVarela-formatoharvard.pdf')
    return FileResponse(open(filepath, 'rb'), as_attachment=True, filename='LeandroEmanuelVarela-formatoharvard.pdf')


def home(request):
    return render(request, 'projects/home.html', {'year': datetime.now().year})

def projects_view(request):
    return render(request, 'projects/projects.html', {'year': datetime.now().year})

def about(request):
    return render(request, 'projects/about.html', {'year': datetime.now().year})

def skills(request):
    return render(request, 'projects/skills.html', {'year': datetime.now().year})

def experience(request):
    return render(request, 'projects/experience.html', {'year': datetime.now().year})

def contact(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        mensaje = request.POST.get('mensaje')

        # Aquí podrías guardar los datos o enviarlos por correo
        print(f"Mensaje recibido de {nombre} ({correo}): {mensaje}")

        messages.success(request, '¡Gracias por tu mensaje! Te responderé pronto.')
        return redirect('contact')  # Redirige para limpiar el formulario
    return render(request, 'projects/contact.html', {'year': datetime.now().year})