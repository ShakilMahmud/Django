# from rest_framework.generics import (
#                  ListAPIView,
#                  RetrieveAPIView,
#                  UpdateAPIView,
#                  CreateAPIView,
#                  DestroyAPIView
#             )
from rest_framework import viewsets             
from articles.models import article
from .serializers import Articleserializer
  
class UserViewSet(viewsets.ModelViewSet):
      serializer_class=Articleserializer
      queryset=article.objects.all()
  
  
  
  
  
  
  
    #### this was done by genericview
    # class articlelist(ListAPIView):
    #     queryset=article.objects.all()
    #     serializer_class=Articleserializer

    # class articleretrive(RetrieveAPIView):
    #     queryset=article.objects.all()
    #     serializer_class=Articleserializer

    # class articleupdate(UpdateAPIView):
    #     queryset=article.objects.all()
    #     serializer_class=Articleserializer

    # class articlecreate(CreateAPIView):
    #     queryset=article.objects.all()
    #     serializer_class=Articleserializer

    # class articledelete(DestroyAPIView):
    #     queryset=article.objects.all()
    #     serializer_class=Articleserializer