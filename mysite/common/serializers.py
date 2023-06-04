from rest_framework.serializers import ModelSerializer
from .models import Post

class PostSerializer(ModelSerializer):
    #username=serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Post
        fields = '__all__'