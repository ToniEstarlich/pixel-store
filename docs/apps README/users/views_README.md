## Comeback [README](../../../README.md#the-functions-and-their-testing-on-the-pixel-store-app)
# pixel-store/clothing_store/
**setting**🟦
```python
INSTALLED_APPS = [
    # my apps
    'users',
]
```
**urls**🟩
```python
urlpatterns = [
    path("users/", include("users.urls")),
]
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
# pixel-store/users
/forms.py
**form**🟦
```python
class CustomRegisterForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')

    def save(self, request):
        user = super(CustomRegisterForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user
    
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
    
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'default_phone_number',
            'default_street_address1',
            'default_town_or_city',
            ...
        ]

        labels = {
            'default_phone_number': 'Phone number',
            'default_street_address1': 'Street address 1',
            'default_town_or_city': 'Town / City',
            ...,
        }
```
# pixel-store/users/views.py
## register
**function** 🟩
```python
def register(request):
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        ...
        return render(request, 'users/register.html', {'form': form})
```
**urls** 🟩
```python
urlpatterns = [
    path('register/', views.register, name='register'),
]
```
**html** 🟧 **Jinja** ⬜
``pixel-store/users/templates/users/register.html``
```html
<form method="POST">
    {% csrf_token %}
    {{ form|crispy }}
    <button type="submit" class="btn btn-primary">Register</button>
</form>
```
- ``register(request)``: Handles user registration. Creates a ``UserProfile`` for the new user, logs them in, and redirects to the profile page.
## profile_view
**function** 🟩
```python
@login_required
def profile_view(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    ...
    return render(request, 'users/profile.html', {
        'user_form': user_form,
         'profile_form': profile_form,
     })
```
**urls** 🟩
```python
urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.profile_view, name='edit_profile'),
]
```
**html** 🟧 **Jinja** ⬜
``pixel-store/users/templates/users/profile.html``
```html
     <!-- Account Details -->
    <div class="col-md-6 mb-3">
      <div class="profile-card glass-card p-3">
        <h2 class="profile-title">Account Details</h2>
        <p><strong>E-mail:</strong> {{ user.email }}</p>
        <p><strong>Username:</strong> {{ user.username }}</p>
        ...
      </div>
    </div>

      <!-- Edit Profile Form -->
    <form method="POST" action="{% url 'edit_profile' %}">
          {% csrf_token %}
          <h3>Account Info</h3>
          {{ user_form.as_p }}

          <h3>Address Info</h3>
          {{ profile_form.as_p }}
          <button type="submit" class="btn btn-success mt-2">Save Changes</button>
     </form>
```
- ``profile_view(request)``: Displays and allows editing of the logged-in user’s profile and account info. Saves changes if the form is submitted.
## my_orders
**function** 🟩
```python
@login_required
def my_orders(request):

    user_profile = UserProfile.objects.get(user=request.user)
    orders = Order.objects.filter(user_profile=user_profile).order_by('-date')

    return render(request, 'users/my_orders.html',{'orders': orders})
```
**urls** 🟩
```python
urlpatterns = [
    path('my-orders/', views.my_orders, name='my_orders'),
]
```
**html** 🟧 **Jinja** ⬜
``pixel-store/users/templates/users/my_orders.html``
```html
    {% for order in orders %}
          <li class="orders-item">
            <div>
              <strong>Order #:</strong> {{ order.order_number }}<br>
              <strong>Date:</strong> {{ order.date|localtime|date:"SHORT_DATETIME_FORMAT" }}<br>
              <strong>Total (raw):</strong> £{{ order.grand_total }}
            </div>
          </li>
    {% endfor %}
```
- ``my_orders(request)``: Retrieves all orders associated with the logged-in user and displays them in reverse chronological order.
## Comeback [README](../../../README.md#the-functions-and-their-testing-on-the-pixel-store-app)