#from django.shortcuts import render_to_response
from django.http import HttpResponse
import time

def b1(request):
	response = HttpResponse()
	for i in range(100):
		response.write("<p>La hora (%d) en epochs es: %d</p>" % (i, time.time()))
	return response
		
    #html = "Hora actual: %s (%d)" % (now, offset)
    #return HttpResponse(html)
    #data = {"current_time": now, "offset": offset}
    #return render_to_response("current_time.html", data)

