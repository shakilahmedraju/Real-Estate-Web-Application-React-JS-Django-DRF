from django.urls import path
from .views import RealtorListView, RealtorView, TopSellerView

urlpatterns = [
    path('', RealtorListView.as_view()),#allowany
    path('topseller', TopSellerView.as_view()),#allowany
    path('<pk>', RealtorView.as_view()),#authentication
    
    
]
