from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Articulo
import json

@login_required
def like_section(request, section):
    if request.method == 'POST':
        if section in ['cielo', 'deporte', 'fotografia']:
            try:
                articulo = Articulo.objects.get(seccion=section)
                
                data = json.loads(request.body)            
                action = data.get('action')
                
                if 'like' == action:
                    articulo.likes += 1
                elif 'dislike'  == action:
                    articulo.dislikes += 1
                articulo.save()
                
                return HttpResponse(json.dumps({'likes': articulo.likes, 'dislikes': articulo.dislikes}), content_type='application/json')
            except Articulo.DoesNotExist:
                return HttpResponse(json.dumps({'error': f'Article with section {section} does not exist'}), status=404)
            except Exception as e:
                return HttpResponse(json.dumps({'error': f'An error occurred: {str(e)}'}), status=500)
    return HttpResponse(status=400)

@login_required
def dislike_section(request, section):
    if request.method == 'POST':
        if section in ['cielo', 'deporte', 'fotografia']:
            try:
                articulo = Articulo.objects.get(seccion=section)
                
                data = json.loads(request.body)            
                action = data.get('action')
                
                if 'like' == action:
                    articulo.likes += 1
                elif 'dislike'  == action:
                    articulo.dislikes += 1
                articulo.save()
                
                return HttpResponse(json.dumps({'likes': articulo.likes, 'dislikes': articulo.dislikes}), content_type='application/json')
            except Articulo.DoesNotExist:
                return HttpResponse(json.dumps({'error': f'Article with section {section} does not exist'}), status=404)
            except Exception as e:
                return HttpResponse(json.dumps({'error': f'An error occurred: {str(e)}'}), status=500)
    return HttpResponse(status=400)
