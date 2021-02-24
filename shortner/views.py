from django.shortcuts import render, HttpResponse
from .forms import LinkForm
from .models import Link

# Create your views here.
def index(request):
    form = LinkForm(request.POST or None)

    if form.is_valid():
        Long = form.cleaned_data['longLink']
        Sort = 'http://127.0.0.1:8000/'+'testsort'
        b = Link(longLink=Long, shortLink=Sort)
        b.save()
        return HttpResponse(Sort)
    #return HttpResponse('Test')
    return render(request, 'index.html', {'form':form})