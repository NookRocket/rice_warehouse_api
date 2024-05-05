from rest_framework import serializers
from .models import Seed

class SeedSerializer(serializers.ModelSerializer):

    id = serializers.ReadOnlyField()
    
    class Meta:
        model = Seed
        fields = [
            "id",
            "year",
            "year_week",
            "varity",
            "rdcsd",
            "stock2sale",
            "season",
            "crop_year",
        ]
