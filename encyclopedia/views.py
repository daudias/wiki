from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def page(request, title):
	entry = util.get_entry(title)
	if entry != None:
		return render(request, "encyclopedia/page.html", {
		"title" : title, "content" : entry 
		})
	return render(request, "encyclopedia/error.html", {
		"errorMessage" : "No such entry"
		})

def search(request):
	if request.method == "POST":
		query = request.POST.get("query")
		entry = util.get_entry(query)
		if entry != None:
			return page(request, query)
		else:
			mathchedEntries = []
			for entry in util.list_entries():
				if query.lower() in entry.lower():
					mathchedEntries.append(entry)
			return render(request, "encyclopedia/search.html", {
				"entries" : mathchedEntries
				})
	return render(request, "encyclopedia/error.html", {
		"errorMessage" : "Not allowed (Access must be by POST method)"
		})

