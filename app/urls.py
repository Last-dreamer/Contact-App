from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('detail/<int:pk>', views.ContactDetailView.as_view(), name='detail'),
    path('search/', views.search, name="search"),
    path('contact/create', views.ContactCreateView.as_view(), name="create"),
    path('contact/update<int:pk>', views.ContactUpdateView.as_view(), name="update"),
    path('contact/delete<int:pk>', views.ContactDeleteView.as_view(), name="delete"),
    path('signup/', views.SignUpView.as_view(), name="signup"),


]
