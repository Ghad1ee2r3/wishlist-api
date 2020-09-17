from django.shortcuts import render


# Create your views here.
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
# from datetime import datetime
from django.contrib.auth.models import User

from items.models import Item
from .serializers import RegisterSerializer ,ItemListSerializer ,ItemDetailSerializer
from rest_framework.filters import SearchFilter,OrderingFilter
from api.permissions import IsStaffOrUser
from rest_framework.permissions import AllowAny



class Register(CreateAPIView):
    serializer_class = RegisterSerializer



class ItemListView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemListSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = '__all__'
    ordering_fields = ['name','id']
    permission_classes=['AllowAny']


class ItemDetailView(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'item_id'
    permission_classes=['IsStaffOrUser']
