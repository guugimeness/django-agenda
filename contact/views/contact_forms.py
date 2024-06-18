from django.shortcuts import render, redirect
from contact.forms import ContactForm

def create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        context = {
            'form': form
        }
        
        if form.is_valid():
            contact = form.save()
            return redirect('contact:detail', contact.id)
        
        return render(
            request,
            'contact/create.html',
            context,
        )
        
    context = {
        'form': ContactForm()
    }
    
    return render(
        request,
        'contact/create.html',
        context,
    )