# from django.db.models.signals import post_save
#
# from metrics.signals import MetricsSignals
#
#
# class MetricsSignals(object):
#
#     @staticmethod
#     def print_hello(sender, instance, **kwargs):
#         if kwargs.get('created'):
#             print('run signal when created')
#             print(sender)
#             print(instance)
#             print(instance.qty_purchased)
#             print('signal ends')
#         else:
#             print('run signal when updated')
#             print(sender)
#             print(instance)
#             print(instance.qty_purchased)
#             print('signal ends')
#
#
# post_save.connect(MetricsSignals.print_hello, sender=PurchasedOrder)
