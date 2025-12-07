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
2. [Wireframes](#wireframes)
3. [The Logo](#the-logo)
4. [Colors](#colors)
5. [UI/UX Screenshots](#uiux-screenshots)
6. [Installation](#installation)
7. [Data Model](#1-data-model)
8. [Backend and Testing](#backend-and-testing)
9. [Problems & Solutions](#problems--solutions)
10. [Code Example](#code-example)
11. [functions and testing](#the-functions-and-their-testing-on-the-pixel-store-app)
12. [Pytest](#testing)
13. [pep8 & black](#code-quality-pep8--linters)
14. [Environment Variables ``(.env)``](#environment-variables-env)
15. [Deployment](#deployment)

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

## - Git & Version Control  
![Website Preview](./wireframes/pixel_diagram.jpg)

- Version control was managed using **Git** and hosted on **GitHub**.  
- The project was mainly developed on the **main branch**, with **frequent commits** documenting progress.  
- Clear commit messages (e.g., *added checkout logic*, *fixed product model bug*) were used to track changes.  
- GitHub was also used for deployment to **Heroku**, ensuring smooth version tracking and project backup.  
- The project was initially started using **Django Allauth**, inspired by the e-commerce tutorial video from the course, providing a foundation for user authentication and registration.  
- Custom **context_processors.py** were added to Pixel Store apps to manage shared data across templates, improving code reusability and ensuring dynamic content (e.g., shopping bag contents, product categories) was consistently available.

[Comeback Index](#pixel-store)
---
# 1. Data Model 
# 🗄
Describes the data model used in the Pixel Store application, including all entities and relationships between them.

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
[Comeback Index](#pixel-store)
---
### What is it and what is it for?
This documentation summarizes the main files in each Pixel Store app:  
- **views.py** → handles the business logic and response to HTTP requests (renders templates, processes forms, manages sessions, etc.)  
- **context_processors.py** → injects common variables into templates (like timestamps, shopping bag contents, categories)  
- **signals.py** → automatically executes functions in response to model events (like creating UserProfiles or loading BagItems on login)  


# The functions and their testing on the Pixel Store app
Use the links below to explore each file’s purpose and its corresponding tests.

## home
- ### [views.py](/docs/apps%20README/home/views_README.md)🟢
  >``home/views.py`` renders the main pages: ``index`` with timestamp, ``faqs``, and ``about``.
- ### [context_processors.py](/docs/apps%20README/home/context_processors_README.md)🟢
  >``home/context_processors.py`` provides a ``timestamp`` context processor, making the current timestamp available in all templates.
  - ### [test](/docs/test%20README/home_README.md)🛑
    >``home/tests/`` verifies views and context processors: pages return 200, correct templates are used, and ``timestamp`` is present and an integer in all templates.

## products
- ### [views.py](/docs/apps%20README/products/views_README.md)🟢
  >``products`` app defines ``Category`` and ``Product`` models, and provides views for listing products (with optional category filter), searching by name, and displaying individual product details, all rendered with Jinja templates.
- ### [context_processors.py](/docs/apps%20README/products/context_processors_README.md)🟢
  >``products/context_processors.py`` provides ``get_categories``, making all product categories available in templates for navigation or filtering.
  - ### [test](/docs/test%20README/products_README.md)🛑
    >``products/tests/`` verifies the ``Category`` model and ``get_categories`` context processor: the model’s ``__str__`` returns the category name, and the context processor provides a list of categories in templates.

## users
- ### [views.py](/docs/apps%20README/users/views_README.md)🟢
  >``users`` app manages user accounts: ``register`` handles signup and creates a ``UserProfile``, ``profile_view`` displays and edits account and profile info, and ``my_orders`` lists the user’s orders.
- ### [signals.py](/docs/apps%20README/users/signals_README.md)🟢
  >``users/signals.py`` listens to ``User`` model changes and automatically creates or updates a ``UserProfile`` whenever a user is created or saved.
  - ### [test](/docs/test%20README/users_README.md)🛑
    >``users/tests/`` verifies user-related functionality: profile page access and template rendering, ``UserProfile`` string representation, and that ``UserProfileForm`` includes all expected fields.

## bag
- ### [views.py](/docs/apps%20README/bag/views_README.md)🟢
  >``bag`` app manages the shopping bag: ``view_bag`` displays items with totals, ``add_to_bag`` adds or updates items via POST/AJAX, ``remove_from_bag`` deletes items, and ``clear_bag`` empties the bag for the user.
- ### [context_processors.py](/docs/apps%20README/bag/context_processors_README.md)🟢
  >``bag/context_processors.py`` provides ``bag_contents`` and ``calculate_bag_total``, making the current shopping bag items, counts, and totals available in all templates.
- ### [signals.py](/docs/apps%20README/bag/signals_README.md)🟢
  >``bag/apps.py`` activates signals on app ready, and ``bag/signals.py`` automatically loads a logged-in user’s ``BagItems`` into the session, reconstructing the shopping bag.
  - ### [test](/docs/test%20README/bag_README.md)🛑
    >``bag/tests/`` verifies shopping bag functionality: pages return 200 and use correct templates, add/remove/clear actions update session and redirect properly, URLs resolve correctly, and context processors calculate totals, counts, and bag items accurately.

## checkout
- ### [views.py](/docs/apps%20README/checkout/views_README.md)🟢
  >``checkout/`` handles order processing: displays checkout form if the bag isn’t empty, validates and saves orders and line items, creates a Stripe checkout session, empties the bag, and shows a success page with order details.
  - ### [test](/docs/test%20README/checkout_README.md)🛑
    >checkout/tests/ verifies the checkout flow: redirects when the bag is empty, ensures checkout success page loads correctly, confirms order numbers are auto-generated, and validates the OrderForm with correct data.

# 📱 User Experience (UX) — Pixel Store
After creating an account, the user can:

- Browse products and filter by category
- Search products by name
- View product details
- Add, update, or remove items in the shopping bag
- Proceed to checkout and complete orders
- View order history in their profile
- Edit account and shipping information

[Comeback Index](#pixel-store)
---
## CRUD Features – Pixel Store

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

### 4. Information Pages
- Users can explore the About page.
<img src="./screenshots/CRUDs/4-about.jpeg" alt="Website Preview" width="300">
- The Footer includes useful links such as FAQs.
<img src="./screenshots/CRUDs/4-FAQs.jpeg" alt="Website Preview" width="300">

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

### 7. Shopping Bag
- Users can:
  - Review their selected items
  - Remove items
  - View the subtotal
  - See delivery costs
  
  <img src="./screenshots/CRUDs/6-bag.jpeg" alt="Website Preview" width="300">

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

##  Problems & Solutions
# ❗

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

### Problem:
- Database `makemigrations` failed due to wrong plural naming.

### Solution:
- Added `verbose_name_plural = "Categories"` inside Meta class.
## Testing
# 🧪 

Tests were run using **pytest** in a Django environment.

<img src="./screenshots/CRUDs/pytest.png" alt="Website Preview" width="500">

### Summary

- ✅ 22 tests passed
- ❌ 2 tests failed
- ⏭ 1 test skipped
- ⚠️ 9 warnings

### Example failed tests

1. `bag/tests/test_views.py::BagViewsTestCase::test_add_to_bag`
   - Error: UnboundLocalError — variable `product` not defined.

2. `users/tests/test_forms.py::UserFormsTests::test_userprofile_form_fields`
   - Error: AssertionError — form fields do not match expected list.

[Comeback Index](#pixel-store)
---
## Code Quality: PEP8 & Linters
# 🧹

To keep the **Pixel Store** project clean, consistent, and professional, PEP8 style guidelines were applied together with Python linters.

### ⭐ Why this was done
- To maintain a consistent coding style across the project.
- To reduce common mistakes before running the application.
- To improve readability and long-term maintainability.
- To follow industry best practices used in real software projects.

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

[Comeback Index](#pixel-store)
---
## Environment Variables (.env)
# 🔐

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

[Comeback Index](#pixel-store)
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
[Comeback Index](#pixel-store)
---