from django.contrib.auth.models import User
from django.db import models
from XeroxIt.settings import IsPaid,IsPrinted,PaperType,DeviceStatus,DeviceTypes,Type
from . import model_base as CoreModels
# Create your models here.


class ExtendedUser(CoreModels.TrackableModel):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    phone_number = models.IntegerField(blank=True)
    age = models.IntegerField(null=True, blank=True, default=0)
    type =  models.CharField(max_length=9,choices = Type,default="Consumer")



class Location(CoreModels.TrackableModel):
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    long = models.DecimalField(max_digits=9, decimal_places=6)
    addressline = models.CharField(max_length=200, null=True, blank=True)
    area = models.CharField(max_length=200, null=True, blank=True)
    landmark = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    landmark = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.addressline + " " + self.area + " " + self.city

class Node(CoreModels.TrackableModel):
    name = models.CharField(max_length=200, null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    gst = models.IntegerField(null=True, blank=True, default=0)
    def __str__(self):
        return self.name


class UserLocation(CoreModels.TrackableModel):
    user = models.ForeignKey(ExtendedUser, on_delete=models.SET_NULL, null=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.user.name


class Review(CoreModels.TrackableModel):
    user = models.ForeignKey(ExtendedUser, on_delete=models.SET_NULL, null=True)
    node = models.ForeignKey(Node, on_delete=models.SET_NULL, null=True)
    rating =  models.IntegerField(null=True, blank=True, default=0)
    comment = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.comment


class Document(CoreModels.TrackableModel):
    img = models.ImageField(null=True, blank=True)
    pdf = models.FileField(upload_to='pdf',null=True, blank=True)


class Price(CoreModels.TrackableModel):
    Papertype = models.CharField(max_length=19, choices=PaperType, default="No")
    price = models.IntegerField(null=True, blank=True, default=0)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    range = models.IntegerField(null=True, blank=True, default=100000)
    def __str__(self):
        return self.Papertype

class Status(CoreModels.TrackableModel):
    auto_id = models.AutoField(primary_key=True)
    status_name = models.CharField(max_length=200,default='', null=True, blank=True)
    def __str__(self):
        return self.status_name

class Action(CoreModels.TrackableModel):
    name = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.name



class OrderStatusMap(CoreModels.TrackableModel):
    From = models.ForeignKey(Status, on_delete=models.DO_NOTHING, default=None,related_name="check_from_flow")
    action = models.ForeignKey(Action, on_delete=models.SET_NULL, null=True)
    to = models.ForeignKey(Status, on_delete=models.DO_NOTHING, default=None)
    def __str__(self):
        return str(self.From) + " " + str(self.action)
    class Meta:
        db_table = 'order_status_map'


class Order(CoreModels.TrackableModel):
    user = models.ForeignKey(ExtendedUser, on_delete=models.SET_NULL, null=True)
    node = models.ForeignKey(Node, on_delete=models.SET_NULL, null=True)
    payment_method = models.CharField(max_length=200, null=True, blank=True)
    is_paid =  models.CharField(max_length=9,choices = IsPaid,default="No")
    paid_at = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    is_printed = models.CharField(max_length=19,choices = IsPrinted,default="No")
    price = models.IntegerField(null=True, blank=True, default=0)
    document = models.ForeignKey(Document, on_delete=models.SET_NULL, null=True)
    From = models.IntegerField(null=True, blank=True, default=0)
    status = models.IntegerField(null=True, blank=True, default=0)
    def __str__(self):
        return str(self.user.name) + " " + str(self.node.name)

class Device(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    ip = models.CharField(max_length=200, null=True, blank=True)
    Node = models.ForeignKey(Node, on_delete=models.SET_NULL, null=True)
    type = models.CharField(max_length=19, choices=DeviceTypes, default="No")
    device_status = models.CharField(max_length=19, choices=DeviceStatus, default="No")

    def __str__(self):
        return self.name

class OrderDevice(models.Model):
    device = models.ForeignKey(Device, on_delete=models.SET_NULL, null= True)
    order_id = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)