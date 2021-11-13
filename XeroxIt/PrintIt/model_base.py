from django.contrib.auth.models import User
from django.db import models


class FirstQuerySet(models.query.QuerySet):
    def first(self):
        try:
            return self[0]
        except:
            return None

    def ten(self):
        try:
            return self[:10]
        except:
            return None

class ManagerWithFirstQuery(models.Manager):
    def get_query_set(self):
        return FirstQuerySet(self.model)

class ModelBase(models.Model):
    """ model base """
    objects = ManagerWithFirstQuery()

    class Meta:
        abstract = True

class MasterTrackableModel(ModelBase):
    """ master trackable model """
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=3, related_name="userc_%(class)s")
    cip_address = models.CharField(max_length=20, blank=True, null=True, editable=False)
    uip_address = models.CharField(max_length=20, blank=True, null=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, null=True, editable=False)
    updated_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=3, related_name="useru_%(class)s",
                                   editable=False)

    class Meta:
        abstract = True

class TrackableModel(ModelBase):
    """ trackable model """
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    created_by = models.ForeignKey(User,on_delete=models.DO_NOTHING,default=3,related_name="userc_%(class)s")

    class Meta:
        abstract = True
