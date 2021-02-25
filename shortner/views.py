from django.shortcuts import redirect, render, HttpResponse
from .forms import LinkForm
from .models import Link

# Create your views here.
def index(request):
    form = LinkForm(request.POST or None)

    if form.is_valid():
        longLink = form.cleaned_data['longLink']
        alias = 'testsort1'
        shortLink = 'http://127.0.0.1:8000/'+alias
        b = Link(longLink=longLink, shortLink=alias)
        b.save()
        #return HttpResponse(Sort)
        return render(request,'result.html', {'longLink':longLink, 'shortLink':shortLink})

    return render(request, 'index.html', {'form':form})

def link_destination(request,slink):
    link = Link.objects.get(shortLink=slink)
    #return HttpResponse(link.longLink)
    return redirect(link.longLink)

