from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from user.models import CommentUser

User = get_user_model()


class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user = authenticate(**attrs)
        if user and user.is_active:
            return user
        raise serializers.ValidationError({
            'error': 'Wrong username or password'
        })


class RegisterUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    image = serializers.ImageField(use_url=False, max_length=None)

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'image']

    def validate(self, attrs):
        if get_user_model().objects.filter(username=attrs['username']).exists():
            raise serializers.ValidationError({
                'error': 'Username already exists, please choose another one'
            })
        if len(attrs['username']) < 4 or len(attrs['first_name']) < 4 or len(attrs['last_name']) < 4:
            raise serializers.ValidationError({
                'error': 'Username, First name and Last name must be at least 4 character long'
            })
        if len(attrs['password']) < 6:
            raise serializers.ValidationError({
                'error': 'Password must be at least 6 character long'
            })
        return attrs

    def create(self, validated_data):
        user = CommentUser(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            image=validated_data['image']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        if not self.context['request'].user.check_password(attrs['old_password']):
            raise serializers.ValidationError({
                'error': 'Old password is incorrect'
            })
        if len(attrs['new_password']) < 6:
            raise serializers.ValidationError({
                'error': 'Password must be at least 6 character long'
            })
        return attrs

    def update(self, instance, validated_data):
        instance.set_password(validated_data['new_password'])
        instance.save()
        return instance

