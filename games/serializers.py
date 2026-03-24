from rest_framework import serializers

from .models import Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ["id", "name", "url", "author", "plays", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]
