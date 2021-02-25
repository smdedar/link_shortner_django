from django.shortcuts import redirect, render, HttpResponse
from .forms import LinkForm
from .models import Link

import string
import random

#Generate Random String
def random_string():
    # Length of string needed
    N = 5
    # With random.choices()
    res = ''.join(random.choices(string.ascii_lowercase+string.digits, k=N))
    return res

# Long Link Convert to Short Link
def link_shortner(request):
    form = LinkForm(request.POST or None)

    if form.is_valid():
        #Get Value From Input Form
        longLink = form.cleaned_data['longLink']
        #Here Random String Generator
        alias = random_string()
        #Short Link
        shortLink = 'http://127.0.0.1:8000/'+alias
        #Save The Short Link to Database
        b = Link(longLink=longLink, shortLink=alias)
        b.save()
        #return HttpResponse(Sort)
        return render(request,'result.html', {'longLink':longLink, 'shortLink':shortLink})

    return render(request, 'index.html', {'form':form})

#Link Redirect to Orginal Link
def link_redirect(request, alias):
    link = Link.objects.get(shortLink=alias)
    #return HttpResponse(link.longLink)
    return redirect(link.longLink)



