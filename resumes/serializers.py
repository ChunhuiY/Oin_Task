
from rest_framework import serializers
from .models import Resume

class ResumeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    email = serializers.ReadOnlyField()

    class Meta:
        model = Resume
        fields = '__all__'

    def validate_education(self, value):
        if not isinstance(value, list):
            raise serializers.ValidationError("Education must be a list of objects.")
        return value

    def validate_work_experiences(self, value):
        if not isinstance(value, list):
            raise serializers.ValidationError("Work experiences must be a list of objects.")
        return value

