from rest_framework import serializers
from .models import Movie, Ratings, MovieOrder


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, default=None)
    rating = serializers.ChoiceField(choices=Ratings.choices, default=Ratings.G)
    synopsis = serializers.CharField(default=None)
    added_by = serializers.SerializerMethodField()

    def get_added_by(self, obj: Movie):
        return obj.user.email

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    buyed_at = serializers.DateTimeField(read_only=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)

    title = serializers.SerializerMethodField()

    def get_title(self, obj):
        return obj.movie.title

    buyed_by = serializers.SerializerMethodField()

    def get_buyed_by(self, obj):
        return obj.user.email

    def create(self, validated_data):
        return MovieOrder.objects.create(**validated_data)
