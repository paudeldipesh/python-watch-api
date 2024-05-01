from rest_framework import serializers
from watchlist_app.models import Movie

class MovieSerializer(serializers.ModelSerializer):
  len_name = serializers.SerializerMethodField()
  
  class Meta:
    model = Movie
    fields = '__all__'
    # fields = ['id', 'name', 'description']
    # exclude = ['id']
    
  def get_len_name(self, object):
    return len(object.name)
    
  def validate(self, data):
    if data['name'] == data['description']:
      raise serializers.ValidationError('Name and Description should be different')
    else:
      return data
    
  def validate_name(self, value):
    if len(value) < 2:
      raise serializers.ValidationError('Name is too short')
    else:
      return value
  
  def validate_description(self, value):
    if len(value) < 15:
      raise serializers.ValidationError('Descriptions must be at least 15 characters long')
    else:
      return value