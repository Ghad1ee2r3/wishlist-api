from django.shortcuts import render


# Create your views here.
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from datetime import datetime
from django.contrib.auth.models import User
#from items.models import
from items.models import Item
from .serializers import RegisterSerializer ,ItemListSerializer ,ItemDetailSerializer
from rest_framework.filters import SearchFilter,OrderingFilter
# , ClassroomSerializer , ClassroomDetailsSerializer,CreatClassroomSerializer
#from rest_framework.generics import ListAPIView


class Register(CreateAPIView):
    serializer_class = RegisterSerializer



class ItemListView(ListAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemListSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = '__all__'
    ordering_fields = '__all__'


class ItemDetailView(RetrieveAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'item_id'
