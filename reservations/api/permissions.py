from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):


    def has_permission(self, request, view): # First this method
        return request.user and request.user.is_authenticated

    message = "You must be the owner of this object."

    # If you want to allow only owner users or admin to perform a certain action
    def has_object_permission(self, request, view, obj):
        return (obj.user == request.user) or request.user.is_superuser


    # Farkı su has_permission delete sayfaısını  ilk gösterri, snra on üstünde islemi has_objet ile yapasn has
    # permiison kaldrrsan delete sayfasınıda yetkin olmaz, yani silmeden has permlison
    # calısır obje snn degile goremessn demek