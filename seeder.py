
from ecommerce.models import User,Category,Product
from ecommerce import db,create_app
from sqlalchemy.exc import SQLAlchemyError


app = create_app()


def seed_db():
    with app.app_context():
        # Create categories
        categories = [
            Category(name='Electronics', description='Electronic items'),
            Category(name='Clothing', description='Men and Women Clothing'),
            Category(name='Books', description='Books and Stationery'),
            Category(name='Home & Kitchen', description='Home appliances and kitchen items'),
            Category(name='Sports & Outdoors', description='Sports and outdoor equipment'),
            Category(name='Health & Beauty', description='Health and beauty products'),
            Category(name='Toys & Games', description='Toys and games for kids and adults'),
            Category(name='Automotive', description='Automotive parts and accessories')
        ]

        for category in categories:
            db.session.add(category)
        db.session.commit()

        # Create products
        products = [
            Product(name='Laptop', description='A high-performance laptop.', price=99999.99, discount_price=89999.99,
                    stock=50, image_url='https://ke.jumia.is/unsafe/fit-in/300x300/filters:fill(white)/product/31/9619752/1.jpg?2814', category_id=categories[0].id),
            Product(name='Smartphone', description='Latest model smartphone.', price=79999.99, discount_price=69999.99,
                    stock=100, image_url='https://ke.jumia.is/unsafe/fit-in/500x500/filters:fill(white)/product/33/1880971/1.jpg?6409', category_id=categories[0].id),
            Product(name='Jeans', description='Comfortable blue jeans.', price=4999.99, discount_price=3999.99,
                    stock=200, image_url='https://ke.jumia.is/unsafe/fit-in/300x300/filters:fill(white)/product/30/559218/1.jpg?3307', category_id=categories[1].id),
            Product(name='T-shirt', description='Casual t-shirt.', price=1999.99, discount_price=1499.99,
                    stock=150, image_url='https://ke.jumia.is/unsafe/fit-in/300x300/filters:fill(white)/product/16/9662661/1.jpg?5554', category_id=categories[1].id),
            Product(name='Novel', description='Bestselling novel.', price=2499.99, discount_price=1999.99,
                    stock=300, image_url='https://ke.jumia.is/unsafe/fit-in/500x500/filters:fill(white)/product/07/9472412/1.jpg?6690', category_id=categories[2].id),
            Product(name='Notebook', description='College ruled notebook.', price=599.99, discount_price=499.99,
                    stock=500, image_url='https://ke.jumia.is/unsafe/fit-in/500x500/filters:fill(white)/product/24/608803/1.jpg?3660', category_id=categories[2].id),
            Product(name='Blender', description='High-speed blender.', price=9999.99, discount_price=8999.99,
                    stock=75, image_url='https://ke.jumia.is/unsafe/fit-in/500x500/filters:fill(white)/product/16/5954321/1.jpg?2626', category_id=categories[3].id),
            Product(name='Coffee Maker', description='Automatic coffee maker.', price=4999.99, discount_price=3999.99,
                    stock=120, image_url='https://ke.jumia.is/unsafe/fit-in/680x680/filters:fill(white)/product/12/4541221/1.jpg?9837', category_id=categories[3].id),
            Product(name='Tennis Racket', description='Professional tennis racket.', price=7999.99, discount_price=6999.99,
                    stock=90, image_url='https://ke.jumia.is/unsafe/fit-in/300x300/filters:fill(white)/product/69/221803/1.jpg?6490', category_id=categories[4].id),
            Product(name='Running Shoes', description='Lightweight running shoes.', price=5999.99, discount_price=4999.99,
                    stock=180, image_url='https://ke.jumia.is/unsafe/fit-in/300x300/filters:fill(white)/product/51/5410871/1.jpg?8518', category_id=categories[4].id),
            Product(name='Shampoo', description='Herbal shampoo for healthy hair.', price=1299.99, discount_price=999.99,
                    stock=250, image_url='https://ke.jumia.is/unsafe/fit-in/300x300/filters:fill(white)/product/56/332305/1.jpg?2780', category_id=categories[5].id),
            Product(name='Face Cream', description='Anti-aging face cream.', price=2999.99, discount_price=2499.99,
                    stock=130, image_url='https://www.jumia.co.ke/generic-hakuna-matata-sun-protective-face-and-body-cream-189819070.html', category_id=categories[5].id),
            Product(name='Board Game', description='Fun and exciting board game.', price=3499.99, discount_price=2999.99,
                    stock=70, image_url='https://ke.jumia.is/unsafe/fit-in/300x300/filters:fill(white)/product/84/4526102/1.jpg?8054', category_id=categories[6].id),
            Product(name='Action Figure', description='Collectible action figure.', price=1999.99, discount_price=1499.99,
                    stock=220, image_url='https://ke.jumia.is/unsafe/fit-in/300x300/filters:fill(white)/product/94/5261771/1.jpg?3488', category_id=categories[6].id),
            Product(name='Car Tire', description='All-season car tire.', price=9999.99, discount_price=8999.99,
                    stock=40, image_url='https://www.jumia.co.ke/generic-car-tires-with-wheel-rims-4pcs-replacement-for-110-losi-121464632.html', category_id=categories[7].id),
            Product(name='Car Wax', description='High-quality car wax.', price=1499.99, discount_price=999.99,
                    stock=60, image_url='https://ke.jumia.is/unsafe/fit-in/300x300/filters:fill(white)/product/57/291575/1.jpg?3461', category_id=categories[7].id),
          
            Product(name='Tablet', description='High-resolution tablet.', price=49999.99, discount_price=44999.99,
                    stock=70, image_url='https://www.jumia.co.ke/c-idea-10-inches-android-12-sim-8gb512gb-storage-keyboard-adults-tablet-pcgreen-160566753.html', category_id=categories[0].id),
            Product(name='Headphones', description='Noise-cancelling headphones.', price=19999.99, discount_price=14999.99,
                    stock=85, image_url='https://ke.jumia.is/unsafe/fit-in/300x300/filters:fill(white)/product/14/056876/1.jpg?1786', category_id=categories[0].id),
            Product(name='Jacket', description='Warm winter jacket.', price=8999.99, discount_price=7999.99,
                    stock=110, image_url='https://ke.jumia.is/unsafe/fit-in/300x300/filters:fill(white)/product/30/544157/1.jpg?0676', category_id=categories[1].id),
            Product(name='Sneakers', description='Fashionable sneakers.', price=7999.99, discount_price=6999.99,
                    stock=150, image_url='https://ke.jumia.is/unsafe/fit-in/300x300/filters:fill(white)/product/50/5410871/1.jpg?8518', category_id=categories[1].id),
            Product(name='Cookbook', description='Delicious recipes cookbook.', price=2999.99, discount_price=2499.99,
                    stock=200, image_url='https://ke.jumia.is/unsafe/fit-in/300x300/filters:fill(white)/product/01/4444481/1.jpg?4775l', category_id=categories[2].id),
            Product(name='Desk Lamp', description='Adjustable desk lamp.', price=2499.99, discount_price=1999.99,
                    stock=140, image_url='https://ke.jumia.is/unsafe/fit-in/300x300/filters:fill(white)/product/76/7780732/1.jpg?0752', category_id=categories[3].id),
            Product(name='Yoga Mat', description='Non-slip yoga mat.', price=3999.99, discount_price=3499.99,
                    stock=130, image_url='https://ke.jumia.is/unsafe/fit-in/300x300/filters:fill(white)/product/99/6880961/1.jpg?3385', category_id=categories[4].id),
            Product(name='Perfume', description='Long-lasting perfume.', price=4999.99, discount_price=4499.99,
                    stock=190, image_url='https://ke.jumia.is/unsafe/fit-in/300x300/filters:fill(white)/product/61/035476/1.jpg?3111', category_id=categories[5].id),
        ]

        for product in products:
            db.session.add(product)

        try:
            db.session.commit()
            print("Database seeded!")
        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"Error: {str(e.__dict__['orig'])}")
        
        


seed_db()

