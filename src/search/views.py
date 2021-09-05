from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from search.serializers import UserSerializer, GroupSerializer, CategorySerializer, ProductSerializer
from search.models import Category, Product
from rest_framework import filters
from django.views.generic import TemplateView


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['@title']
    permission_classes = [permissions.AllowAny]


class Search(TemplateView):
    template_name = 'search/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

