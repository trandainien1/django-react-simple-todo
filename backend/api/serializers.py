from django.contrib.auth.models import User
from rest_framework import serializers

# serializer will look at the input of User. Then it will check the validation of input. Then it will call create() with validated data
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        # write_only: no one know about the password
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
