from order.models import Order
from addresses.models import Address

# script for address duplicate removal with safety
def adr():
    d = {}
    delete_list=[]
    for x in Order.objects.all():
        if x is not None:
            # print(d)
            add_obj = None
            if x.ship_add is not None:
                if x.ship_add.add_line_1 in d.keys():
                    key1 = x.ship_add.pk
                    x.ship_add = Address.objects.get(pk=d[x.ship_add.add_line_1]) 
                    delete_list.append(key1)
                    x.save()
                else:
                    d[x.ship_add.add_line_1] =  x.ship_add.pk
            if x.bill_add is not None:
                if x.bill_add.add_line_1 in d.keys():
                    key2 = x.bill_add.pk
                    x.bill_add = Address.objects.get(pk=d[x.bill_add.add_line_1]) 
                    delete_list.append(key2)
                    x.save()
                else:
                    d[x.bill_add.add_line_1] =  x.bill_add.pk
    print(delete_list)
    for i in delete_list:
        Address.objects.get(pk=i).delete()