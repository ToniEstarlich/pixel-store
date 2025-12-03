## Comeback [README](../../../README.md#the-functions-and-their-testing-on-the-pixel-store-app)
# pixel-store/users/app.py
"Signals automatically execute functions in response to model events and are activated by importing them in the app’s ``apps.py``, not via URLs or ``settings.py``."

**app**🟦
```python
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        instance.userprofile.save()
```
# pixel-store/users/models.py
- The ``UserProfile`` model extends Django’s User by storing optional default contact and address details for easier checkout.

**models** 🟦
```python
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    ...
    def __str__(self):
        return self.user.username
```
# pixel-store/users/signals.py
## create_or_update_user_profile
**function** 🟩
```python
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        instance.userprofile.save()
```
- ``create_or_update_user_profile``: Listens for the ``post_save`` signal of the ``User`` model.

- If a new user is created, it automatically creates a ``UserProfile`` for them.

- If an existing user is updated, it saves the associated ``UserProfile``.
## Comeback [README](../../../README.md#the-functions-and-their-testing-on-the-pixel-store-app)
