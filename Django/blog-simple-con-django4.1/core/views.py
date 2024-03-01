import json
from bs4 import BeautifulSoup

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Factifys, Noticias, Noticias2, Post, Category
from django.contrib.auth.models import User

from .NewsAgent.article_creator import generate_final_article

#Para las API
#from rest_framework.decorators import api_view
#from rest_framework.response import Response

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

# def home(request):

#     if not request.session.get('items_per_page'):
#         request.session['items_per_page'] = 2

#     if request.method == 'GET' and 'items_per_page' in request.GET:
#         request.session['items_per_page'] = int(request.GET['items_per_page'])

#     items_per_page = request.session['items_per_page']

#     posts_page = Paginator(Post.objects.filter(published=True), items_per_page)
#     page = request.GET.get('page')
#     posts = posts_page.get_page(page)
#     aux = 'x' * posts.paginator.num_pages

#     return render(request,'core/home.html', {'posts':posts, 'aux':aux})

# # Detalle del Post
# def post(request, post_id):
#     # post = Post.objects.get(id=post_id)
#     try:
#         post = get_object_or_404(Post, id=post_id)
#         return render(request, 'core/detail.html', {'post':post})
#     except:
#         return render(request, 'core/404.html')

# # Filtrado por Categoría
# def category(request, category_id):
#     try:
#         category = get_object_or_404(Category, id=category_id)
#         return render(request, 'core/category.html', {'category':category})
#     except:
#         return render(request, 'core/404.html')

# # Filtrado por Author
# def author(request, author_id):
#     try:
#         author = get_object_or_404(User, id=author_id)
#         return render(request, 'core/author.html', {'author':author})
#     except:
#         return render(request, 'core/404.html')

# def dates(request, month_id, year_id):

#     meses = {
#         1: 'Enero',
#         2: 'Febrero',
#         3: 'Marzo',
#         4: 'Abril',
#         5: 'Mayo',
#         6: 'Junio',
#         7: 'Julio',
#         8: 'Agosto',
#         9: 'Septiembre',
#         10: 'Octubre',
#         11: 'Noviembre',
#         12: 'Diciembre',
#     }

#     if month_id > 12 or month_id < 1:
#         return render(request, 'core/404.html')

#     posts = Post.objects.filter(published=True, created__month=month_id, created__year=year_id)
#     return render(request, 'core/dates.html', {'posts':posts, 'month':meses[month_id], 'year':year_id})


#NOTICIAS

# def noticias(request):
#     noticias = Noticias.objects.all().order_by('title')
#     return render(request, 'core/noticias.html', {'noticias': noticias})

# def detalle_noticia(request, noticia_id):
#     noticia = get_object_or_404(Noticias, id=noticia_id)
#     return render(request, 'core/detalle_noticia.html', {'noticia': noticia})

def noticias2(request):
    noticias2 = Noticias2.objects.all().order_by('title')
    # print(len(noticias2))
    return render(request, 'core/noticias2.html', {'noticias2': noticias2})

def detalle_noticia2(request, noticia2_id):
    noticia2 = get_object_or_404(Noticias2, id=noticia2_id)
    return render(request, 'core/detalle_noticia2.html', {'noticia2': noticia2})

def factifys(request):
    factifys = Factifys.objects.all().order_by('title')
    return render(request, 'core/factifys.html', {'factifys': factifys})

def detalle_factify(request, factify_id):
    factify = get_object_or_404(Factifys, id=factify_id)
    return render(request, 'core/detalle_factify.html', {'factify': factify})






def buscar_view(request):
    if request.method == 'GET':
        # Creación de un endpoint cuando se usa el buscador de index.html

        user_query = request.GET.get('busqueda')

        #En principio aquí deberíamos llamar a factifys para que cambie de pagina y además deberíamos hacer ejecutar la creación del articulo final en el proceso
        #salida = generate_final_article(user_query)
        redirect('factifys')
        return JsonResponse({'resultado': user_query})
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)




## Esto lo intentamos usar para enseñar el Texto Final por Consola -> No es necesario
    
# def parse_html_to_json(html_content):
#     # Parsear el contenido HTML
#     soup = BeautifulSoup(html_content, 'html.parser')

#     # Aquí deberías identificar la estructura de la página HTML y extraer los datos que necesitas
#     # por ejemplo, puedes encontrar elementos usando métodos como find(), find_all(), etc.

#     # Supongamos que tienes una estructura específica que deseas extraer
#     data = {
#         'titulo': soup.find('h1').text,
#         'parrafos': [p.text for p in soup.find_all('p')],
#         # Agrega más campos según sea necesario
#     }

#     # Convertir los datos extraídos a formato JSON
#     json_data = json.dumps(data, indent=4)
    
#     return json_data