price = 100
discount = 20

def apply_discount(price, discount):
    if not isinstance(price, (int, float)):
        return 'The price should be a number'
    elif not isinstance(discount, (int, float)):
        return 'The discount should be a number'
    elif price <= 0:
        return 'The price should be greater than 0'
    elif discount < 0 or discount > 100:
        return 'The discount should be between 0 and 100'
    else:
        pass

    discount_decimal = discount / 100
    final_price = price - (price * discount_decimal)
    
    if discount == 100:
        return 0
    else:
        return final_price

    print(final_price)
    
apply_discount(price, discount)