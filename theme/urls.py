from django.urls import path
from django.views.generic.base import RedirectView
from . import views

app_name = 'theme'

urlpatterns = [
    path('favicon.ico/', RedirectView.as_view(url='/static/img/logo.png', permanent=True), name='favicon'),
    path('', views.index, name='index'),

    path('faq/', views.faq, name='faq'),
    path('info1/', views.info1, name='info1'),
    path('info2/', views.info2, name='info2'),
    path('info3/', views.info3, name='info3'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),

    path('blog/howto-create-steam-account/', views.htcsa, name='htcsa'),

    
]