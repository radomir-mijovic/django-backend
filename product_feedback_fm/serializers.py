from rest_framework import serializers
from .models import *


def slug_field(name):
    return serializers.SlugRelatedField(read_only=True, slug_field=name)


class RepliesFeedbackSerializer(serializers.ModelSerializer):
    user = slug_field('get_user_info')

    class Meta:
        model = Replies
        fields = '__all__'


class CreateReplySerializer(serializers.ModelSerializer):
    reply = serializers.CharField(max_length=500, required=True)
    user = slug_field('get_user_info')

    class Meta:
        model = Replies
        fields = '__all__'

    def validate(self, attrs):
        if len(attrs['reply']) < 10:
            raise serializers.ValidationError({
                'reply': 'Reply must be at least 10 character long'
            })


class CommentsFeedbackSerializer(serializers.ModelSerializer):
    user = slug_field('get_user_info')
    replies = RepliesFeedbackSerializer(many=True, read_only=True)
    text = serializers.CharField(max_length=500, required=True)

    class Meta:
        model = Comments
        fields = '__all__'

    def validate(self, attrs):
        if len(attrs['text']) < 10:
            raise serializers.ValidationError({
                'text': 'Reply must be at least 10 character long'
            })
        return attrs


class ReadProductsFeedbackSerializer(serializers.ModelSerializer):
    comments = CommentsFeedbackSerializer(many=True, read_only=True)

    class Meta:
        model = ProductFeedback
        fields = '__all__'
        read_only_field = fields


class ProductsFeedbackSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100, required=True)
    category = serializers.CharField(max_length=400, required=True)
    status = serializers.CharField(max_length=100, required=True)
    description = serializers.CharField(max_length=500, required=True)
    comments = CommentsFeedbackSerializer(many=True, read_only=True)

    class Meta:
        model = ProductFeedback
        fields = '__all__'

    def validate(self, attrs):
        if len(attrs['title']) < 4:
            raise serializers.ValidationError({
                'title': 'Title must be at least 4 character long'
            })
        return attrs


class ProductFeedbackUpVotesSerializer(serializers.ModelSerializer):
    comments = CommentsFeedbackSerializer(many=True, read_only=True)

    class Meta:
        model = ProductFeedback
        fields = '__all__'
