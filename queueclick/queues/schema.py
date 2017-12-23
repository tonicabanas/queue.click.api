import graphene
from graphene_django.types import DjangoObjectType
from queueclick.queues import models


class QueueType(DjangoObjectType):
    class Meta:
        model = models.Queue
        interfaces = (graphene.Node,)


class Query(object):
    queue = graphene.Field(QueueType, uuid=graphene.UUID(), shared_token=graphene.String())

    def resolve_queue(self, info, **kwargs):
        queue_uuid = kwargs.get('uuid')
        shared_token = kwargs.get('shared_token')
        user = info.context.user

        if user.is_authenticated and user.queue.uuid == queue_uuid:
            return models.Queue.objects.get(pk=queue_uuid)
        else:
            return models.Queue.objects.get(pk=queue_uuid, shared_token=shared_token)
