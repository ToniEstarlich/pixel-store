## Comeback [README](../../../README.md#the-functions-and-their-testing-on-the-pixel-store-app)
# pixel-store/clothing_store/
**setting**🟦
```python
INSTALLED_APPS = [
    # my apps
    'home',
]
```
**urls**🟩
```python
urlpatterns = [
    path('', include('home.urls')),
]
```
# pixel-store/home/views.py
## index
**function** 🟩
```python
def index(request):
    return render(request, 'home/index.html', {
        'timestamp': now().timestamp()
    })
```
**urls** 🟩
```python
urlpatterns = [
    path('', views.index, name='home'),
]
```
**html** 🟧 **Jinja** ⬜
``pixel-store/home/templates/home/index.html``
```html
<!--Example-->
<h1>Welcome to Pixel Store</h1>
<p>Current timestamp: {{ timestamp }}</p>
```
``index(request)``
- Renders the home page and includes a timestamp in the context.
## faqs
**function** 🟩
```python
def faqs(request):
    return render(request, 'home/faqs.html')
```
**urls** 🟩
```python
urlpatterns = [
    path('faqs/', views.faqs, name='faqs'),
]
```
**html** 🟧 **Jinja** ⬜
``pixel-store/home/templates/home/faqs.html``
```html
<!--Example-->
<h1>FAQs</h1>
<p>Frequently Asked Questions content here.</p>
```
``faqs(request)``
- Renders the FAQs page.
## about
**function** 🟩
```python
def about(request):
    return render(request, 'home/about.html')
```
**urls** 🟩
```python
urlpatterns = [
    path('about/', views.about, name='about'),
]
```
**html** 🟧 **Jinja** ⬜
``pixel-store/home/templates/home/about.html``
```html
<!--Example-->
<h1>About Us</h1>
<p>Information about the store.</p>
```
``about(request)``
- Renders the About page.
## Comeback [README](../../../README.md#the-functions-and-their-testing-on-the-pixel-store-app)