from rest_framework import viewsets

from todos import models
from . import serializers


class OrgViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Organisation.objects.all()
    serializer_class = serializers.OrgViewSerializers

    def get_queryset(self):
        return super().get_queryset().filter(members=self.request.user)


class TodoViewSet(viewsets.ModelViewSet):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializers

    def get_queryset(self):
        return super().get_queryset().filter(organisation_id__company=self.request.user)
