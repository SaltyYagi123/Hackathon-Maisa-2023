from django.urls import path
from .views import buscar_view, detalle_factify, detalle_noticia2, factifys, index, noticias2 #, detalle_noticia,noticias,  post, category, author, dates #, home



urlpatterns = [
    #PAGINA DE INICIO
    #path('', home, name='home'),

    path('', index, name='index'),

    #PAGINA FILTRADO DE CATEGORIAS
    #path('category/<int:category_id>', category, name='category'),

    #PAGINA FILTRADO DE AUTOR
    #path('author/<int:author_id>', author, name='author'),

    #PAGINA FILTRADO POR FECHA
    #path('dates/<int:month_id>/<int:year_id>', dates, name='dates'),

    #path('post/<int:post_id>', post, name='post'),

    # path('noticias/', noticias, name='noticias'),

    # path('noticia/<int:noticia_id>/', detalle_noticia, name='detalle_noticia'),

    path('noticias2/', noticias2, name='noticias2'),

    path('noticia2/<int:noticia2_id>/', detalle_noticia2, name='detalle_noticia2'),

    path('factifys/', factifys, name='factifys'),

    path('factify/<int:factify_id>/', detalle_factify, name='detalle_factify'),

    # Endpoint para obtener el valor
    path('buscar/', buscar_view, name='buscar'),
]