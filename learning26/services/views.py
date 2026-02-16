from django.shortcuts import render, redirect, get_object_or_404
from .models import Service
from .forms import ServiceForm

def service_create(request):
    form = ServiceForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('service_list')
    return render(request, 'services/service_form.html', {'form': form})

def service_list(request):
    services = Service.objects.all()
    return render(request, 'services/service_list.html', {'services': services})

def service_update(request, id):
    service = get_object_or_404(Service, id=id)
    form = ServiceForm(request.POST or None, instance=service)
    if form.is_valid():
        form.save()
        return redirect('service_list')
    return render(request, 'services/service_form.html', {'form': form})

def service_delete(request, id):
    service = get_object_or_404(Service, id=id)
    service.delete()
    return redirect('service_list')
