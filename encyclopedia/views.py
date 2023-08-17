from django.shortcuts import render

from . import util
import markdown


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry_title(request, entry):
    markdown_file_path = f"entries/{entry}.md"  # Update the path to your Markdown files
    
    try:
        with open(markdown_file_path, 'r') as file:
            markdown_content = file.read()
            content_entry = markdown.markdown(markdown_content)
            
        return render(request, "encyclopedia/entry.html", {
            'entry_content': content_entry
        })
    except FileNotFoundError:
        return render(request, "encyclopedia/entry_not_found.html")
