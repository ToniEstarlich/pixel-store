# PIXEL STORE

Pixel Store is a fictional textile company that sells creative and modern fashion products online.


![Website Preview](./screenshots/responsive.jpg)
You can check the live application here: [Pixel Store](https://pixel-store-6fb82487a320.herokuapp.com/)
With features such as user authentication, product management, a shopping bag system, and secure checkout integration.

The project focuses on combining aesthetic design with functional usability, aiming to reflect the values of a brand that is both bold and innovative. It supports various screen sizes and provides a seamless experience across desktop, tablet, and mobile devices.

## - User Stories

As a user:

-  **browse products by category** so that I can easily find the items I’m interested in.
-  **view product details** so that I can check price, description.
-  **register an account and log in** so that I can manage my profile and view my orders.
-  **add and remove items from the shopping bag** so that I can control what I purchase.
-  **checkout securely** so that I can pay with confidence and receive confirmation of my order.
-  the website to be **responsive** so that I can shop smoothly on desktop, tablet, or mobile.

## Repository and Live Project  

You can find the source code for **Pixel Store** in the GitHub repository below:  

- **Repository:** [https://github.com/ToniEstarlich/pixel-store](https://github.com/ToniEstarlich/pixel-store)  

The live version of the project is accessible here:  

- **Live Project:** [https://pixel-store-6fb82487a320.herokuapp.com/](https://pixel-store-6fb82487a320.herokuapp.com/)  


## Table of Contents
1. [Tech Stack](#tech-stack)
2. [Project Structure](#project-structure)
3. [Wireframes](#wireframes)
4. [The Logo](#the-logo)
5. [Colors](#colors)
6. [UI/UX accessibility and Screenshots](#ux--accessibility)
7. [Installation](#installation)
8. [Data Models](#data-models)
9. [Problems & Solutions](#problems--solutions)
10. [Code Example](#code-example)
11. [functions and testing](#the-functions-and-their-testing-on-the-pixel-store-app)
12. [Value for Users and CRUD](#value-for-users)
13. [Pytest](#testing)
14. [pep8 & black](#code-quality-pep8--linters)
15. [Environment Variables ``(.env)``](#environment-variables-env)
16. [Deployment](#deployment)

## **Legend:**

- 🔵 [Database layer](#data-models) (models)
- 🟢 [Backend logic](#the-functions-and-their-testing-on-the-pixel-store-app) (views, urls, context processors)
- 🟠 [Frontend layer](#crud-features) (templates)
- 🔴 [Testing](#testing) (pytest)

“Emojis act as a visual map of the app layers, showing how models, backend logic, templates, and tests are connected in a coherent workflow.”

## Pixel Store – Design & Evaluation Rationale

This section reflects on the key design decisions behind Pixel Store, explaining the rationale for the chosen technologies, evaluating database and testing choices, highlighting UX and security considerations, and outlining trade-offs and future improvement opportunities.
> ℹ️ Click on the ▼ icons in each section to view the full content. Sections are collapsible to make navigation easier.

### Table of Contents
- 1️⃣ [Framework Choice – Django](#framework-choice-django)  
- 2️⃣ [Database Choice – PostgreSQL](#database-choice-postgresql) 
- 3️⃣ [Libraries and Tools](#libraries-and-tools)
- 4️⃣ [Application Architecture & Organization](#application-architecture-and-organization)    
- 5️⃣ [UX / UI Decisions](#ux--ui-decisions)  
- 6️⃣ [Key Functionalities](#key-functionalities) 
- 7️⃣ [HTML/CSS Validation](#htmlcss-validation)
- 8️⃣ [Testing Strategy](#testing-strategy)   
- 9️⃣ [Security Practices](#security-practices)  
- 🔟 [Trade-offs & Conscious Decisions](#trade-offs-and-conscious-decisions)

---
# Why Pixel Store?

Pixel Store is an online store, but more importantly, it is a complete full-stack architecture exercise focused on separation of responsibilities, basic security, and a real e-commerce flow, prioritizing structure and maintainability over advanced features.

>⚠️ **Note :** Click on the headings (▼) to expand and see the full details of each section, including design rationale, code examples, and testing strategies.

###  Framework Choice: Django
<details>
  <summary><h3 style="color:#007bff;">1️⃣ Design Rationale</h3></summary>
  <p style="color:#007bff;">Django was chosen because it was a project requirement and, additionally, it is one of the most complete and robust frameworks for web applications. It simplifies authentication, security, and database management, allowing the implementation of critical e-commerce functionalities (registration, login, product management, and cart) without reinventing the wheel. I chose this project motivated by the Level 5 E-commerce tutorial, and Pixel Store seemed the best option to apply these concepts in a practical way.</p>
</details>
## Code & Architecture Decisions

<details>
<summary><h3>🚀 Why Django?</h3></summary>

<ul>
  <li>Clear MVC / MTV architecture</li>
  <li>Built-in ORM → fewer SQL errors</li>
  <li>Proven authentication and security system</li>
  <li>Ideal for applications with complex models (orders, cart, users)</li>
</ul>
<details>
<summary><h3>⚙ How to install</h3></summary>

📦 Installation

```bash
pip install django
```
🧠 Usage

- Django is installed at the project level

- Used across multiple apps following Django’s recommended architecture

- Provides the foundation for models, views, forms, and templates

</details> 
</details>

> “Django is a robust full-stack framework that already includes authentication, security, and an ORM, allowing me to focus on the business logic of an e-commerce application instead of reinventing critical functionality.”

<details>
<summary><h3>🧩 Why split the project into apps?</h3></summary>

<ul>
  <li><strong>products</strong> → product catalog (independent from users)</li>
  <li><strong>users</strong> → authentication and user profiles</li>
  <li><strong>bag</strong> → decoupled shopping cart (session + database)</li>
  <li><strong>checkout</strong> → critical order and payment logic</li>
  <li><strong>home</strong> → informational pages</li>
</ul>
<details>
<summary><h3>⚙ Example: creating and installing an app</h3></summary>

📦 Create a new app

```bash
python manage.py startapp products
```
🔧 Register the app

```python
# settings.py
INSTALLED_APPS = [
    ...
    'products',
]
```
🧠 Architectural note

- Each app owns its own models, views, templates, and URLs

- Business logic is isolated per app

- Apps communicate only when necessary

</details>
</details>

> “The project is divided into independent apps to keep the codebase clean, scalable, and easy to maintain.”

<details>
<summary><h3>🔁 Typical Pixel Store Request Flow</h3></summary>

<ul>
  <li>The user enters the store</li>
  <li>Django queries products from PostgreSQL</li>
  <li>The view processes the data</li>
  <li>The template renders the HTML</li>
</ul>
<details>
<summary><h3>⚙ Example: product list request</h3></summary>

(🔵)Models

```python
# products/models.py
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
```
(🟢) View

```python
# products/views.py
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/products.html', {'products': products})
```
(🟢)URL

```python
# products/urls.py
path('', product_list, name='product_list')
```
(🟠) Template

```html
{% for product in products %}
  <p>{{ product.name }} - {{ product.price }}</p>
{% endfor %}
```
</details> 
</details>

> “The request flow always follows the same pattern:  
> (🔵) models → (🔵) forms → (🟢) views → (🟢) urls → (🟢) context processors → (🟠) templates”

## Library Decisions

<details>
<summary><h3>🔐 Django Allauth</h3></summary>

<ul>
  <li>Manages sessions, passwords, and CSRF protection</li>
  <li>Less custom code = fewer bugs</li>
  <li>Industry-standard authentication solution</li>
</ul>

<details>
<summary><h3>⚙ How to install</h3></summary>

📦 Installation

```bash
pip install django-allauth
```
🔧 Configuration

```python
# settings.py
INSTALLED_APPS = [
    ...
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
]

SITE_ID = 1

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]
```
🧠 Usage

- Centralized authentication

- Forms and views managed by Allauth

- Integrated mainly in the users app
</details>
</details>

> “Allauth is a secure and well-tested authentication solution. I avoided implementing custom login logic to prevent common security mistakes.”

<details> 
<summary><h3>🎨 Bootstrap + Crispy Forms</h3></summary> 
<ul> 
<li>Focus on usability</li> 
<li>Use of professional tooling</li> 
<li>No time wasted reinventing styles</li> 
</ul> 
<details> 
<summary><h3>⚙ How to install</h3></summary>

📦 Installation

```python
pip install django-crispy-forms crispy-bootstrap4
```
🔧 Configuration

```python
# settings.py
INSTALLED_APPS = [
    ...
    'crispy_forms',
    'crispy_bootstrap4',
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
CRISPY_TEMPLATE_PACK = "bootstrap4"
```
🧠 Usage

```html
{% load crispy_forms_tags %}
{{ form|crispy }}
```
</details>
</details>

> “Bootstrap allows me to guarantee responsive design quickly, while Crispy Forms helps render clean and accessible forms without repeating HTML.”

<details> 
<summary><h3>💳 Stripe</h3></summary> 
<ul> 
<li>No credit card data is stored</li> 
<li>Stripe complies with industry regulations</li> 
<li>Widely adopted industry standard</li>
</ul> 
<details> <summary><h3>⚙ How to install</h3></summary>

📦 Installation

```python
pip install stripe
```

🔧 Configuration
```python
# settings.py
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")
```

🧠 Usage
```python
# checkout/views.py
import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY
```
</details>
</details>

>“Stripe is used to simulate real payments securely without handling sensitive user data. Payment logic is isolated in the checkout app.”

## Security Decisions

<details>
<summary><h3>🔐 Environment Variables (.env)</h3></summary>
<ul>
<strong>Examples:</strong>
<li>SECRET_KEY</li>
<li>STRIPE keys</li>
<li>DATABASE_URL</li>
</ul>
<details>
<summary><h3>⚙ Example usage</h3></summary>

📦 Define environment variables

```python
# .env
SECRET_KEY=secret-key
STRIPE_SECRET_KEY=sk_test_xxx
DATABASE_URL=postgres://user:password@localhost:0000/pixel_store
```
🔧 Load variables in Django settings

``` python
# settings.py
import os

SECRET_KEY = os.getenv("SECRET_KEY")
DATABASES = {
    'default': dj_database_url.parse(os.getenv("DATABASE_URL"))
}
```
🧠 Security note

- Sensitive data is never committed to version control

- .env files are excluded via .gitignore

- Different environments use different values
</details> 
</details>

> “Sensitive keys are stored using environment variables to prevent accidental exposure on GitHub.”

<details>
<summary><h3>🛡️ Django Security</summary>
<ul>
<li>DEBUG disabled in production</li> 
<li>ALLOWED_HOSTS properly configured</li>
 <li>Forms validated using Django Forms</li>
</ul>
<details>
<summary><h3>⚙ Example configuration</h3></summary>

🔧 Production settings

```python
# settings.py
DEBUG = False

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'pixelstore.example.com',
]
```
🧠 Form validation

```python
# checkout/forms.py
class OrderForm(forms.Form):
    full_name = forms.CharField(max_length=100)
    email = forms.EmailField()
```
🛡️ **Security note**

- CSRF protection enabled by default

- Secure password hashing handled by Django

- Session management managed by the framework

</details> 
</details>

> “Django automatically handles CSRF protection, secure sessions, and password hashing.”

<details>
<summary><h3>🧪 Testing</h3></summary>
<ul>
<li>Not everything is tested → only critical paths</li>
 <li>Realistic prioritization</li> 
 <li>Early bug detection before production</li>
</ul>
<details>
<summary><h3>⚙ Example: critical business logic test</h3></summary>
🔬 Test focus

- Models with business logic
- Shopping cart behavior
- Checkout and payment flow
- Form validation

🧪 Example test

```python
# bag/tests/test_bag.py
def test_add_product_to_bag(client, product):
    response = client.post('/bag/add/', {'product_id': product.id})
    assert response.status_code == 200
```
✅ Testing approach

- Pytest is used for clarity and simplicity

- Tests focus on behavior, not implementation details

- Critical paths are covered before deployment

</details> 
</details>

> “Tests were implemented using pytest for critical components: models with business logic, cart behavior, checkout flow, and forms.”


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

[Back to Table of Contents](#table-of-contents)
---
# Project Structure
# 📁
```graphql
pixel-store/
│
├── bag/                 # Shopping bag functionality (views, templates, tests)
│
├── checkout/            # Checkout and order processing (views, forms, tests, templates)
│
├── clothing_store/      # Internal app (possibly settings or shared logic)
│
├── home/                # Home page views and templates
│
├── media/               # Uploaded product images
│   └── product_images/
│
├── products/            # Product models, views, templates, and tests
│
├── screenshots/         # Screenshots for README and design reference
│
├── static/              # Static files (CSS, JS, images)
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/           # Global templates
│   ├── includes/        # Shared components like sliders, navigation, footer
│   └── base.html, 404.html, etc.
│
├── users/               # User authentication, profiles, templates, and tests
│
├── wireframes/          # UI design drafts and wireframes
│
├── manage.py
├── requirements.txt
├── README.md
├── .gitignore
├── Procfile             # Deployment configuration (e.g., Heroku)
└── …                     # Other files such as database dumps or examples

```
##  Wireframes
# 🧩

## - Design Iteration

The Pixel Store project went through several design phases:

- Initial **wireframes** outlined the structure of Home, Shop, Bag, and About pages.
- The first version focused on **basic functionality**, ensuring that products could be displayed and added to the bag.
- Based on feedback, the design was refined to improve **navigation, responsiveness, and accessibility**.
- A **vibrant gradient color palette** and a **custom logo** were introduced to reflect the bold and creative identity of the brand.
- Iterations improved the **UI/UX**, including button placement, form validation, and clear error messages during checkout.
- Images and product cards were later optimized for better performance and visual appeal.

---

### Home
| Desktop | Tablet | Mobile |
|--------|--------|--------|
| ![](/wireframes/home-pc.jpg) | ![](/wireframes/home-tablet.jpg) | ![](/wireframes/home_phone.jpg) |

### Shop
| Desktop | Tablet | Mobile |
|--------|--------|--------|
| ![](/wireframes/shop_pc.jpg) | ![](/wireframes/shop_tablet.jpg) | ![](/wireframes/shop_phone.jpg) |
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

![Website Preview](./wireframes/scketch.jpg)

The Pixel Store logo was designed to represent a young, fresh, and modern textile brand. It combines clean lines with a playful aesthetic to appeal to a fashion-conscious, digital-savvy audience.

The initial concept was hand-sketched using Procreate, capturing the creative spirit of the brand. This sketch was then translated into code using HTML and CSS, ensuring scalability, responsiveness, and seamless integration into the website design.

---

##  Colors
# 🎨
The Pixel Store design uses a vibrant, modern color palette to reflect the brand’s creative and fashion-forward identity. The color choices aim to create contrast, visual interest, and a memorable user experience.

![Website Preview](./screenshots/colors_pallets.jpg)

| Purpose                         | Color Code                                          | Description                                                                                                      |
| ------------------------------- | --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **Background Gradient**         | `radial-gradient(circle, #b5179e 0%, #560bad 100%)` | A bold, eye-catching gradient with purple and magenta tones that gives the site a futuristic and trendy vibe.    |
| **Primary Text Highlights**     | `#ff97c9`                                           | A soft neon pink used for accent text elements and headings to enhance readability and style.                    |
| **Icons (default color)**       | `#c0c7cf`                                           | A clean light-gray tone used for neutral icons (like the shopping cart or nav icons).                            |
| **Hover Color (icons & links)** | `#ffc107`                                           | A vibrant yellow/gold tone applied on hover for logo and social media icons, helping to highlight interactivity. |


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

[Back to Table of Contents](#table-of-contents)
---
## UX + Accessibility

The Pixel Store was designed with a strong focus on usability and accessibility. Navigation is simple and consistent across all pages, with clear visual hierarchy and intuitive button placement. Interactive elements, such as buttons and promotional slides (``slide-AD.html`` and ``slide-AD-2.html``), include hover states and clear feedback to improve user confidence. Text colors and backgrounds follow accessible contrast ratios to ensure readability. Forms provide clear validation messages, preventing user frustration. The layout is fully responsive, ensuring a smooth experience on mobile, tablet, and desktop. Alt text is included for all images, and non-essential animations were minimized to reduce cognitive load. These design choices make the site intuitive, engaging, and accessible for a wide range of users.

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
### Reusable UI Components

To enhance the visual appeal and marketing feel of the site, two reusable slide
components were created:

- `slide-AD.html`
- `slide-AD-2.html`

```html
pixel-store
   |_/static
     |_ /js
       |_ /slide-AD.js 🟨
       |_ /slide-AD-2.js 🟨
   |_ /templates
     |_ /includes
       |_slide-AD.html 🟧
       |_slide-AD-2.html 🟧
```

These components are stored inside `templates/includes/` and are included where
needed using Django template inheritance.  
This approach keeps templates clean, avoids duplication, and allows the slides to
be reused or repositioned easily across different pages.

## Custom 404 Page

A custom 404 page was added to improve user experience when users navigate to a non-existent page. The page provides a clear message ("Oops! Page not found") and a direct link back to the homepage. It is fully responsive, visually consistent with the site’s design, and includes clear visual hierarchy and accessible button styling. This ensures users are guided smoothly back to the main site and reduces frustration when encountering broken links.

[Back to Table of Contents](#table-of-contents)
---

## - Git & Version Control  
![Website Preview](./wireframes/pixel_diagram.jpg)

- Version control was managed using **Git** and hosted on **GitHub**.  
- The project was mainly developed on the **main branch**, with **frequent commits** documenting progress.  
- Clear commit messages (e.g., *added checkout logic*, *fixed product model bug*) were used to track changes.  
- GitHub was also used for deployment to **Heroku**, ensuring smooth version tracking and project backup.  
- The project was initially started using **Django Allauth**, inspired by the e-commerce tutorial video from the course, providing a foundation for user authentication and registration.  
- Custom **context_processors.py** were added to Pixel Store apps to manage shared data across templates, improving code reusability and ensuring dynamic content (e.g., shopping bag contents, product categories) was consistently available.

[Back to Table of Contents](#table-of-contents)
---

# Data Models 
# 🗄
Describes the data model used in the Pixel Store application, including all entities and relationships between them.

Database migrations were created and applied using Django’s built-in migration system
(`makemigrations` and `migrate`) to keep the PostgreSQL database schema aligned with the models.

### Database Choice: PostgreSQL
<details style="color:#007bff; padding:10px; border-radius:5px;">
<summary><h3>2️⃣ Design Rationale</h3></summary>
  <p>PostgreSQL was selected for its scalability, referential integrity, and efficient handling of concurrent transactions, and also because it is familiar to me from my experience at Amazon Career and projects in C#/.NET. This choice allows managing multiple users and complex relationships between models robustly, something SQLite does not handle optimally in production environments.</p>
</details>


## Model Overview
- Products (`products/models.py`)
- Users (`users/models.py`)
- Bag (`bag/models.py`)
- Checkout (`checkout/models.py`)

**Legend:**
- 🔵 Database layer (models)
- 🟢 Backend logic (views, urls, context processors)
- 🟠 Frontend layer (templates)
- 🔴 Testing (pytest)

# pixel-store/products/models.py

## 🧩 1. Category

Represents product categories (e.g., t-shirts, hoodies, accessories).

**Key fields:**

- name — unique category name.

**Relationships:**

-**One-to-Many:** One category can contain many products.
```mathematica
Category 1 ───▶ * Product
```
## 🛍️ 2. Product

Represents items available for sale in the store.

**Key fields:**

- ``name``, ``sku``, ``description``, ``extra_information``,

- ``price``, ``stock``, ``size``, ``color``, ``image``

- ``category`` — ForeignKey to ``Category``

**Relationships:**

- Many products belong to one category.

- A product can appear in multiple order line items.

- A product can appear multiple times in BagItem (shopping cart).
```markdown
Category 1 ───▶ * Product ───▶ * OrderLineItem
                         └──▶ * BagItem
```
### Request Flow
- (🔵)models.py → (🟢)views.py → (🟢)urls.py → (🟢)context_processors.py → (🟠)
templates/
### Functions:
- [(🟢)views.py → (🟢)urls.py → (🟢)context_processors.py](#products)
### CRUD:
- [(🟠)Templates/](#5-shop-page)
# pixel-store/users/models.py
## 👤 3. UserProfile

Extends Django’s built-in ``User`` model with additional customer information.

**Key fields:**

- One-to-One with User

- Phone number, address fields, city, postcode, country

**Relationships:**

- **One-to-Many:** One user profile may have multiple orders.
```sql
User 1 ───▶ 1 UserProfile ───▶ * Order
```
### Request Flow
- (🔵)models.py → (🔵)forms.py → (🟢)views.py → (🟢)urls.py → (🟢)signals.py → (🟠)
templates/
### Form:
- [(🔵)forms.py](#user-registration-and-profiles)
### Functions:
- [(🟢)views.py → (🟢)urls.py → (🟢)signals.py](#users)
### CRUD:
- [(🟠)Templates/](#1-user-registration)
# pixel-store/bag/models.py
## 👜 4. BagItem (Shopping Cart Item)

Represents individual items a user has added to their shopping bag.

**Key fields:**

- ``user`` — FK to User

- ``product`` — FK to Product

- ``size``, ``quantity``

**Constraint:**

- ``unique_together = (user, product, size)``
Prevents the same product/size combination from appearing multiple times.

Relationships:
```sql
User 1 ───▶ * BagItem ◀── * Product
```
### Request Flow
- (🔵)models.py → (🟢)views.py → (🟢)urls.py → (🟢)context_processors.py → (🟢)signals.py → (🟠)
templates/
### Functions:
- [(🟢)views.py → (🟢)urls.py → (🟢)context_processors.py → (🟢)signals.py](#bag-2)
### CRUD:
- [(🟠)Templates/](#7-shopping-bag)
# pixel-store/checkout/models.py
## 📦 5. Order

Represents a completed purchase after checkout.

**Key fields:**

- Customer details (name, email, phone)

- Shipping address

- Totals: ``order_total``, ``delivery_cost``, ``grand_total``

- ``user_profile`` — optional FK (guest checkouts allowed)

- Auto-generated ``order_number``

**Logic:**

- ``_generate_order_number()`` creates a unique ID.

- ``update_total()`` recalculates order totals and delivery cost.

**Relationships:**
```sql
Order 1 ───▶ * OrderLineItem
```
## 🧾 6. OrderLineItem

Represents each individual product line inside an order.

**Key fields:**

- ``order`` — FK to Order

- ``product`` — FK to Product

- ``quantity``

- ``lineitem_total``

**Logic:**

Automatically calculates ``lineitem_total`` (price × quantity) when saving.

## 📊 Data Model Relationship Diagram 
```sql
User ───1──▶ UserProfile ───1──▶* Order ───1──▶* OrderLineItem
  │                               ▲
  │                               │
  └──▶* BagItem ◀─────1──── Product ───▶ Category
```
### Request Flow
- (🔵)models.py → (🔵)forms.py → (🟢)views.py → (🟢)urls.py →  (🟠)
templates/
### Form:
- [(🔵)forms.py](#checkout)
### Functions:
- [(🟢)views.py → (🟢)urls.py](#checkout-1)
### CRUD:
- [(🟠)Templates/](#8-checkout)
## Forms & User Input Handling

The project uses Django Forms and ModelForms to handle user input in a clean and secure way.

### Libraries and Tools
<details style="color:#007bff; padding:10px; border-radius:5px;">
  <summary><h3>3️⃣ Design Rationale</h3></summary>
  <ul>
    <li><strong>Django Allauth:</strong> secure and tested authentication, allowing focus on e-commerce logic without reinventing critical features.</li>
    <li><strong>Bootstrap 4:</strong> provides a flexible grid, reusable components, and visual consistency, accelerating development and reducing design errors.</li>
    <li><strong>django-crispy-forms:</strong> renders forms cleanly and consistently with Bootstrap, avoiding repetitive HTML.</li>
  </ul>
  <p>These choices improve productivity, security, and user experience, providing clear and consistent interfaces.</p>
</details>

### User Registration and Profiles
- A custom registration form extends Django Allauth’s `SignupForm` to collect additional user information such as first and last name during signup.
- `UserForm` allows users to update basic account details (name and email).
- `UserProfileForm` is linked to the `UserProfile` model and is used to manage delivery and contact information.

Using ModelForms ensures automatic validation and keeps form logic consistent with the database models.

### [(🔵)forms.py](/docs/apps%20README/users/views_README.md)

### Checkout

- `OrderForm` is a ModelForm connected to the `Order` model.
- It collects delivery and contact information during checkout.
- Validation is handled automatically by Django before an order is saved.

This approach improves security, reduces duplicated code, and keeps form handling aligned with Django best practices.

### [(🔵)forms.py](/docs/apps%20README/checkout/views_README.md)

[Back to Table of Contents](#table-of-contents)
---
### What is it and what is it for?
This documentation summarizes the main files in each Pixel Store app:  
- **views.py** → handles the business logic and response to HTTP requests (renders templates, processes forms, manages sessions, etc.)  
- **context_processors.py** → injects common variables into templates (like timestamps, shopping bag contents, categories)  
- **signals.py** → automatically executes functions in response to model events (like creating UserProfiles or loading BagItems on login)  

# The functions and their testing on the Pixel Store app
### Application Architecture and Organization
<details style="color:#007bff; padding:10px; border-radius:5px;">
  <summary><h3>4️⃣ Design Rationale</h3></summary>
  <p>The application is organized into the following apps: <strong>home</strong>, <strong>products</strong>, <strong>users</strong>, <strong>bag</strong>, and <strong>checkout</strong>:</p>
  <ul>
    <li><strong>home:</strong> entry point of the project, contains initial presentation and navigation.</li>
    <li><strong>products:</strong> manages and stores the store’s products.</li>
    <li><strong>users:</strong> handles registration, login, and profile management.</li>
    <li><strong>bag:</strong> independent shopping cart, synchronized with session and database.</li>
    <li><strong>checkout:</strong> handles payment flow and order confirmation.</li>
  </ul>
  <p>This separation facilitates maintainability, scalability, and readability, avoiding mixing logic from different areas. The organization was inspired by tutorials, course material, and reference repositories.</p>
</details>

Use the links below to explore each file’s purpose and its corresponding tests.

## home
- ### [views.py](/docs/apps%20README/home/views_README.md)🟢
  >``home/views.py`` renders the main pages: ``index`` with timestamp, ``faqs``, and ``about``.
- ### [context_processors.py](/docs/apps%20README/home/context_processors_README.md)🟢
  >``home/context_processors.py`` provides a ``timestamp`` context processor, making the current timestamp available in all templates.
  - ### [test](/docs/test%20README/home_README.md)🔴
    >``home/tests/`` verifies views and context processors: pages return 200, correct templates are used, and ``timestamp`` is present and an integer in all templates.
- ### [Templates/](#4-information-pages)🟠
  >The ``home`` app provides static informational pages such as the About page and manages global site elements, including the footer with useful links like FAQs.
## products
- ### [models.py](#pixel-storeproductsmodelspy)🔵
  >The Product model represents items available for sale, each belonging to a single Category, and can be referenced multiple times in both order line items and shopping bag entries
- ### [views.py](/docs/apps%20README/products/views_README.md)🟢
  >``products`` app defines ``Category`` and ``Product`` models, and provides views for listing products (with optional category filter), searching by name, and displaying individual product details, all rendered with Jinja templates.
- ### [context_processors.py](/docs/apps%20README/products/context_processors_README.md)🟢
  >``products/context_processors.py`` provides ``get_categories``, making all product categories available in templates for navigation or filtering.
  - ### [test](/docs/test%20README/products_README.md)🔴
    >``products/tests/`` verifies the ``Category`` model and ``get_categories`` context processor: the model’s ``__str__`` returns the category name, and the context processor provides a list of categories in templates.
- ### [Templates/](#5-shop-page)🟠
  >The ``products`` app powers the Shop section, allowing users to browse products, view detailed information, select size and quantity, and add items to their shopping bag.
## users
- ### [models.py](#pixel-storeusersmodelspy)🔵
  >The UserProfile model extends Django’s built-in User model with additional customer details and is linked to multiple orders created by the same user.
- ### [forms.py🔵](#user-registration-and-profiles)
  >User and profile forms with Django, secure and model-driven.
- ### [views.py](/docs/apps%20README/users/views_README.md)🟢
  >``users`` app manages user accounts: ``register`` handles signup and creates a ``UserProfile``, ``profile_view`` displays and edits account and profile info, and ``my_orders`` lists the user’s orders.
- ### [signals.py](/docs/apps%20README/users/signals_README.md)🟢
  >``users/signals.py`` listens to ``User`` model changes and automatically creates or updates a ``UserProfile`` whenever a user is created or saved.
  - ### [test](/docs/test%20README/users_README.md)🔴
    >``users/tests/`` verifies user-related functionality: profile page access and template rendering, ``UserProfile`` string representation, and that ``UserProfileForm`` includes all expected fields.
- ### [Templates/](#1-user-registration)🟠
  >The ``users`` app handles user accounts, including registration, login, logout, profile management, and viewing past orders
## bag
- ### [models.py](#pixel-storebagmodelspy)🔵
  >The BagItem model represents individual products added to a user’s shopping bag, linking users and products while ensuring each product–size combination is stored only once.
- ### [views.py](/docs/apps%20README/bag/views_README.md)🟢
  >``bag`` app manages the shopping bag: ``view_bag`` displays items with totals, ``add_to_bag`` adds or updates items via POST/AJAX, ``remove_from_bag`` deletes items, and ``clear_bag`` empties the bag for the user.
- ### [context_processors.py](/docs/apps%20README/bag/context_processors_README.md)🟢
  >``bag/context_processors.py`` provides ``bag_contents`` and ``calculate_bag_total``, making the current shopping bag items, counts, and totals available in all templates.
- ### [signals.py](/docs/apps%20README/bag/signals_README.md)🟢
  >``bag/apps.py`` activates signals on app ready, and ``bag/signals.py`` automatically loads a logged-in user’s ``BagItems`` into the session, reconstructing the shopping bag.
  - ### [test](/docs/test%20README/bag_README.md)🔴
    >``bag/tests/`` verifies shopping bag functionality: pages return 200 and use correct templates, add/remove/clear actions update session and redirect properly, URLs resolve correctly, and context processors calculate totals, counts, and bag items accurately.
- ### [Templates/](#7-shopping-bag)🟠
  >The ``bag`` app manages the shopping bag functionality, allowing users to review selected items, remove products, and view subtotals and delivery costs before checkout.
## checkout
- ### [models.py](#pixel-storecheckoutmodelspy)🔵
  >The ``checkout`` app manages completed purchases through the ``Order`` and ``OrderLineItem`` models, separating order-level data from individual product lines for clarity and scalability.
- ### [forms.py🔵](#checkout)
  >Checkout form for orders, secure and validated via Django ModelForms
- ### [views.py](/docs/apps%20README/checkout/views_README.md)🟢
  >``checkout/`` handles order processing: displays checkout form if the bag isn’t empty, validates and saves orders and line items, creates a Stripe checkout session, empties the bag, and shows a success page with order details.
  - ### [test](/docs/test%20README/checkout_README.md)🔴
    >checkout/tests/ verifies the checkout flow: redirects when the bag is empty, ensures checkout success page loads correctly, confirms order numbers are auto-generated, and validates the OrderForm with correct data.
- ### [Templates/](#8-checkout)🟠
  >The checkout app manages the purchase process, including delivery details, payment, order confirmation, and post-purchase options.
# 📱 User Experience (UX) — Pixel Store
After creating an account, the user can:

- Browse products and filter by category
- Search products by name
- View product details
- Add, update, or remove items in the shopping bag
- Proceed to checkout and complete orders
- View order history in their profile
- Edit account and shipping information

[Back to Table of Contents](#table-of-contents)
---
## Value for Users

Pixel Store offers a fast, responsive, and easy shopping experience where users can browse clothing products, manage a dynamic shopping bag, and complete purchases securely using Stripe. The platform provides clear product information, intuitive navigation, and real-time feedback during checkout, making online shopping simple and enjoyable for all users.

## CRUD Features
### UX / UI Decisions
<details style="color:#007bff; padding:10px; border-radius:5px;"  >
  <summary><h3>5️⃣ Design Rationale</h3></summary>
  <ul>
    <li>Clear and predictable layout, prioritizing quick access to products, cart, and user profile.</li>
    <li>Forms with visible validations, semantic labels, and clear error messages, ensuring a consistent and accessible user experience.</li>
    <li>Basic accessibility principles: clear labels, visible feedback, and coherent visual structure for maximum usability.</li>
  </ul>
</details>

### 1. User Registration
- Users can create an account through the registration form.

<img src="./screenshots/CRUDs/1-sigin.jpeg" alt="Website Preview" width="300">



### 2. Login & Redirect
- After registering or logging in, the user is automatically redirected to the Home page.

<img src="./screenshots/CRUDs/2-inside.jpeg" alt="Website Preview" width="300">

### 3. Account Management
- Users can:
  - Log out
  - View account details
  - View their orders
  - Edit their profile
  
  <img src="./screenshots/CRUDs/3-account.jpeg" alt="Website Preview" width="300">

  >**1, 2 & 3:**

    **models**
      [(🔵)models.py](#pixel-storeusersmodelspy)

    **form**
      [(🔵)forms.py](#user-registration-and-profiles)
 
    **functions:**
     [(🟢)views.py → (🟢)urls.py → (🟢)signals.py](#users)
### 4. Information Pages
- Users can explore the About page.

<img src="./screenshots/CRUDs/4-about.jpeg" alt="Website Preview" width="300">

- The Footer includes useful links such as FAQs.

<img src="./screenshots/CRUDs/4-FAQs.jpeg" alt="Website Preview" width="300">

>**4:**

**functions:**
[(🟢)views.py → (🟢)urls.py](#home-2)

### 5. Shop Page
- The main store is located in the Shop section.
- Each product card allows users to:
  - Select a size
  - Choose a quantity
  - Add items to their bag
  
  <img src="./screenshots/CRUDs/5-shop.jpeg" alt="Website Preview" width="300">
  
  - View detailed product information

  <img src="./screenshots/CRUDs/5-more-details.jpeg" alt="Website Preview" width="300">
    
### 6. Navbar
- Products: Browse different clothing categories.
- Search: Find items quickly by name or keyword.

 >**5 & 6 :**

  **models**
    [(🔵)models.py](#pixel-storeproductsmodelspy)
    
  **Functions:**
     [(🟢)views.py → (🟢)urls.py → (🟢)context_processors.py](#products)


### 7. Shopping Bag
- Users can:
  - Review their selected items
  - Remove items
  - View the subtotal
  - See delivery costs
  
  <img src="./screenshots/CRUDs/6-bag.jpeg" alt="Website Preview" width="300">

  >**7 :**

  **models**
    [(🔵)models.py](#pixel-storebagmodelspy)

  **functions:** [(🟢)views.py → (🟢)urls.py → (🟢)context_processors.py → (🟢)signals.py](#bag-2)

### 8. Checkout
- Users enter their delivery details during the checkout process.

<img src="./screenshots/CRUDs/7-checkout.jpeg" alt="Website Preview" width="300">

### 9. Payment
- After checkout, users are redirected to the Payment Details page.

<img src="./screenshots/CRUDs/8-pay.jpeg" alt="Website Preview" width="300">

### 10. Order Confirmation
- A confirmation message is shown:
  “Thank you! Your order number is 00000000.”
  
  <img src="./screenshots/CRUDs/9-order-number.jpeg" alt="Website Preview" width="300">
- Users can choose to:
  - Continue shopping
  - View their orders
 
  <img src="./screenshots/CRUDs/9-my-orders.png" alt="Website Preview" width="300">
  
  >**8, 9 & 10:**

  **models**
    [(🔵)models.py](#pixel-storecheckoutmodelspy)

  **form**
    [(🔵)forms.py](#checkout)

  **Checkout functions:**
    [(🟢)views.py → (🟢)urls.py](#checkout-1)

### Key Functionalities
<details style="color:#007bff; padding:10px; border-radius:8px;" >
 <summary><h3> 6️⃣ Design Rationale</h3></summary>
  <ul>
    <li><strong>Cart (bag):</strong> independent, synchronized between session and database. Allows adding products even without being logged in, ensuring persistence upon login.</li>
    <li><strong>Order and OrderLineItem:</strong> reflect real purchases; separate the order from products, facilitating calculations and future expansions.</li>
    <li><strong>OneToMany relationships:</strong> used when an element clearly belongs to another, allowing specific information (quantity, price) per order line.</li>
    <li><strong>Separate categories:</strong> for normalization, filtering, and data reuse.</li>
    <li><strong>Context processors & AJAX:</strong> improve UX and avoid duplicated code.</li>
    <li><strong>Signals:</strong> automate critical tasks, such as creating user profiles or synchronizing the cart upon login.</li>
  </ul>
  <p>The approach prioritized clarity, reusability, and user flow, inspired by real e-commerce platforms and tutorials.</p>
</details>


## [Back to Table of Contents](#table-of-contents)

## Problems & Solutions
# ❗

### Development Bug

### Database migration issue
- **Problem:** `makemigrations` failed due to wrong plural naming in the Category model.
- **Solution:** Added `verbose_name_plural = "Categories"` inside Meta class.
 
  ```python
  class Category(models.Model):
    name = models.CharField(max_length=100)
    ...
    class Meta:
        verbose_name_plural = "Categories"  # bug solution
  ```
- **Outcome:** Migrations now run successfully and database schema is correct.

### Order date issues (My Orders)
- **Problem:** Some orders displayed incorrect or missing dates in the “My Orders” page.
- **Solution:** Ensured the `Order` model assigns a valid timestamp when creating an order (`auto_now_add=True`) and confirmed the template references this field correctly.

 ``checkout/models.py``
 
```python
class Order(models.Model):
    ...
    date = models.DateTimeField(auto_now_add=True) # the date
```
``users/views.py``

```python
orders = Order.objects.filter(user_profile=user_profile).order_by("-date")
```

``users/templates/users/my_orders.html``
```html
{{ order.date|localtime|date:"SHORT_DATETIME_FORMAT" }}
```
- **Outcome:** All orders now display correct dates in “My Orders” and timestamps are consistent.

### Incorrect shopping bag total
- **Problem:** The total amount displayed in the shopping bag did not match the total sent to Stripe during checkout.
- **Solution:** Adjusted the calculation logic in `checkout/views.py` to ensure that all item quantities, prices, and delivery costs are correctly summed and sent to Stripe.
```python
# calculate subtotal for Stripe
line_items = []
for item_id, quantity in bag.items():
  ...
    product = get_object_or_404(Product, pk=int(item_id.split("_")[0]))

  ...
    line_items.append({
        "price_data": {
            "currency": "gbp",
            "product_data": {"name": product.name},
            "unit_amount": int(product.price * 100),
        },
        "quantity": quantity,
    })
...
# Add delivery cost if applicable
if delivery_cost > 0:
                line_items.append(
                    {
                        "price_data": {
                            "currency": "gbp",
                            "product_data": {
                                "name": "Delivery Cost",
                            },
                            "unit_amount": delivery_cost,
                        },
                        "quantity": 1,
                    }
                )
```
- **Outcome:** Shopping bag total now matches the Stripe payment total in all scenarios, ensuring correct payment processing.

### Image storage limitation in Admin

- **Problem:** When adding products via Django Admin, uploaded images were not saved on Heroku deployment because Heroku’s filesystem is ephemeral. This prevented product images from persisting.

- **Solution:** Decided to keep the project as-is for deployment simplicity. Using external storage (e.g., AWS S3) would solve the issue, but it requires a paid service, so it was deferred.

- **Outcome:** Project functions correctly with placeholder images, and the limitation is documented. Images work locally, and the Admin remains fully functional.

### HTML/CSS Validation

<details style="color:#007bff; padding:10px; border-radius:8px;">
  <summary><h3>7️⃣ Design Rationale</h3></summary>
  <ul>
    <li>Minor warnings detected from external libraries (Bootstrap, Font Awesome), which do not affect functionality or UX.</li>
    <li>A model pluralization issue in the database was corrected via <code>verbose_name_plural</code>.</li>
    <li>Stability and maintainability were prioritized over 100% W3C validation of external resources.</li>
  </ul>
</details>

## HTML Validation
The HTML code was validated using the W3C Markup Validation Service.  
[https://validator.w3.org/](https://validator.w3.org/)


### Problem:
- The validator showed some warnings and minor errors.
- Most issues come from external libraries (e.g. Font Awesome, Bootstrap).
- Use of `<i>` tags for icons and dynamic attributes like `aria-*`.

### Solutions:
- No changes were made because:
  - These issues are not critical.
  - They do not affect accessibility or functionality.
  - They originate from trusted third-party libraries.

---

## CSS Validation
The CSS was validated using the W3C CSS Validator.  
[https://jigsaw.w3.org/css-validator/](https://jigsaw.w3.org/css-validator/)

### Problem:
- One error from Font Awesome CDN:
  - `rotate(var(--fa-rotate-angle, none))` is not a valid transform value.
- 1400+ warnings due to:
  - Vendor extensions like `-webkit-` and `-moz-`.
  - Use of CSS variables in the external stylesheet.

### Solutions:
- No changes were made because:
  - All issues come from an external CDN (Font Awesome).
  - Modifying CDN files is not recommended.
  - The website displays correctly with the current styles.

## Testing
# 🧪 
### Testing Strategy
<details style="color:#007bff; padding:10px; border-radius:8px;" >
  <summary><h3>8️⃣ Design Rationale</h3></summary>
  <ul>
    <li><strong>Main tool:</strong> pytest, for clear syntax, readable tests, and good organization.</li>
    <li><strong>Priority areas:</strong> models with logic, critical views, forms, context processors, cart, and checkout.</li>
    <li>End-to-end tests were not implemented due to project scope; focus was on functional and unit testing, ensuring key flows.</li>
    <li><strong>Testing criteria:</strong> logic-heavy features, persistent data, critical flows, or areas prone to break with future changes.</li>
  </ul>
  <p>Tests cover status codes, templates, context processors, model methods, forms, session handling, AJAX, and URLs.</p>
</details>

Tests were run using **pytest** in a Django environment.

<img src="./screenshots/CRUDs/pytest.png" alt="Website Preview" width="500">

>📌 **Note:** “During testing, two initial bugs were found: an uninitialized variable in the bag app and a form validation mismatch in checkout. Both were corrected and verified. Remaining warnings were assessed but deemed non-critical.”

### How to Run the Tests

- From the project root, run:

```bash
pytest
```
- you can also run tests using Django’s test runner:
```bash
python manage.py test
```
- To run a specific test file:
```bash
pytest pixel-store/bag/tests/test_views.py
```
- To run a single test function:
```bash
pytest pixel-store/bag/tests/test_views.py::TestClass::test_remove_from_bag
```
### Summary
Although a strict TDD workflow was not followed from the beginning, tests were added alongside feature development and organized per app. Git commits reflect the iterative process of building functionality and validating it through tests.

### conftest.py explanation
The conftest.py file is used to configure and initialize Django for pytest, ensuring that settings and applications are loaded before running tests.

- ✅ 22 tests passed
- ❌ 2 tests failed
- ⏭ 1 test skipped
- ⚠️ 9 warnings

Failures were caused by an uninitialized product variable in the add_to_bag view for anonymous users, and by an over-strict form test expecting a non-essential default_county field. Both issues were resolved, resulting in a fully passing test suite.

<img src="./screenshots/CRUDs/testing-ok.png" alt="Website Preview" width="500">


- **Home**
  - ### [test](/docs/test%20README/home_README.md)🛑
    >``home/tests/`` verifies views and context processors: pages return 200, correct templates are used, and ``timestamp`` is present and an integer in all templates.

    - **What was tested:** Views and context processors  
    - **Results:** ✅3 passed, 🟨 2 warnings  

- **Products**
  - ### [test](/docs/test%20README/products_README.md)🛑
    >``products/tests/`` verifies the ``Category`` model and ``get_categories`` context processor: the model’s ``__str__`` returns the category name, and the context processor provides a list of categories in templates.
    -  **What was tested:** Models, views, and context processors  
    -  **Results:** ✅4 passed    

- **User**
  - ### [test](/docs/test%20README/users_README.md)🛑
    >``users/tests/`` verifies user-related functionality: profile page access and template rendering, ``UserProfile`` string representation, and that ``UserProfileForm`` includes all expected fields.
    -  **What was tested:** Models, views, and forms  
    -  **Results:** ✅3 passed, 🟫1 skipped,🟨1 warning  

- **Bag**
  - ### [test](/docs/test%20README/bag_README.md)🛑
    >``bag/tests/`` verifies shopping bag functionality: pages return 200 and use correct templates, add/remove/clear actions update session and redirect properly, URLs resolve correctly, and context processors calculate totals, counts, and bag items accurately.
    -  **What was tested:** Views, context processors, and URLs  
    -  **Results:** ✅10 passed, 🟨4 warnings   

- **Checkout**
  - ### [test](/docs/test%20README/checkout_README.md)🛑
    >checkout/tests/ verifies the checkout flow: redirects when the bag is empty, ensures checkout success page loads correctly, confirms order numbers are auto-generated, and validates the OrderForm with correct data.
    -  **What was tested:** Forms, models, and views  
    -  **Results:** ✅4 passed, 🟨2 warnings   


> 📌 **Note:** “Tests were added alongside feature development to validate functionality, even though a strict TDD workflow was not followed.”

[Back to Table of Contents](#table-of-contents)
---
## Code Quality: PEP8 & Linters
# 🧹

To keep the **Pixel Store** project clean, consistent, and professional, PEP8 style guidelines were applied together with Python linters.


### 🛠️ How it was done
1. Installation of the linters:
   ```bash
   pip install flake8 black
2. Running Flake8 to detect style issues and warnings:
   ```bash
     flake8 .
   ````
3. Formatting the entire codebase automatically with Black:
   ```bash
      black .
   ```
4. ✅ Results

- Removed unused imports and variables.

- Fixed indentation, spacing, and long line issues.

- Codebase became cleaner, more readable, and more consistent.

- Reduced the risk of future bugs.

- Improved maintainability and overall project quality.

[Back to Table of Contents](#table-of-contents)
---
## Environment Variables (.env)
# 🔐
### Security Practices
<details style="color:#007bff; padding:10px; border-radius:8px;">
  <summary><h3>9️⃣ Design Rationale</h3></summary>
  <ul>
    <li>Use of environment variables for credentials and Stripe keys.</li>
    <li>DEBUG disabled in production.</li>
    <li>CSRF protection in forms.</li>
    <li>Secure session management and authentication through Django Allauth.</li>
    <li>ALLOWED_HOSTS configured and secret keys separated from the code.</li>
    <li>MFA or additional encryption was not implemented due to project scope, but could be added in future phases.</li>
  </ul>
</details>

This project uses a ``.env`` file to store sensitive configuration values.
The ``.env`` file is listed in ``.gitignore`` to prevent these secrets from being committed to the repository.
```blash
Example .env
STRIPE_PUBLIC_KEY=your_stripe_public_key
STRIPE_SECRET_KEY=your_stripe_secret_key
DATABASE_URL=postgres://user:password@localhost:5432/databasename
```

**Purpose of Each Variable**

- STRIPE_PUBLIC_KEY – Used on the client side to initialize Stripe.

- STRIPE_SECRET_KEY – Used on the server side to process secure Stripe payments.

- DATABASE_URL – Defines the connection string for the PostgreSQL database.

These environment variables are required for the project to run correctly and securely.

[Back to Table of Contents](#table-of-contents)
---
## Deployment

Pixel Store was deployed to **Heroku** using a **Heroku PostgreSQL** database.  
Below is the exact process I followed to deploy the project:

1. I created a new Heroku app from the Heroku dashboard.
2. In the **Resources** tab, I added the **Heroku PostgreSQL** add-on so the project could use Postgres in production.
3. In the **Settings → Config Vars**, I added all required environment variables:
   - `DATABASE_URL` (created automatically by Heroku Postgres)
   - `SECRET_KEY`
   ...
4. I connected my GitHub repository to Heroku in the **Deploy** tab and selected the main branch.
5. I clicked **Deploy Branch**, and Heroku built the Django project.
6. After the build completed, I ran the database migrations directly on Heroku:
   ```bash
   heroku run
   python manage.py migrate
   ```
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
[Back to Table of Contents](#table-of-contents)
---
## Conclusion

Pixel Store is a fully functional e-commerce platform for a fictional clothing brand.  
It combines a responsive, user-friendly design with secure and efficient functionality, including user authentication, shopping bag management, product browsing, and Stripe payment integration.  
The project demonstrates both front-end and back-end capabilities, testing practices, and attention to accessibility, providing a complete full-stack web application example.

### Trade-offs and Conscious Decisions
<details style="color:#007bff; padding:10px; border-radius:8px;">
  <summary><h3>🔟 Design Rationale</h3></summary>
  <ul>
    <li><strong>Sacrifices:</strong> visual design and marketing in favor of a solid and functional backend.</li>
    <li><strong>Omitted features:</strong> coupons, wishlist, reviews, advanced admin panel, and full E2E tests.</li>
    <li><strong>Maintainability decisions:</strong> clear app separation, use of context processors and signals, models with defined responsibilities, and clean template code.</li>
    <li><strong>Visual impact:</strong> consistent styles and promotional slides were used to compensate for the technical focus.</li>
  </ul>
  <p>The project reflects a priority on understanding, structure, and technical robustness over speed or aesthetics.</p>
</details>

### [Back to Table of Contents](#table-of-contents)
