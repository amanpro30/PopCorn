from rest_framework import serializers, fields
from rest_framework import generics
from Movie.models import *
from Celebrities.models import *


class ShowSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Show
		fields=('id',  'Duration', 'Description', 'ReleaseDate',  'Country', 'Boc', 'Status', 'Trailer','Avg_rating', 'Num_rating','Type')	



class AwardSerializer(serializers.ModelSerializer):
	
	
	class Meta:
		model=Award
		fields=('id', 'Name', 'Date', 'Cast',)


class CelebritySerializer(serializers.ModelSerializer):
	
	celebrity = AwardSerializer(many=True) 

	class Meta:
		model = Celebrity
		fields = (
			'id',
		 	'Name',
		 	'Dob', 
			'About', 
			'Image',
			'Nationality',
			'celebrity',
		)
	
	
	
	def create(self, validated_data):
		awards_data=validated_data.pop('celebrity')
		celebrity = Celebrities.objects.create(**validated_data)
		for award_data in awards_data:
			Award.objects.create( **award_data) 
		return celebrity
		