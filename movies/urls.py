from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from movies.views import movie_list, movie_detail


urlpatterns = [
    path('', movie_list, name='movie_list'),
    path('detail/<int:pk>', movie_detail, name='movie_detail')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
