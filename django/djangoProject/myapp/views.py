from django.shortcuts import render, get_object_or_404, redirect
from .models import Case, Client, Area
from .forms import CaseForm, ClientForm


def index(request):
    cases = Case.objects.all()
    return render(request, 'index.html', {'cases': cases})


def create_case(request):
    if request.method == 'POST':
        form = CaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CaseForm()
    return render(request, 'create_case.html', {'form': form})


def case_detail(request, case_id):
    case = get_object_or_404(Case, pk=case_id)
    # Получаем данные из связанных моделей
    area = case.area
    client = case.client_set.first()
    return render(request, 'case_detail.html', {'case': case, 'area': area, 'client': client})


def update_case(request, case_id):
    case = get_object_or_404(Case, pk=case_id)
    if request.method == 'POST':
        form = CaseForm(request.POST, instance=case)
        if form.is_valid():
            form.save()
            return redirect('case_detail', case_id=case.pk)
    else:
        form = CaseForm(instance=case)
    return render(request, 'update_case.html', {'form': form})


def create_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'create_client.html', {'form': form})


def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client_list.html', {'clients': clients})


def client_detail(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    return render(request, 'client_detail.html', {'client': client})


def update_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_detail', client_id=client_id)
    else:
        form = ClientForm(instance=client)
    return render(request, 'update_client.html', {'form': form})


def area_list(request):
    areas = Area.objects.all()
    return render(request, 'area_list.html', {'areas': areas})


def area_detail(request, area_id):
    area = get_object_or_404(Area, pk=area_id)
    return render(request, 'area_detail.html', {'area': area})