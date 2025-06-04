from django.shortcuts import render, redirect, get_object_or_404
from .models import Ficha
from .forms import FichaForm

def criar_ficha(request):
    if request.method == 'POST':
        form = FichaForm(request.POST)
        if form.is_valid():
            ficha = form.save()
            return redirect('ver_ficha', ficha_id=ficha.id)
    else:
        form = FichaForm()
    return render(request, 'core/criar_ficha.html', {'form': form})

def ver_ficha(request, ficha_id):
    ficha = get_object_or_404(Ficha, id=ficha_id)
    return render(request, 'core/ver_ficha.html', {'ficha': ficha})
