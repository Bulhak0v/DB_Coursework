from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.user_list, name='user_list'),
    path('cars/', views.car_list, name='car_list'),
    path('bookings/', views.booking_list, name='booking_list'),
    path('users/add/', views.add_user, name='add_user'),
    path('cars/add/', views.add_car, name='add_car'),
    path('bookings/add/', views.add_booking, name='add_booking'),
    path('users/edit/<int:pk>/', views.edit_user, name='edit_user'),
    path('cars/edit/<int:pk>/', views.edit_car, name='edit_car'),
    path('bookings/edit/<int:pk>/', views.edit_booking, name='edit_booking'),
    path('users/delete/<int:pk>/', views.delete_user, name='delete_user'),
    path('cars/delete/<int:pk>/', views.delete_car, name='delete_car'),
    path('bookings/delete/<int:pk>/', views.delete_booking, name='delete_booking'),
    path('branches/', views.branches_list, name='branches_list'),
    path('statistics/total_income', views.total_income, name='total_income'),
    path('statistics/most_popular_cars', views.most_popular_cars, name='most_popular_cars'),
    path('user/<int:user_id>/bookings/', views.user_bookings, name='user_bookings'),
    path('car/<int:car_id>/bookings/', views.car_bookings, name='car_bookings'),
    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('user_info', views.user_info, name='user_info'),
    path('user_cars_list', views.user_cars, name="user_cars"),
    path('user_booking', views.user_make_booking_step_one, name='user_make_booking_step_one'),
    path('user_booking/step_two', views.user_make_booking_step_two, name='user_make_booking_step_two'),
    path('user_booking/step_three', views.user_make_booking_step_three, name='user_booking_step_three'),
    path('user_booking/step-four/<int:booking_id>/', views.user_make_booking_step_four, name='user_booking_step_four'),
    path('confirm-agreement/<int:booking_id>/', views.confirm_rental_agreement, name='confirm_rental_agreement'),
    path('cancel-agreement/<int:booking_id>/', views.cancel_rental_agreement, name='cancel_rental_agreement'),
    path('user_info/cancel_booking/<int:pk>/', views.cancel_booking, name='cancel_booking'),
    path('user_info/complete_booking/<int:pk>/', views.complete_booking, name='complete_booking'),
    path('user_info/edit/<int:pk>/', views.edit_user_info, name='edit_user_info'),
    path('user_info/rental_agreement_info/<int:pk>/', views.rental_agreement_info, name='rental_agreement_info'),
]
