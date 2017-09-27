from django.contrib.auth.models import User, Group
from rest_framework import serializers
from transi.models import Document, Paragraph, Translated

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class DocumentSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Document
		fields = ('title', 'created_date', 'original_lang', 'target_lang', 'owner')

class ParagraphSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Paragraph
		fields = ('document', 'content')

class TranslatedSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Translated
		fields = ('paragraph', 'content')