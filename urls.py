#travelbooker/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bookings.urls')),
]
#bookings/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # auth
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),

    # profile
    path('profile/', views.profile, name='profile'),

    # travel options
    path('', views.travel_options, name='travel_options'),

    # booking
    path('book/<int:pk>/', views.book_travel, name='book_travel'),

    # my bookings
    path('my-bookings/', views.booking_list, name='booking_list'),
    path('cancel-booking/<int:pk>/', views.cancel_booking, name='cancel_booking'),
]
