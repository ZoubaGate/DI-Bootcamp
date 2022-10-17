from django.shortcuts import render
from .forms import GifForm
# Create your views here.

def myGif(request):
    context = {}
    
    if request.method == 'POST':
        form = GifForm(request.POST)
        if form.is_valid():
            #get the value from the fields
            uploader_name = form['uploader_name']
            title = form['title']
            url = form['title']
            Category = form['Category']
            # render to a the same url, but with new data:
            context['gifInfo'] = [uploader_name,title,url,Category]
    else:
        context['form'] = GifForm()   

    return render(request,'gifs/addNewGif.html',context)