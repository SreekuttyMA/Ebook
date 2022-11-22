from . models import Ebook
from rest_framework import serializers

class EbookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ebook
        fields = '__all__'

class DeletePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ebook
        fields = '__all__'

class UpdatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ebook
        fields = '__all__'