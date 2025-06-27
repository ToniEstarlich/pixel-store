# PIXEL STORE

Pixel Store is a fictional textile company that sells creative and modern fashion products online.

![Website Preview](./static/screenshots/responsive.jpg)

## Table of Contents
1. [Tech Stack](#tech-stack)
2. [Wireframes](#wireframes)
3. [The Logo](#the-logo)
4. [Colors](#colors)
5. [UI/UX Screenshots](#uiux-screenshots)
6. [Installation](#installation)
7. [Database](#database)
8. [Backend and Testing](#backend-and-testing)
9. [Problems & Solutions](#problems-and-solutions)
10. [Example of Algorithm / Code](#example-of-algorithm--code)
[Comeback Index](#pixel-store)

---

## 🎯 Objective

The goal of Pixel Store is to create an interactive online shop where customers can browse, explore, and purchase textile products in a seamless full-stack web application.

---

##  Tech Stack
# 💻

### 🎨 Style
- **Bootstrap** – Provides responsive and modern design framework.
- **CSS** – Custom styling for layout and visuals.
- **Flexbox** & **Grid** – Layout systems to organize content.

### 🌐 Frontend
- **HTML** – Structure and content.
- **JavaScript** – Interactivity and dynamic actions.
- **Event Listeners** – Capture and handle user input.

### 🚀 Backend
- **Python** – Backend programming logic.
- **Django** – Framework for building web applications.
- **Allauth** – Handles user authentication and accounts.

### 🗄️ Database
- **PostgreSQL** – Relational database for products, users, orders.

### ✏️ Illustration & Design
- **Procreate** – Designed wireframes and UI sketches.
- **Adobe Illustrator** –  creation and branding.

### 🔄 Version Control
- **Git** – Code tracking.
- **GitHub** – Hosting and collaboration.

[Comeback Index](#pixel-store)
---

##  Wireframes
# 🧩

### Home
| Desktop | Tablet | Mobile |
|--------|--------|--------|
| ![](/wireframes/home-pc.jpg) | ![](/wireframes/home-tablet.jpg) | ![](/wireframes/home_phone.jpg) |

### Shop
| Desktop | Tablet | Mobile |
|--------|--------|--------|
| ![](/wireframes/home_phone.jpg) | ![](/wireframes/shop_tablet.jpg) | ![](/wireframes/shop_phone.jpg) |
### Bag
| Desktop | Tablet | Mobile |
|--------|--------|--------|
| ![](/wireframes/bag_pc.jpg) | ![](/wireframes/bag_tablet.jpg) | ![](/wireframes/bag_phone.jpg) |

### About
| Desktop | Tablet | Mobile |
|--------|--------|--------|
| ![](/wireframes/about_pc.jpg) | ![](/wireframes/about_tablet.jpg) | ![](/wireframes/about_phone.jpg) |

[Comeback Index](#pixel-store)
---

##  The Logo

The logo was created to reflect a young, fresh, and modern textile company. Designed with Adobe Illustrator.

---

##  Colors
# 🎨

```css
body {
  background: radial-gradient(circle, rgb(181, 23, 158) 0%, rgb(86, 11, 173) 100%) !important;
  color: #ff97c9 !important;
  font-family: 'Urbanist', sans-serif;
}

.px-navbar {
  backdrop-filter: blur(10px);
  border-bottom: 1px solid #ff97c9;
}
```

Cards, footer, and navbar were designed to be clean and semi-transparent so the focus stays on the products.

[Comeback Index](#pixel-store)
---

##  UI/UX Screenshots

### Home
| Desktop | Tablet | Mobile |
|--------|--------|--------|
| ![](/screenshots/home-pc.jpeg) | ![](/screenshots/home-tablet.jpeg) | ![](/screenshots/home-phone.jpeg) |

### Shop
| Desktop | Tablet | Mobile |
|--------|--------|--------|
| ![](/screenshots/shop-pc.jpeg) | ![](/screenshots/shop-tablet.jpeg) | ![](/screenshots/shop-phone.jpeg) |

### Bag
| Desktop | Tablet | Mobile |
|--------|--------|--------|
| ![](/screenshots/bag-pc.jpeg) | ![](/screenshots/bag-tablet.jpeg) | ![](/screenshots/bag-phone.jpeg) |

### About
| Desktop | Tablet | Mobile |
|--------|--------|--------|
| ![](/screenshots/about-pc.jpeg) | ![](/screenshots/about-tablet.jpeg) | ![](/screenshots/about-phone.jpeg) |

[Comeback Index](#pixel-store)
---

## Installation
# 🛠️ 

Clone the repository and install dependencies:

```bash
git clone https://github.com/ToniEstarlich/pixel-store.git
cd pixel-store
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

[Comeback Index](#pixel-store)
---

##  Database
# 🗄️

Example Django models:

```python
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField(default=0)
    size = models.CharField(max_length=50, null=True, blank=True)
    color = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)

    def __str__(self):
        return self.name
```

[Comeback Index](#pixel-store)
---

##  Backend and Testing
# 🧪

- `/products/` – Display all products from the database.
- `/bag/` – Manage shopping bag (add/remove items).
- `/checkout/` – Checkout form and order confirmation.
- `/accounts/` – User authentication via Django Allauth.

---

##  Problems & Solutions
# ❗

### Problem:
- Database `makemigrations` failed due to wrong plural naming.

### Solution:
- Added `verbose_name_plural = "Categories"` inside Meta class.

[Comeback Index](#pixel-store)
---

##  Example of Algorithm / Code
# 🧠

### Add product to bag logic

```python
def add_to_bag(request, item_id):
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in bag:
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)
```

[Comeback Index](#pixel-store)
---

## 📫 Contact

Project by [Toni Estarlich](https://github.com/ToniEstarlich)