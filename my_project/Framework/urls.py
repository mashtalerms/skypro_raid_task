from django.urls import path

from .views import FrameworkListView, FrameworkLookupView

urlpatterns = [
    path("", FrameworkListView.as_view()),
    path("<str:language>/", FrameworkLookupView.as_view()),
]
