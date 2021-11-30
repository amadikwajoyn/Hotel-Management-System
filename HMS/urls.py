from HMS import views
from django.conf.urls import url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.homepage, name="homepage"),
    url(r'^about/$', views.about, name="about"),
    url(r'^cart/$', views.cart, name="cart"),
    url(r'^checkout/$', views.checkout, name="checkout"),
    url(r'^contact/$', views.contact, name="contact"),
    url(r'^page_404/$', views.page_404, name=""),
    url(r'^payment_complete/$', views.payment_complete, name="payment_complete"),
    url(r'^payment_received/$', views.payment_received, name="payment_received"),
    url(r'^room_details/$', views.room_details, name="room_details"),
    url(r'^room-grid/$', views.room_grid, name="room_grid"),
    url(r'^user_dashboard_booking/$', views.user_dashboard_booking, name="user_dashboard_booking"),
    url(r'^user_dashboard_profile/$', views.user_dashboard_profile, name="user_dashboard_profile"),
    url(r'^user_dashboard_reviews/$', views.user_dashboard_reviews, name="user_dashboard_reviews"),
    url(r'^user_dashboard_wishlist/$', views.user_dashboard_wishlist, name="user_dashboard_wishlist"),
    url(r'^user_dashboard/$', views.user_dashboard, name="user_dashboard"),
    url(r'^user_profile/$', views.user_profile, name="user_profile"),
    url(r'^login/$', views.signin, name = "signin"),
    url(r'^signup/$', views.signup, name = "signup"),
]
