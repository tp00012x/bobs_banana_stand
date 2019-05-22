from django.conf import settings

from redis import Redis


class ProductStockManagement(object):
    """
    A cool class that deals with handling the redis data.
    """

    def __init__(self, order, db=0):
        self.order = order
        self.db = db
        self.redis_instance = Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=self.db)
        self.redis_stock = self.redis_instance.hgetall(self.order.product.id)

    @property
    def stock(self):
        return {key.decode('utf-8'): int(value.decode('utf-8')) for (key, value) in self.redis_stock.items()}

    def create_or_update_order_stock(self):
        self.redis_instance.hset(self.order.product.id, self.order.id, self.order.quantity)

    def update_redis_stock(self):
        self.redis_instance.hmset(
            self.order.product.id, self._calc_new_stock(list(self.stock.items()), self.order.quantity)
        )

    def deletes_order_stock(self):
        self.redis_instance.hset(self.order.product.id, self.order.id, 0)

    # TODO Need to work on renaming the variables use for readability
    def _calc_new_stock(self, d, c):
        """
        This recursive function iterates through my redis stock subtracting the sales order quantity from the purchased
        order quantity. It ignores the values with a value of zero.
        """
        [a, b], *_c = d
        return {a: 0 if c > b else b - c, **({} if not _c else self._calc_new_stock(_c, 0 if b > c else abs(b - c)))}
