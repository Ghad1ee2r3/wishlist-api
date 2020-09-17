from django.shortcuts import render


# Create your views here.
from rest_framework.generics import ListAPIView, RetrieveAPIView,CreateAPIView
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
    permission_classes=[AllowAny]
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['name', 'description']





class ItemDetailView(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'item_id'
    permission_classes=[IsStaffOrUser]
