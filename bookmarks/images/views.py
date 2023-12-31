from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm

# Create your views here.

@login_required
def image_create(request):
    if request.method == 'POST':
        #form is sent
        form = ImageCreateForm(data = request.POST)
        if form.is_valid():
            # form data is valid
            cd = form.cleaned_data
            new_item = form.save(commit=False)
            
            #assign current User to the item
            new_item.user = request.user
            new_item.save()
            messages.success(request, "Image created successfully")
            # redirect to new created item detail view
            
            return redirect(new_item.get_absolute_url())
    else:
        # build form with data provided by the bookmark
        
        form = ImageCreateForm(data = request.GET)
        
    return render(request, 'images/image_create.html',
                  {'section':'images',
                   'form': form})