'''
Created on 12 sept. 2018

@author: Marcelo
'''
import datetime

from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render


HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
<meta httpequiv="
contenttype"
content="text/html; charset=utf8">
<meta name="robots" content="NONE,NOARCHIVE">
<title>Hola mundo</title>
<style type="text/css">
html * { padding:0; margin:0; }
body * { padding:10px 20px; }
body * * { padding:0; }
body { font:small sansserif;
}
body>div { borderbottom:
1px solid #ddd; }
h1 { fontweight:
normal; }
#summary { background: #e0ebff; }
</style>
</head>
<body>
<div id="summary">
<h1>¡Hola Mundo!</h1>
</div>
</body></html> """


def hola(request):
    return HttpResponse(HTML)

def fecha_actual(request):
    
    """
    ahora = datetime.datetime.now()
    html = "<html><body><h1>Fecha:</h1><h3>%s<h/3></body></html>" % ahora
    return HttpResponse(html)
    """
    """
    ahora = datetime.datetime.now()
    t = get_template('fecha_actual.html')
    html = t.render(Context({'fecha_actual': ahora}))
    return HttpResponse(html)
    """
    ahora = datetime.datetime.now()
    return render(request, 'fecha_actual.html', {'fecha_actual': ahora})
    
    
def horas_adelante(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt= datetime.datetime.now()+datetime.timedelta(hours=offset)
    """html = "<html><body><h1>En %s hora(s), seran:</h1> <h3>%s</h3></body></html>" % (offset, dt)
    return HttpResponse(html)
    """
    return render(request, 'horas_adelante.html', {'hora_siguiente': dt, 'horas': offset })