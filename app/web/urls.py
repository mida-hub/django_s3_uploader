from django.urls import path
from . import views


urlpatterns = [
    path('root', views.RootDocumentCreateView.as_view(), name='s3_root'),
    path('schema', views.SchemaDocumentCreateView.as_view(), name='s3_schema'),
    path('download/<int:pk>/<str:doc>', views.download, name='download'),
]
