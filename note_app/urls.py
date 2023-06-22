from django.urls import path,include
from . import views
#path(url , function , name) you can execute this function if you get this url.
#url に対応するviews.py の関数を設定する
app_name = 'note_app'
urlpatterns = [
    path('',views.index,name='index'),
    path('post/',views.post,name='post'),
    path('create/',views.create,name='create'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('delete/<int:post_id>/', views.delete, name='delete'),
    path('logout/', views.logout_view, name='logout'),
]