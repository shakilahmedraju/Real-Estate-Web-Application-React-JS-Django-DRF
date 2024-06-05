from django.urls import path
from .views import ListingListView, ListingRetrieveView, SearchView

urlpatterns = [
    path('', ListingListView.as_view()),
    path('search', SearchView.as_view()),
    path('<slug>', ListingRetrieveView.as_view()),
]
