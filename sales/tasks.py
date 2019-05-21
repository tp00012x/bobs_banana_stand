from bobs_banana_stand.celery import app


@app.task
def place_order(func, sale_order_id):
    print('Sale Order with an id {} was placed'.format(sale_order_id))
    return func

