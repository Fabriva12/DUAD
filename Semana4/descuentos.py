product_price=int (input("cual es el precio del producto"))
if (product_price<100):
    discount= product_price*0.02
else:
    discount=product_price*0.1
final_price= product_price-discount
print(f"el precio final es {final_price}")   
 