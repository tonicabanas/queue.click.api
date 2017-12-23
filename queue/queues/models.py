from uuid import uuid4

from django.core.validators import MinValueValidator
from django.db import models
from helpers.fields import TruncatingCharField
from model_utils import Choices
from model_utils.models import TimeStampedModel, StatusModel


class Queue(models.Model):
    user = models.OneToOneField('users.User', on_delete=models.CASCADE)
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    start_time = models.TimeField()
    end_time = models.TimeField()
    shared_token = models.UUIDField(unique=True, default=uuid4, editable=False)
    events = models.ManyToManyField('Event')

    def __str__(self):
        return '{}'.format(self.uuid)


class Event(TimeStampedModel, StatusModel):
    STATUS = Choices('pending', 'in_progress', 'done', 'canceled')
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    order = models.PositiveIntegerField()
    reporter_name = TruncatingCharField(max_length=40)
    description = models.TextField(max_length=140)
    estimated_time_min = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return '{} - {}'.format(self.uuid, self.reporter_name)
