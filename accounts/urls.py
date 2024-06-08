from django.urls import path
from .views import CustomLoginView, SignUpView  # Importa la vista de registro

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),  # Agrega una ruta para el registro
    # Aquí puedes agregar otras URL si es necesario
]
