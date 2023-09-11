from django.urls import path


from . import views


app_name = 'pets'

urlpatterns = [
    path('pets/<int:pet_id>/delete/', views.pet_delete, name='pet_delete'),
    path('', views.index, name='index'),
    path('group/<slug:slug>/', views.group_pets, name='group_list'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('pets/<int:pet_id>/', views.pet_detail, name='pet_detail'),
    path('create/', views.pet_create, name='pet_create'),
    path('pets/<int:pet_id>/edit/', views.pet_edit, name='pet_edit'),
    path(
        'pets/<int:pet_id>/comment/',
        views.add_comment,
        name='add_comment'),
    path('comment/<int:comment_id>/comment_edit/',
         views.comment_edit,
         name='comment_edit'),
    path('pets/<int:pet_id>/comment/<int:comment_id>/delete/',
         views.comment_delete,
         name='comment_delete'),
]
