from rest_framework import serializers
from todos import models


class OrgViewSerializers(serializers.ModelSerializer):

    class Meta:
        fields = (
            'name',
            'company',
        )
        model = models.Organisation


class TodoSerializers(serializers.ModelSerializer):

    class Meta:
        fields = (
            'organisation',
            'title',
            'description',
        )
        model = models.Todo
