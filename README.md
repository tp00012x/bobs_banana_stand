# Bob's Banana Stand

This application let's Bob (Bobby 'the machine') keep track of his purchases and sales while also being able to tell how 
much money he has made selling his bananas, and how much in stock he has left.

## Getting Started

Clone this repo anywhere where you desire.

### Installing

1. Install Brew
    ```
    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    ```

2. Make sure to have Python 3 installed
    ```
    brew install python
    ```
3. Install Virtual env

    ```
    pip install virtualenv
    ```

4. Install Redis
    ```
    brew install redis
    ```

### Set up

1. Locate the bobs_banana_stand folder in your computer and cd into it by typing the following in terminal:
    ```
    cd bobs_banana_stand
    ```
    
2. Create a Virtual Environment
    ```
    virtualenv -p python3 bobs_banana_stand
    ```
    
3. Activate Virtual Env
    ```
    source bobs_banana_stand/bin/activate
    ```
    
4. Install requirements:
    ```
    python -m pip install -r requirements.txt
    ```

## Running application locally
1. Make migrations
    ```
    python manage.py make migrations
    ```
    
2. Run migrate
    ```
    python manage.py make migrate
    ```

3. Run Celery Worker
    ```
    celery -A bobs_banana_stand worker -l info
    ```

4. Run Celery scheduler
    ```
    celery -A bobs_banana_stand beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
    ```
    
## API Instructions

1. Navigate to *http://localhost:8000/suppliers/*, and create a Supplier by adding its name.

2. Navigate to *http://localhost:5000/products/*, and create the Banana product.

3. Navigate to *http://localhost:5000/purchased_orders/*, and start creating purchased orders for the product you just created.
    
    These purchased orders will represent your banana purchases
    
4. in the same way Navigate to *http://localhost:5000/sales_orders/*, to start placing orders.

    When you crease Sale Orders, you will automatically update the stock of the product you selected.
    
## Additional information

1. To deal with expired products, I've created a task using django and celery to schedule a task that will run daily to
check if a product is expired. If it's expired, the products stock for that purchased order will be set to zero, and
therefore you won't be able to set these purchased orders of bananas.

2. Redis was used to handle the stock calculation behind scenes. They work in hand with signals when save and delete
methods are triggered.

    - To access the stock using redis run:
        ```
        redis-server
        ```
        And,
        ```
        redis-cli
        ```
        
    - Then, you can run:
    
        ```
        hgetall 1
        ```
        
        To get all the purchased products' stock for product 1.

3. This application supports the creation of multiple products. Perhaps, Bobby in the future wants to sell Apples or
other products

## Authors
**Anthony P Torres**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Thank you to Bob for is great initiative of starting his banana business.
