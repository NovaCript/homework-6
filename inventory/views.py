from rest_framework import generics
from .models import Warehouse, Product
from .serializers import (
    WarehouseDetailSerializer,
    WarehouseSerializer,
    ProductSerializer,
    ProductPatchSerializer,
)
from .permissions import (
    IsProviderOrAuthenticatedOrReadOnly,
    IsConsumerOrAuthenticatedOrReadOnly,
)


class WarehouseListCreateView(generics.ListCreateAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    permission_classes = [
        IsProviderOrAuthenticatedOrReadOnly,
    ]


class WarehouseDetailView(generics.RetrieveAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseDetailSerializer
    permission_classes = [
        IsProviderOrAuthenticatedOrReadOnly,
    ]


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [
        IsProviderOrAuthenticatedOrReadOnly,
    ]


class ProductUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductPatchSerializer
    permission_classes = [
        IsConsumerOrAuthenticatedOrReadOnly,
    ]

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(
            instance,
            data=request.data,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return
