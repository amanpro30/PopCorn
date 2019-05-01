from rest_framework import serializers, fields
from rest_framework import generics
from Movie.models import *
from Celebrities.models import *


class ShowSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Show
		fields=('id', 'Title', 'ReleaseDate', 'Duration', 'Description', 'Image',   'Country', 'Budget', 'Boc', 'Status', 'Trailer','Avg_rating', 'Num_rating','Type')	


class CelebritySerializer(serializers.ModelSerializer):
	
	
	class Meta:
		model = Celebrity
		fields = (
			
		 	'Name',
		 	'Dob', 
			'About', 
			'Image',
			'Nationality',
			'Height',
			#'award',
		)
	


class AwardSerializer(serializers.ModelSerializer):
	#celebrity = CelebritySerializer(write_only=True) 

	
	class Meta:
		model=Award
		fields=( 'Name', 'Date', )

	
	
	def create(self, validated_data):
		celebritys_data=validated_data.pop('celebrity')
		awards = Award.objects.create(**validated_data)
		for celebrity_data in celebritys_data:
			Celebrity.objects.create(awards=Cast, **celebrity_data) 
		return awards
	