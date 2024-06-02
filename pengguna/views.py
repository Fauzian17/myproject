from django.shortcuts import render,redirect,get_object_or_404

from pengguna.models import Formulir
from pengguna.forms import FormulirForm


# Create your views here.

def home(request):
    template = "index.html"
    context = {
        'title': 'Home',
    }
    return render(request, template, context)

def formulir_list(request):
    template = "admin.html"
    formulir_list = Formulir.objects.all()
    print(formulir_list)
    context = {
        'title': 'Form Pendaftaran',
        'formulir_list': formulir_list
    }
    return render(request, template, context)

def akun_pengguna(request):
    template = "akun_pengguna.html"
    context = {
        'title': 'Akun Pengguna',
    }
    return render(request, template, context)

    
def formulir_detail(request, pk):
    formulir = get_object_or_404(Formulir, pk=pk)
    context = {
        'formulir': formulir,
        'title': 'Detail Formulir',
    }
    return render(request, 'dashboard/snippets/formulir_detail.html', context)


def create_formulir(request):
    if request.method == "POST":
        form = FormulirForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('formulir_detail')  # Ganti dengan URL halaman sukses Anda
    else:
        form = FormulirForm()

    context={
        'form': form, 
        'title': 'Formulir Pendaftaran'
        }

    return render(request,'dashboard/snippets/formulir.html', context)

def formulir_list(request):
    formulirs = Formulir.objects.all()
    context = {
        'formulirs': formulirs,
        'title': 'Daftar Formulir',
    }
    return render(request, 'dashboard/snippets/formulir_list.html', context)


def some_view(request):
    context = {
        'formulir_list': Formulir.objects.all(),  # Misalnya Anda memiliki formulir list di sini
        'user': request.user
    }
    return render(request, 'content/admin.html', context)



