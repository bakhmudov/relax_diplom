from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, SeatViewSet, ShowTimeView, TicketOrderView

router = DefaultRouter()
router.register('movies', MovieViewSet, basename='movies')
router.register('seats', SeatViewSet, basename='seats')

urlpatterns = [
    path('', include(router.urls)),
    path('show-times/', ShowTimeView.as_view(), name='show_times'),
    path('show-times/<int:pk>/', ShowTimeView.as_view(), name='show_time'),
    path('ticket-order/', TicketOrderView.as_view(), name='ticket_order')
]
