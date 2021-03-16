import string
import random

def random_string_generator(size=10,chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

# here we create order id used in order app for making id as random but also makes sence

def order_id_generator(instance):
    new_order_id=random_string_generator(size=8)
    klass=instance.__class__
    qset=klass.objects.filter(order_id=new_order_id)
    if qset.count() >= 1:
        new_order_id=order_id_generator(instance)
    return new_order_id
