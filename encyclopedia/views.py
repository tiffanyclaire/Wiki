from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from . import util
from markdown2 import markdown

class NewEntry(forms.Form):
    entry = forms.CharField(label="Entry Title")
    content = forms.CharField(label="Description")

class EditEntry(forms.Form):
    entry = forms.CharField(widget=forms.HiddenInput)
    content = forms.CharField(widget=forms.Textarea)


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):
    content = util.get_entry(title)
    if content == None:
        return render (request, "encyclopedia/error.html")
    
    else: 
        return render (request, "encyclopedia/entry.html", {
       "title": title,
       "content": markdown(content)
})


'''def add(request):
        if request.method == "POST":
            form = NewEntryForm(request.POST)
            if form.is_valid():
                entry = form.cleaned_data["entry"]
                content = form.cleaned_data["content"]
                util.save_entry(entry, content)
                return HttpResponseRedirect(reverse("entry", args=(entry,)))
            else:
                return render (request, "new_entry/html", {
                    "form": form
                })


        return render(request, "encyclopedia/new_entry.html", {
            "form": NewEntryForm()
                  })'''


def add(request):
        if request.method == "POST":
            form = NewEntry(request.POST)
            if form.is_valid():
                entry = form.cleaned_data["entry"]
                content = form.cleaned_data["content"]
                entries = util.list_entries()
                if entry in entries:
                    return render (request, "encyclopedia/error.html")

                else: 
                    util.save_entry(entry, content)
                    return HttpResponseRedirect(reverse("entry", args=(entry,)))


        return render(request, "encyclopedia/new_entry.html", {
            "form": NewEntry()
                  })


def edit(request, title):
    if request.method == "GET" :
        content =  util.get_entry(title)
        form = EditEntry(initial={'content' : content})
        return render(request, "encyclopedia/edit.html", {
            "form" : form,
            "title": title
        })

    else:
        form = EditEntry(request.POST)
        if form.is_valid():
            title = form.cleaned_data ['title']
            content = form.cleaned_data ['content']
            util.save_entry(entry, content)
            return HttpResponseRedirect(reverse("entry", args=(entry,)))

            
