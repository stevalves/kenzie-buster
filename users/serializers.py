from rest_framework import serializers
from .models import User
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    username = serializers.CharField(
        max_length=30,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(), message="username already taken."
            )
        ],
    )
    email = serializers.CharField(
        max_length=127,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(), message="email already registered."
            )
        ],
    )
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    birthdate = serializers.DateField(default=None)
    is_employee = serializers.BooleanField(default=False)
    is_superuser = serializers.BooleanField(read_only=True)
    password = serializers.CharField(write_only=True)

    def create(self, validated_data: dict):
        if validated_data.get("is_employee"):
            return User.objects.create_superuser(**validated_data)
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()

        return instance
