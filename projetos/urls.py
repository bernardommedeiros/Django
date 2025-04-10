from django.urls import path
from . import views
urlpatterns = [
    # todo path precisa de um name
    path('', views.index, name = 'index'),
    path('topics', views.topics, name = 'topics'),
    path('topics/<topic_id>/', views.topic, name = 'topic'),
]
