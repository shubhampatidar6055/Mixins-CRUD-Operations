from .models import *
from .views import *
from django.urls import path

urlpatterns = [
    path("", StudentCreate.as_view(), name = "create"),
    path("StudentList/", StudentList.as_view(), name = "studentlist"),
    path("StudentGet/<int:pk>/", StudentGet.as_view(), name = "getstudent"),
    path("StudentUpdate/<int:pk>/", StudentUpdate.as_view(), name = "updatestudent"),
    path("StudentDestroy/<int:pk>/", StudentDestroy.as_view(), name = "deletestudent"),
    # path("StudentDetail/<int:pk>/", StudentDetail.as_view(), name = "Studentdetail"),
]
