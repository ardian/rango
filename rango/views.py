from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from rango.models import Category

def index(request):
    # Obtain the context from the HTTP request.
    context = RequestContext(request)

    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}

    # Render the response and send it back!
    return render_to_response('rango/index.html', context_dict, context)

def about(request):
	# return HttpResponse("Rango Says: Here is the about page.") # FIRST EXAMPLE
	context = RequestContext(request)
	context_dict = {'boldmessage': 4 + 4}
	return render_to_response('rango/about.html', context_dict, context)