from django.shortcuts import render, redirect
from django import forms

from . import util
import markdown
import random
import os


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry_title(request, entry):
    markdown_file_path = f"entries/{entry}.md"  # path to your Markdown files
    
    try:
        with open(markdown_file_path, 'r') as file:
            markdown_content = file.read()
            content_entry = markdown.markdown(markdown_content)
            
        return render(request, "encyclopedia/entry.html", {
            'entry_content': content_entry
        })
    except FileNotFoundError:
        return render(request, "encyclopedia/entry_error.html")
    
def search_entries(request):
    entries = util.list_entries()
    search = request.GET.get("q", "")
    search = str(search)
    search_results = []

    for entry in entries:
        if entry.lower() == search.lower():
            return redirect("entry_title", entry)
        elif search.lower() in entry.lower():
            search_results.append(entry)

    return render(request,"encyclopedia/search_results.html", {"search_results": search_results, "search": search})

def random_entry(request):
    entries = util.list_entries()
    entry = random.choice(entries)
    return redirect("entry_title", entry)

def new_page(request):
    return render(request, "encyclopedia/new_entry.html")

def create_new(request):
    content = request.POST.get("entry_content", "")
    title = request.POST.get("entry_title", "")
    file_title = title.replace(" ", "")
    file_path = (f"entries/{file_title}.md")
 
    if os.path.isfile(file_path):
        return render(request, "encyclopedia/create_entry_error.html")
    
    else:
        file = open(file_path, 'w')
        file.write(f"# {title}\n{content}")
        return redirect("entry_title", file_title)
    

    

    



   
