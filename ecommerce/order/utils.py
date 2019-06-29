import string
import random

def order_id_generator(instance):
    n_id=random_generator()
    k=instance.__class__
    q=k.objects.filter(order_id=n_id).exists()
    print(q)
    if q:
        return order_id_generator(instance)
    return n_id

def random_generator(size=12,chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for _ in range(size))