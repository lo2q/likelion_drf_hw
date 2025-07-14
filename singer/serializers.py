from rest_framework import serializers
from .models import Tag, Singer, Song, SingerImage

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class SingerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SingerImage
        fields = ['id', 'image']


class SingerSerializer(serializers.ModelSerializer):
    songs = serializers.SerializerMethodField(read_only=True)
    images = SingerImageSerializer(many=True, read_only=True)
    tags = serializers.SerializerMethodField()

    class Meta:
        model = Singer
        fields = '__all__'
    
    def get_songs(self, instance):
        serializer = SongSerializer(instance.songs, many=True)
        return serializer.data

    def get_tags(self,instance):
        tag = instance.tags.all()
        return [t.name for t in tag]



class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'
        read_only_fields = ['singer']
