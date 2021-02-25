from django.shortcuts import redirect, render, HttpResponse
from .forms import LinkForm
from .models import Link

# Create your views here.
def link_shortner(request):
    form = LinkForm(request.POST or None)

    if form.is_valid():
        #Get Value From Input Form
        longLink = form.cleaned_data['longLink']
        #Here Random String Generator
        alias = 'testsort1'
        #Short Link
        shortLink = 'http://127.0.0.1:8000/'+alias
        #Save The Short Link to Database
        b = Link(longLink=longLink, shortLink=alias)
        b.save()
        #return HttpResponse(Sort)
        return render(request,'result.html', {'longLink':longLink, 'shortLink':shortLink})

    return render(request, 'index.html', {'form':form})

def link_redirect(request,slink):
    link = Link.objects.get(shortLink=slink)
    #return HttpResponse(link.longLink)
    return redirect(link.longLink)

