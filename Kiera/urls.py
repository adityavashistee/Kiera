"""Kiera URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from rec.views import TSRStatusView, TSRTrainView, TSRAccuracyView, TSRPredictionView

# TODO Test these out
urlpatterns = [
    path(r'rec/status', TSRStatusView.as_view()),
    path(r'rec/train', TSRTrainView.as_view()),
    path(r'rec/accuracy', TSRAccuracyView.as_view()),
    path(r'rec/predict', TSRPredictionView.as_view()),

]
