import random

def get_numbers_ticket(min_num, max_num, quantity):

    if quantity > (max_num - min_num + 1):
        raise ValueError
    random_numbers = random.sample(range(min_num, max_num + 1), quantity)
    
    return random_numbers
ticket_numbers = get_numbers_ticket(1, 49, 6)
print(ticket_numbers)
