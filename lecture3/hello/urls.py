from django.urls import path
# import any functions in view.py
from . import views 

# "" is URL path, view.index call function index in view.py, name="index" is name for this path
urlpatterns = [
    path("", views.index, name="index"),
    # path("brian", views.brian,  name="brian"),
    # path("david", views.david, name="david")
    path("<str:name>", views.greet, name="greet")
]