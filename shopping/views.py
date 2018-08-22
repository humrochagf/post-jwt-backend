from rest_framework import viewsets

from .models import ShoppingItem
from .serializers import ShoppingItemSerializer


class ShoppingItemViewSet(viewsets.ModelViewSet):

    serializer_class = ShoppingItemSerializer
    queryset = ShoppingItem.objects.all()
