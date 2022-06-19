from django.shortcuts import render, redirect
from app.forms import MotosForm
from app.models import Motos
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Motos.objects.filter(modelo__icontains=search)
    else:
        data['db'] = Motos.objects.all()

    # PAGINAÇÃO
    #all = Motos.objects.all()
    #paginator = Paginator(all, 2)
    #pages = request.GET.get('page')
    #data['db'] = paginator.get_page(pages)
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = MotosForm()
    return render(request, 'form.html', data)

def create(request):
    form = MotosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = Motos.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Motos.objects.get(pk=pk)
    data['form'] = MotosForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Motos.objects.get(pk=pk)
    form = MotosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    db = Motos.objects.get(pk=pk)
    db.delete()
    return redirect('home')
