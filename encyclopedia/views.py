from django.shortcuts import render
import random

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
	query = request.POST.get("query")
	entry = util.get_entry(query)
	if entry != None:
		return page(request, query)
	mathchedEntries = []
	for entry in util.list_entries():
		if query.lower() in entry.lower():
			mathchedEntries.append(entry)
	return render(request, "encyclopedia/search.html", {
		"entries" : mathchedEntries
		})

def createNewPage(request):
	if request.method == "POST":
		title = request.POST.get("title")
		entry = util.get_entry(title)
		if entry != None:
			return render(request, "encyclopedia/error.html", {
				"errorMessage" : "An entry with the title is already exist"
				})
		util.save_entry(title, request.POST.get("content"))
		return page(request, title)
	return render(request, "encyclopedia/create.html")

def editPage(request, title):
	if request.method == "POST":
		util.save_entry(title, request.POST.get("content"))
		return page(request, title)
	return render(request, "encyclopedia/edit.html", {
		"title" : title, "content" : util.get_entry(title)
		})

def randomPage(request):
	return page(request, random.choice(util.list_entries()))

