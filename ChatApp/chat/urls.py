
from django.urls import path, include
from chat import views as chat_views
from django.contrib.auth.views import LoginView, LogoutView
 
 
urlpatterns = [
    path("Chat_Global", chat_views.ChatgPage, name="chat-global-page"),
    path("Chat_One", chat_views.ChatooPage, name="chat-global-page"),
 
    # login-section
    path("", LoginView.as_view
         (template_name="chat/LoginPage.html"), name="login-user"),
    path("Reg", chat_views.register),
    path("auth/logout/", LogoutView.as_view(), name="logout-user"),
]