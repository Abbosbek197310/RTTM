from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext
from django.shortcuts import render
from django.conf.urls import handler404
from django.shortcuts import render


# Create your views here.
def custom_404(request, exception):
    return render(request, '404.html', status=404)

handler404 = custom_404



def Index3(request):
    context={
        'adti':Adti.objects.all(),
        'raxbarlar':Xodimlari.objects.all(),
        'servis':Servis.objects.all(),
        'foto':Foto.objects.all(),
        'kompyuter':Kompyuter.objects.all(),
        'prorektor':Prorektor.objects.all(),
        'atm_raxbar':ATM_raxbar.objects.all(),
        'rttm_malumot':Rttm_malumot.objects.all()
       
    }
    return render(request,'index-3.html',context )

def Index1(request):

    return render(request,'index-1.html' )






