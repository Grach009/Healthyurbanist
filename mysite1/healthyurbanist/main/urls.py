from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.utils.encoding import uri_to_iri

urlpatterns = [
    path('', views.PostView.as_view()),
    path('about/', views.about),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('review/<int:pk>/', views.AddComments.as_view(), name='add_comments'),
    path('<int:pk>/add_likes', views.AddLike.as_view(), name='add_likes'),
    path('<int:pk>/del_likes', views.DelLike.as_view(), name='del_likes'),
    path('tag/<str:tag_name>/', views.tag_posts, name='tag_posts'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
