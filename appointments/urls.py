from . import views
from django.urls import path

urlpatterns = [
    path('appointments', views.AppointmentCreate.as_view(),
         name='appointments'),
]
# create ApointmentCreateView, referring to PostDetail url below

#     path('', views.PostList.as_view(), name='home'),
#     path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
#     path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
