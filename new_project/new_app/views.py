from django.shortcuts import render
from .models import Works, Trideshniki


# Create your views here.
def show_works(request):
    works = {'works': Works.objects.all()}

    return render(request, "index.html", context=works)


def show_trideshniki(request):
    trideshniki = {'trideshniki': Trideshniki.objects.all()}

    return render(request, "index.html", context=trideshniki)
