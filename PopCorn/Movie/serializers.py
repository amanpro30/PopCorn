from rest_framework import serializers, fields
from rest_framework import generics
from Movie.models import *
from Celebrities.models import *


class ShowSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Show
		fields=(
			
			'id', 
			'Title', 
			'ReleaseDate',
			'Duration', 
			'Description', 
			'Image',   
			'Country', 
			'Budget', 
			'Boc', 
			'Status', 
			'Trailer',
			'Avg_rating', 
			'Num_rating',
			'Type',
			'tagline'
			)	

	def Show(self, validated_data):
		return Show(**validated_data)


	def update(self, instance, validated_data):
		instance.Title = validated_data.get('Title', instance.Title)
		instance.save()
		return instance

class CelebritySerializer(serializers.ModelSerializer):
	
	
	class Meta:
		model = Celebrity
		fields = (
			
		 	'Name',
		 	'Dob', 
			'About', 
			'Image',
			'Nationality',
			#'Height',
			#'award',
		)
	def Celebrity(self, validated_data):
		return Celebrity(**validated_data)

	def update(self, instance, validated_data):
		instance.Name = validated_data.get('Name', instance.Name)
		instance.save()
		return instance
	


class AwardSerializer(serializers.ModelSerializer):
	#celebrity = CelebritySerializer(write_only=True) 

	
	class Meta:
		model=Award
		fields=( 'Name', 'Date','Cast' )

	def Award(self, validated_data) :
		return Award(**validated_data)

	def update(self, instance, validated_data):
		instance.Name = validated_data.get('Name', instance.Name)
		instance.save()
		return instance
	
