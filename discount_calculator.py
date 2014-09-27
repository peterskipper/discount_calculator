def calculate_discount(item_cost, relative_discount, absolute_discount):
    """Takes an item price and discount sizes, returns discounted price"""
    #Check inputs
    try:
        percent_discount = (relative_discount + absolute_discount) / 100.0
    except TypeError:
        print "item_cost, relative_discount and absolute_discount must be numbers"
        return
    if item_cost <= 0:
        raise ValueError("Item must cost more than $0")
        return
    if relative_discount < 0 or absolute_discount < 0:
        raise ValueError("Discounts must be greater than or equal to zero")
        return
    if relative_discount + absolute_discount >= 100:
        raise ValueError("Total discount cannot be greater than or equal to 100%")
        return
    if relative_discount == 0 and absolute_discount == 0:
        raise ValueError("At least one discount must be above zero")
    if relative_discount > 0 and relative_discount < 1:
        resp = raw_input("Relative discount should be entered as a percent. Did you intend to have a {:.2f} percent relative discount (y/n)? ".format(relative_discount))
        if resp.lower() not in ['y', 'yes']:
            return
    if absolute_discount > 0 and absolute_discount < 1:
        resp = raw_input("Absolute discount should be entered as a percent. Did you intend to have a {:.2f} percent absolute discount (y/n)? ".format(absolute_discount))
        if resp.lower() not in ['y', 'yes']:
            return
    return item_cost - item_cost * percent_discount #discounted cost
