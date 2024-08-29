from django.shortcuts import render
from .models import *
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework import mixins

# Create your views here.
class StudentCreate(GenericAPIView, mixins.CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class StudentList(GenericAPIView, mixins.ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
class StudentGet(GenericAPIView, mixins.RetrieveModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
class StudentUpdate(GenericAPIView, mixins.UpdateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
class StudentDestroy(GenericAPIView, mixins.DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    


    
# class StudentDetail(GenericAPIView, mixins.CreateModelMixin,
#                     mixins.RetrieveModelMixin, mixins.ListModelMixin,
#                     mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
#     def put(self, request, *args, **kwargs):    
#         return self.update(request, *args, **kwargs)
    
#     def delete(self, request, *args, **kwargs):
#         return self.delete(request, *args, **kwargs)