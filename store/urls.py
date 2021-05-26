from django.urls import path

from . import views

urlpatterns = [
    path('', views.menu, name="menu"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('about/', views.about, name="about"),
    path('register/', views.register, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('user/', views.userPage, name="user-page"),
    path('account/', views.account, name="account"),

    path('update_item/', views.updateItem, name="updateitem"),
    path('process_order/', views.processOrder, name="process_order"),
    path('admin/', views.dashboard, name="dashboard"),
    path('admin/items', views.items, name="items"),
    path('customer/<str:pk>', views.customer, name="customer"),
    # path('orders/', views.orders, name="orders"),
    # path('order_type/<str:pk>/', views.orderType, name="order_type"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
    path('addItem/', views.addItem, name="addItem"),
    path('update_item/<str:pk>/', views.updateitem, name="update_item"),

]
