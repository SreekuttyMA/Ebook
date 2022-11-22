from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import DeletePostSerializer, EbookSerializer, UpdatePostSerializer
from .models import Ebook
  
# Create your views here.
class Ebookviewset(viewsets.ModelViewSet):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    
class DeletePostViewSet(viewsets.ModelViewSet):
    queryset = Ebook.objects.all()
    serializer_class = DeletePostSerializer
    permission_classes = (permissions.IsAuthenticated,)
    http_method_names = ['delete', ]

    def destroy(self, request, pk=None, *args, **kwargs):
        instance = self.get_object()
        # you custom logic #
        return super(DeletePostViewSet, self).destroy(request, pk, *args, **kwargs)

class UpdateViewSet(viewsets.ModelViewSet):
    queryset = Ebook.objects.all()
    serializer_class = UpdatePostSerializer
    http_method_names = ['patch', ]
 
    def perform_update(self, serializer):
        instance = self.get_object()  # instance before update
        self.request.data.get("title", None)  # read data from request
        if self.request.user.is_authenticated:
            updated_instance = serializer.save(author=self.request.user)
        else:
            updated_instance = serializer.save()