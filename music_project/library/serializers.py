from rest_framework import serializers
from .models import Song

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'artist', 'album', 'release_date', 'genre']


        def update(self, instance, validated_data):
            instance.title = validated_data.get('title', instance.title)
            instance.artist = validated_data.get('artist', instance.artist)
            instance.album = validated_data.get('album', instance.album)
            instance.release_date = validated_data.get('release_date', instance.release_date)
            instance.genre = validated_data.get('genre', instance.genre)
            instance.save()
            return instance