from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.view_news, name='view_news'),
    path('json/', views.get_news_json, name='get_news_json'),
    path('create-news/', views.create_news, name='create_news'),
    path('news/<str:id>/', views.show_news, name='show_news'),
    path('xml/', views.show_xml, name='show_xml'),
    path('json/', views.show_json, name='show_json'),
    path('xml/<str:news_id>/', views.show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:news_id>/', views.show_json_by_id, name='show_json_by_id'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('news/<uuid:id>/edit', views.edit_news, name='edit_news'),
    path('news/<uuid:id>/delete', views.delete_news, name='delete_news'),
    path('create-news-ajax', views.add_news_entry_ajax, name='add_news_entry_ajax'),
    path('proxy-image/', views.proxy_image, name='proxy_image'),
    path('create-flutter/', views.create_news_flutter, name='create_news_flutter'),
]