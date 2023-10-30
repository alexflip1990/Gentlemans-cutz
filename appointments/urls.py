from . import views
from django.urls import path
from appointments.views import AppointmentCreate

urlpatterns = [
    path('add_appointment/', views.add_appointment, name='example-url'),
]
# create ApointmentCreateView, referring to PostDetail url below

#     path('', views.PostList.as_view(), name='home'),
#     path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
#     path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
