from django.shortcuts import render
from formapp.forms import StudentForm
def index(request):
# Create your views here.
    f=StudentForm()
    if request.method=='POST':
        f=StudentForm(request.POST)
        if f.is_valid():
            sname=f.cleaned_data['sname']
            sid=f.cleaned_data['sid']
            sage=f.cleaned_data['sage']
            sphone=f.cleaned_data['sphone']
            d={'sname':sname,'sid':sid,'sage':sage,'sphone':sphone}
            return render(request,'htmlpages/output.html',d)
    d={'form':f}
    return render(request,'htmlpages/input.html',d)