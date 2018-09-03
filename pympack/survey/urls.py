from django.urls import path
from . import views

urlpatterns = [
    path('', views.survey, name='survey'),
    path('results/', views.results, name='results'),
    path('details/', views.details, name='details'),
    path('<pk>/edit/', views.SurveyEditView.as_view(), name='edit'),
    path('<pk>/delete/', views.SurveyDeleteView.as_view(), name='delete'),
    path('thanks/', views.thanks, name='thanks'),
    path('edited/', views.edited, name='edited'),
]
