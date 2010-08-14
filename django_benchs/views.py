# -*- coding: utf-8 -*-

#from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context, Template
from django.template.loader import get_template
import time
import datetime



def b1(request):
    """Respuesta incremental con response"""
    response = HttpResponse()
    for i in range(100):
        response.write("<p>La hora (%d) en epochs es: %d</p>" % (i, time.time()))
    return response

def b1_1(request):
    """Respuesta optimizada"""
    x = ("<p>La hora (%d) en epochs es: %d</p>" % (i, time.time()) for i in xrange(1,100))
    return HttpResponse("\n".join(x))

def b1_tpl(request):
    """Generamos la plantilla 100 veces"""
    #t = Template("Hora actual: {{num}} {{hora}}" )
    t = get_template("b1_tpl.html")
    response = HttpResponse()
    for i in range(100):
        response.write(t.render(Context({'i':i, 'epoch':time.time()})))
    return response

def b2_tpl(request):
    """prueba con bucle"""
    class Info:
        def __init__(self, num, hora):
            self.i = num
            self.epoch = hora
    x = ( Info(i, time.time()) for i in xrange(1,100))
    return render_to_response('b2_tpl.html', {'objects':x})
    
def b2_1_tpl(request):
    """prueba con bucle"""
    class Info:
        def __init__(self, num, hora):
            self.i = num
            self.epoch = hora
    x = ( Info(i, datetime.datetime.today()) for i in xrange(1,100))
    return render_to_response('b2_filters_tpl.html', {'objects':x})    

def header(request):
	title = "Cabecera menéame"
	globals = {}
	globals['favicon'] = "icon.jpg"
	globals['noindex'] = True
	globals['tags'] = 'test1, test2'
	globals['description'] = 'Pruebas de descripción'
	globals['server_name'] = 'www.meneame.net'
	globals['base_url'] = '/'


	globals['base_static'] = 'http://static.meneame.net'
	globals['js_main'] = 'general01.php'
	globals['security_key'] = 'xxxxxxxxxxxxxxxxxxxxxxx'


	globals['thumbnail'] = 'void.jpg'
	globals['thumbnail_logo'] = 'void.jpg'
	globals['extra_head'] = ''
	globals['extra_js'] = ('void.js', 'void1.js')
	globals['q'] = 'q=aslkdlñak ñlsakd ñlaks&kasjlkadjlajsdljkl'
	globals['lang'] = 'es'
	globals['css_main'] = 'main.css'
	globals['css_color'] = 'main.css'
	
	response = HttpResponse()
	t = get_template("header.html")

	response.write(t.render(Context({'globals': globals, 'title': title})))
	response.write(t.render(Context({'globals': globals, 'title': title})))
	response.write(t.render(Context({'globals': globals, 'title': title})))

	return response
	# render_to_response('header.html', {'globals': globals, 'title': title})

