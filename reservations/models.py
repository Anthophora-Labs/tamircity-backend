from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from device_types.models import DeviceType
from brands.models import Brand
from models.models import Model
from service_types.models import ServiceType


RESERVATION_STATUS = (
    ("Pending", "Pending"),
    ("Cancelled", "Cancelled"),
    ("Approved", "Approved"),
    ("Completed", "Completed"),
)

OPERATIONAL_STATUS = (
    ("WAITING_FOR_REPAIR", "WaitingforRepair"),
    ("IN_PROGRESS", "InProgress"),
    ("COMPLETED", "Completed"),
    ("DEVICE_HAS_BEEN_DELIVERED", "DeviceHasBeenDelivered"),
)

"""
const (
	OperationStatus_WAITING_FOR_REPAIR OperationStatus = "WaitingforRepair" // İşlem Bekliyor
	OperationStatus_IN_PROGRESS        OperationStatus = "InProgress"       // İşleme Alındı
	OperationStatus_COMPLETED          OperationStatus = "Completed"        // Hazır Tamamlandı
	//OperationStatus_PRICE_OFFER_WILL_BE_GIVEN               OperationStatus = "PriceWillbeGiven"                  // Fiyat Verilecek
	//OperationStatus_SMS_WILL_BE_SENT_FOR_PRICE_CONFIRMATION OperationStatus = "SmsWillBeSentForPriceConfirmation" // Fiyat Onayı İçin SMS Gönderildi
	//OperationStatus_PENDING_PRICE_CONFIRMATION              OperationStatus = "PendingPriceConfirmation"          // Fiyat Onay Bekliyor
	//OperationStatus_PRICE_OFFER_NOT_APPROVED                OperationStatus = "PriceOfferNotApproved"             // Onaylanmadı
	//OperationStatus_WAITING_FOR_SPARE_PARTS                 OperationStatus = "WaitingforSpareParts"              // Parça Bekliyor
	//OperationStatus_THE_DEVICE_CANNOT_BE_REPAIRED           OperationStatus = "TheDeviceCannotBeRepaired"         // Onarım Yapılamıyor
	//OperationStatus_DEVICE_WILL_BE_RETURNED                 OperationStatus = "DeviceWillBeReturned"              // Cihaz İade Edilecek
	//OperationStatus_DEVICE_HAS_BEEN_RETURNED                OperationStatus = "DeviceHasBeenReturned"             // Cihaz İade Edildi
	OperationStatus_DEVICE_HAS_BEEN_DELIVERED OperationStatus = "DeviceHasBeenDelivered" // Cihaz Teslim Edildi
	//OperationStatus_OPERATION_HAS_BEEN_CANCELLED            OperationStatus = "OperationHasBeenCancelled"         // Servis İşlem İptal Edildi
)
"""

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # or TechService
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=50)
    second_phone_number = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='reservations', blank=True, null=True)
    # modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='modified_by', blank=True, null=True)

    device_type = models.ForeignKey(DeviceType, on_delete=models.CASCADE, related_name='reservations')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='reservations')
    model = models.ForeignKey(Model, on_delete=models.CASCADE, related_name='reservations')
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE, related_name='reservations')

    status = models.CharField(max_length=50, choices=RESERVATION_STATUS, default=RESERVATION_STATUS[0][0])
    operational_status = models.CharField(max_length=50, choices=OPERATIONAL_STATUS, default=OPERATIONAL_STATUS[0][0])

    slug = models.SlugField(unique=True, max_length=150, editable=False) # Editable ile buna hiç bi şekilde endpoint dahil ulasamaz ekleme tyapalaz gormez
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    """
    Date               time.Time
	WeekDay            time.Weekday
	StartOfHour        int
	EndOfHour          int
	Price              int
    """

    def __str__(self):
        return f"{self.full_name} {self.email} {self.created_date}"

    def get_slug(self):
        slug = slugify(self.full_name.replace("ı", "i"))
        unique_slug = slug
        counter = 1
        while Reservation.objects.filter(slug=unique_slug).exists():
            unique_slug = "{}-{}".format(slug, counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.id:
            pass
            #self.created_date = timezone.now() ## run when created objects
        #self.updated_date = timezone.now() ## run when updated objects
        self.slug = self.get_slug()
        return super(Reservation, self).save(*args, **kwargs)