from django.shortcuts import render
import markdown
import random

from . import util

def convert_md_to_html(title):
    content = util.get_entry(title)
    markdowner = markdown.Markdown()
    if content == None:
        return None
    else:
        return markdowner.convert(content)


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    # content = convert_md_to_html(title)
    content = util.get_entry(title)
    if request.method == "POST":
        content = request.POST['content']
        util.save_entry(title, content)
        return render(request, "encyclopedia/entry.html", {
            "title":   title,
            "content": content
        })
    else:
        if content == None:
            return render(request, "encyclopedia/error.html", {
                "error": "Sorry, the page you are looking for does not exist."
            })
        else:
            return render(request, "encyclopedia/entry.html", {
                "title":   title,
                "content": content
            })
    
def search(request):
    if request.method == "POST":
        entry_search = request.POST['q']
        html_content = convert_md_to_html(entry_search)
        if html_content is not None:
            return render(request, "encyclopedia/entry.html", {
            "title":   entry_search,
            "content": html_content
            })
        else:
            all_entries =  util.list_entries()
            recommendation = []
            for entry in all_entries:
                if entry_search.lower() in entry.lower():
                    recommendation.append(entry)
            return render(request, "encyclopedia/search.html", {
                "recommendation": recommendation,
            })

def new(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        content_convert = convert_md_to_html(title)
        if not title or not content:
            return render(request, "encyclopedia/error.html", {
            "error": "Please provide both a title and content for the new entry."
            })
        all_entries =  util.list_entries()
        for entry in all_entries:
            if title.lower() == entry.lower():
                return render(request, "encyclopedia/error.html", {
                "error": "This title already exists."
                })
            else:
                util.save_entry(title, content)
                return render(request, "encyclopedia/entry.html", {
                    "title":   title,
                    "content": content_convert
                })
    return render(request, "encyclopedia/newpage.html")

def random_entry(request):
    all_entries = util.list_entries()
    title = random.choice(all_entries)
    content = convert_md_to_html(title)
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": content
    })