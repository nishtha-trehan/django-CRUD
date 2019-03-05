import re
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Employee
from .forms import EmployeeForm
from django.contrib.auth.decorators import login_required

@login_required()
def abc1(request):
    template='core1/temp1.html'
    q=Employee.objects.all()
    context={
        "a":q
    }
    return render(request,template,context)



@login_required()
def empdetail(request,pk):
        qs=Employee.objects.get(id=pk)
        template="core1/empdetail.html"
        return render(request,template,{"qs":qs})



@login_required()
def empdelete(request,pk):
        qs=Employee.objects.get(id=pk)
        qs.delete()
        return redirect("abc1")



@login_required()       
def emp_form(request):
        form= EmployeeForm(request.POST)
        if form.is_valid():

                abcd=form.save(commit=False)
                abcd.save()
                return redirect('abc1')
        return render(request,'core1/emp_form.html',{'form':form})

@login_required()
def emp_update(request,pk):
        qs= get_object_or_404(Employee, pk=pk)
        if request.method =='POST':

                form= EmployeeForm(request.POST, instance=qs)
                if form.is_valid():
                        abcd=form.save(commit=False)
                        abcd.save()
                        return redirect('abc1')
        else:

                form= EmployeeForm(instance=qs)
        return render(request,'core1/emp_form.html',{'form':form})


