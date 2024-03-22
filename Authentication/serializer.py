from rest_framework import serializers

from Project.models import Doctor

class UserAuthentication(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['mobile']