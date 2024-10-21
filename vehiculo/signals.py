from django.db.models.signals import post_save
from django.contrib.auth.models import User, Permission
from django.dispatch import receiver

@receiver(post_save, sender=User)
def asignar_permiso_visualizar_catalogo(sender, instance, created, **kwargs):
    if created:
        # Obtén el permiso 'visualizar_catalogo' 
        permiso = Permission.objects.get(codename='visualizar_catalogo')
        # Agrega el permiso al usuario
        instance.user_permissions.add(permiso)
