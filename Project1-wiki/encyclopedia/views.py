from django.shortcuts import render
from . import util
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import forms
# Import Markdown from "pip3 install markdown2"
from markdown2 import Markdown

# For random page choose random entries
import secrets

# Form create new entry page
class NewEntryForm(forms.Form):
    title = forms.CharField(
        label="Entry Title",
        widget=forms.TextInput(attrs={
            'class': 'form-control col-md-10 col-lg-10',
            'placeholder': 'Enter Title'
        })
    )
    content = forms.CharField(
        label="Entry Content",
        widget=forms.Textarea(attrs={
            'class': 'form-control col-md-10 col-lg-10', 'rows': 10, 
            'placeholder': "Enter Page Content Markdown"
        })
    )
    edit = forms.BooleanField(
        widget=forms.HiddenInput(), 
        initial= False, 
        required= False
    )


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, entry):
    markdowner = Markdown()
    entry_page = util.get_entry(entry)
    if  entry_page == None:
        return render(request, "encyclopedia/not_found.html", {
            "entry_title": entry
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "entry_title": entry,
            "entry": markdowner.convert(entry_page),
        })


def search(request):
    query = request.GET.get('q', '')
    if util.get_entry(query) != None:
        return HttpResponseRedirect(reverse("entry", kwargs={'entry': query}))
    else:
        search_list = []
        for entry in util.list_entries():
            if query.upper() in entry.upper():
                search_list.append(entry)
        if len(search_list) == 0:
            empty_list = True
        else:
            empty_list = False
        return render(request, 'encyclopedia/index.html', {
                "entries": search_list,
                "search": True,
                "query": query,
                "empty_list": empty_list
        })


def new_entry(request):
    if request.method == 'POST':
        form = NewEntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            if util.get_entry(title) == None or form.cleaned_data['edit'] == True:
                util.save_entry(title, content)
                return HttpResponseRedirect(reverse('entry', kwargs={'entry': title}))
            else:
                return render(request, "encyclopedia/new_entry.html", {
                    'form': form, 
                    'existing': True, 
                    'entry': title
                })
    else:
        return render(request, "encyclopedia/new_entry.html", {
            "form": NewEntryForm(),
            "existing": False,
        })


def edit(request, entry):
    entry_page = util.get_entry(entry)
    if entry_page == None:
        return render(request, "encyclopedia/not_found.html", {
            "entry_title": entry
        })
    else:
        form = NewEntryForm()
        form.fields["title"].initial = entry
        form.fields["title"].widget = forms.HiddenInput()
        form.fields["content"].initial = entry_page
        form.fields["edit"].initial = True
        return render(request, "encyclopedia/new_entry.html", {
            "form": form,
            "edit": form.fields["edit"].initial,
            "entry_title": form.fields["title"].initial,
        })


def random_page(request):
    entries = util.list_entries()
    random_entry = secrets.choice(entries)
    return HttpResponseRedirect(reverse("entry", kwargs={'entry': random_entry}))