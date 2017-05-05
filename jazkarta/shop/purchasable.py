from decimal import Decimal
from zope.component import adapter
from zope.interface import implementer
from .interfaces import IProduct
from .interfaces import IPurchaseHandler
from .utils import get_setting, resolve_uid
from jazkarta.shop.interfaces import IATProduct


@implementer(IPurchaseHandler)
@adapter(IProduct)
class DefaultPurchaseHandler(object):

    def __init__(self, context):
        self.context = context

    def in_stock(self):
        min_stock_level = get_setting('min_stock_level')
        if (self.context.stock_level is not None and
                self.context.stock_level < min_stock_level):
            return False
        return True

    def get_cart_items(self):
        return [{
            'uid': self.context.UID(),
            'name': self.context.title,
            'price': Decimal('{:.2f}'.format(self.context.price)),
            'quantity': 1,
            'category': self.context.product_category,
            'taxable': self.context.taxable,
            'weight': self.context.weight,
        }]

    def after_purchase(self, item):
        # Override this in a more specific adapter
        pass

    def get_obj_href(self, uid):
        obj = resolve_uid(uid)
        if obj is not None:
            return obj.absolute_url()


@implementer(IPurchaseHandler)
@adapter(IATProduct)
class DefaultArchetypesPurchaseHandler(object):

    def __init__(self, context):
        # MAKE COMPAT AT
        self.context = context

    def in_stock(self):
        # MAKE COMPAT AT
        import pdb; pdb.set_trace()
        min_stock_level = get_setting('min_stock_level')
        if (self.context.stock_level is not None and
                self.context.stock_level < min_stock_level):
            return False
        return True

    def get_cart_items(self):
        # MAKE COMPAT AT
        return [{
            'uid': self.context.UID(),
            'name': self.context.title,
            'price': Decimal('{:.2f}'.format(self.context.price)),
            'quantity': 1,
            'category': self.context.product_category,
            'taxable': self.context.taxable,
            'weight': self.context.weight,
        }]

    def after_purchase(self, item):
        # MAKE COMPAT AT?
        # Override this in a more specific adapter
        pass

    def get_obj_href(self, uid):
        # MAKE COMPAT AT
        obj = resolve_uid(uid)
        if obj is not None:
            return obj.absolute_url()
