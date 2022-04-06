from rest_framework import serializers
from financepy.models import Register

class RegisterSerializer(serializers.ModelSerializer):
  class Meta:
    model = Register
    fields = ['registerDay','description','price','category']
