from rest_framework import serializers, fields
#from rest_framework import generics
from Movie.models import *
from Celebrities.models import *


class ShowSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Show
		fields=('id', 'Movie_title', 'Duration', 'Description', 'ReleaseDate', 'Genre', 'Country', 'Boc', 'Status', 'Trailer')	



class AwardsSerializer(serializers.ModelSerializer):
	
	
	class Meta:
		model=Awards
		fields=('id', 'Name', 'Date', 'Cast',)


class CelebritiesSerializer(serializers.ModelSerializer):
	
	celebritie = AwardsSerializer(many=True) 

	class Meta:
		model = Celebrities
		fields = (
			'id',
		 	'Name',
		 	'Dob', 'About', 
			'Image', 'Nationality',
			'role',
		)
	
	
	
	def create(self, validated_data):
		awards_data=validated_data.pop('celebritie')
		celebrities = Celebrities.objects.create(**validated_data)
		for award_data in awards_data:
			Awards.objects.create( **award_data) 
		return celebrities
		