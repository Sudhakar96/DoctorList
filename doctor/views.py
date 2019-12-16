from django.shortcuts import render, redirect
from .forms import DoctorForm
from .models import Doctor

# Create your views here.


def doctor_list(request):
    context = {'doctor_list': Doctor.objects.all()}
    return render(request, "doctor/doctor_list.html", context)


def doctor_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = DoctorForm()
        else:
            doctor = Doctor.objects.get(pk=id)
            form = DoctorForm(instance=doctor)
        return render(request, "doctor/doctor_form.html", {'form': form})
    else:
        if id == 0:
            form = DoctorForm(request.POST)
        else:
            doctor = Doctor.objects.get(pk=id)
            form = DoctorForm(request.POST,instance= doctor)
        if form.is_valid():
            form.save()
        return redirect('/doctor/list')


def doctor_delete(request,id):
    doctor = Doctor.objects.get(pk=id)
    doctor.delete()
    return redirect('/doctor/list')
