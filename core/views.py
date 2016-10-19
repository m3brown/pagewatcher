from django.http import HttpResponseRedirect
from django.shortcuts import render
from core.forms import WatchForm
from core.models import Watch

def signup(request):
    if request.method == 'POST':
        form = WatchForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    else:
        form = WatchForm()

    watchlist = Watch.objects.filter(triggered=False)

    return render(request, 'signup.html', {'form': form, 'watchlist': watchlist}) 
