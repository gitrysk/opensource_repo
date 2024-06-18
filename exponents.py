
def num_power(num1, exponent):
    product = int(num1)
    for i in range(exponent-1):
        product = product * num1
    return product
