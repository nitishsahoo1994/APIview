from django.shortcuts import render
from restapp.models import Employee
from restapp.serializers import EmployeeSerializer
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView,RetrieveAPIView


class EmployeeListCreateAPIView(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class =EmployeeSerializer

class EmployeeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# from rest_framework import mixins
# class EmployeeListCreateModelMixins(mixins.CreateModelMixin,ListAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)
#
# class EmployeeRetriveUpdateDestroyModelMixin(mixins.UpdateModelMixin,mixins.DestroyModelMixin,RetrieveAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     def put(self,request,*args,**kwargs):
#         return self.update(request,*args,**kwargs)
#     def patch(self,request,*args,**kwargs):
#         return self.partial_update(request,*args,**kwargs)
#     def delete(self,request,*args,**kwargs):
#         return self.destroy(request,*args,**kwargs)
