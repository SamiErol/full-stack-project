# Fitness World (https://sami-fitness-world.herokuapp.com/)

Fitness World is an e-commerce store with a focus towards the fitness fanatics. Offering clothes, accessories and equipment by means of our trendy website, users get an intuitive experience right down to ordering.
 
## UX
 
This website was designed to be familiar. We did not want to disturb the user with unneccesary structures. The mobile layout is seemless and it organically expands for tablet and desktop users.

User stories:
- As a shopper, I want to be able to browse products, so I may buy if I intend.
- As a shopper, I want to be able to browse product details, so I may buy/view more product information.
- As a shopper, I want to be able to instantly find promotional items, so I may buy if I intend.
- As a shopper, I want to be view my cart balance, so I'm aware of what my bag total is.
- As a shopper, I want to be create an account, so that I can provide my information for future orders and manage my details and view orders.
- As a shopper, I want to be able to log in/out, so I may securely access my account.
- As a shopper, I want to be able to browse products, so I may buy if I intend.
- As a shopper, I want to be able to filter products, so I may customize how products are ordered/displayed.
- As a shopper, I want to be able to browse categories of products, so I can narrow down the products I'm interested in.
- As a shopper, I want to be able to browse products, so I may buy if I intend.
- As a shopper, I want to be able to search for products, so I find exactly the product I need.
- As a shopper, I want to be able to select quantity when adding a product to my bag, so I may buy the exact quantity I need.
- As a shopper, I want to be able to view products in my bag before checkout, to review what I am about to order.
- As a shopper, I want to be able to adjust products quantity in my bag, incase I want more/less of that product.
- As a shopper, I want to be able to seemlessly enter my payment information, so I may check out quickly.
- As a shopper, I want my payment details to be secure, so I feel safe about purchasing.
- As a shopper, I want to view an order confirmation, so I'm assured my order is placed and I can see my details entered.
- As a store owner, I want to be able to add products, when new items become available.
- As a store owner, I want to be able to update/edit products, incase I need to modify any criteria.
- As a store owner, I want to be able to delete products, when they are out of stock.



UI Mockups: https://wireframepro.mockflow.com/view/Ma9bd9ca12ef979ebb50e386d648cf4121610848278387
 
### Features Highlight
- Provided an intuitive fully featured e-commerce site
- Seperation of access for admins to allow control
- Integrated payments using stripe API

### Features Left to Implement
- Fully implement the email functionality, so users receive an email as prompted after order

## Technologies Used

- [Python](https://python.org)
    - Used throughout for its highly efficient data structures and approach to OOP.
- [Django](https://www.djangoproject.com/)
    - A high-level Python Web framework.
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
    - Used in providing a scripting language for various web pages.
- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
    - HTML is the standard markup language for creating Web pages and was used in view creation.
- [CSS](https://www.w3.org/Style/CSS/Overview.en.html)
    - Used to add style to my web documents
- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.
- [PostGres](https://www.postgresql.org/)
    - An open source relational database, used to store data in my hosted project.
- [Heroku](https://www.heroku.com/)
    - A web hosting platform used for a lot of languages. Hosts my project.
- [AWS](https://aws.amazon.com/about-aws/)
    - A scalable, cloud platform. Used in my project for hosting static and media files.
- [Stripe](https://stripe.com/)
    - Provides a payment infrastructure for the internet. Served my application through its API.

## Testing

- Manual testing was carried out to ensure user stories did not vary from what was expected.
- Testing consisted of completing said stories in all fashions possible (various browsers, on mobile + desktop)
- Note: Internet Explorer is not fully supported. Payment with Stripe failed to complete.

## Deployment
(Initially)
- Migrate database from default to postgres after creating heroku app.
- Install necessary apps in django server.
- Migrate config vars to heroku (stripe keys etc.)
- Load data to new database
- In AWS, create S3 bucket, setup IAM permissions.

(New deployments)
- Within GitPod, ensure latest changes are committed to GitHub.
- Push committed changes to heroku.

## Credits
- https://github.com/ckz8780

### Content
- The content for various sections was taken from https://github.com/ckz8780/boutique_ado_v1