from django.contrib.auth.models import User, Group
from rest_framework import serializers
from tutorial.quickstart.models import *

class HockeyPlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HockeyPlayer
        exclude = ()
        
class HockeyTeamSerializer(serializers.HyperlinkedModelSerializer):
    players = HockeyPlayerSerializer(many=True, read_only=True)
    class Meta:
        model = HockeyTeam
        fields = ('teamname', 'city', 'coach', 'logo', 'mascot', 'players')

class CatBreedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CatBreed
        fields = ('name', 'temperment', 'hair_length')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')