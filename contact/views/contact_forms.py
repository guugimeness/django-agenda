from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from contact.forms import ContactForm
from contact.models import Contact

def create(request):
    form_action = reverse('contact:create')
    
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        context = {
            'form': form,
            'form_action': form_action,
        }
        
        if form.is_valid():
            contact = form.save()
            return redirect('contact:update', id=contact.pk)
        
        return render(
            request,
            'contact/create.html',
            context,
        )
        
    context = {
        'form': ContactForm(),
        'form_action': form_action,
    }
    
    return render(
        request,
        'contact/create.html',
        context,
    )

def update(request, id):
    contact = get_object_or_404(Contact, pk=id, show=True)
    form_action = reverse('contact:update', args=(id,))
    
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=contact)
        
        context = {
            'form': form,
            'form_action': form_action,
        }
        
        if form.is_valid():
            contact = form.save()
            return redirect('contact:update', id=contact.pk)
        
        return render(
            request,
            'contact/create.html',
            context,
        )
        
    context = {
        'form': ContactForm(instance=contact),
        'form_action': form_action,
    }
    
    return render(
        request,
        'contact/create.html',
        context,
    )

def delete(request, id):
    contact = get_object_or_404(Contact, pk=id, show=True)
    confirmation = request.POST.get('confirmation', 'no')
    
    if confirmation == 'yes':
        contact.delete()
        return redirect('contact:index')
    
    context = {
        'contact': contact,
        'confirmation': confirmation,  
    }    

    return render(
        request,
        'contact/contact.html',
        context,
    )
