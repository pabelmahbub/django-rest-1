from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from myapp.models import Contact
from myapp.serializers import ContactSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import Http404
from rest_framework.views import APIView

from rest_framework import mixins
from rest_framework import generics



class ContactList(generics.ListCreateAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
    
class ContactDetail(generics.RetrieveUpdateDestroyAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
   queryset = Contact.objects.all()
   serializer_class = ContactSerializer

   def get(self, request, *args, **kwargs):
       return self.retrieve(request, *args, **kwargs)
   
   def put(self, request, *args, **kwargs):
       return self.update(request, *args, **kwargs)
   
   def delete(self, request, *args, **kwargs):
       return self.destroy(request, *args, **kwargs)    