
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[

    path('', views.loginUser, name="index"),
    path('home/', views.home, name="home"),   
    path('register/', views.registerUser, name="registeruser"),
    path('uploadimage/', views.new_image, name="uploadimage"),
    path('viewimage/<int:pk>/', views.viewPhoto, name="viewphoto"),
    path('likes/<int:pk>/', views.likes, name="likes"),
    path('userprofile/<int:pk>/', views.profile_view, name="userprofile"),
    path("followers/<int:pk>/", views.followers, name="followers"),
    path("editpage/<int:pk>/", views.editpage, name="editprofile"), 
    path("searchprofile/", views.search_profile, name="search_profile"),
    path('logout/', views.logoutUser, name="logout")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
