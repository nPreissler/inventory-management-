# 1 - Adição de produtos
# -- 1.1 - Adição de mais de um produto
# -- 1.2 - ID generativo
# -- 1.3 - Quantidade do produto
# 2 - Pesquisa de produto
# -- 2.1 - Pesquisa por ID
# -- 2.2 - Pesquisa Filtrada por letras que as palavras contém
# 3 - Remoção de produtos
# -- 3.1 - Remoção de mais de um produto
# -- 3.2 - Remoção por ID
# 4 - Desligamento do programa

# -- Todas as operações devem ter como ser canceladas a qualquer momento

from models.product import Product
import os
import time


def add_product():
    os.system('cls')
    time.sleep(1)
    
    print('To go back to menu click "L"\n')
    name = input('--> ')
    
    null_field(name)
    leave_to_menu(name)
    
    quantity = input('Quantity you want add: ')
    null_field(quantity)
    
    product = Product(name, quantity, '0')
    stock.append(product)
    
    os.system('cls')

    print('Now the product(s) is in the stock:\n ')
    time.sleep(1)
    for i in stock:
        print(i)
        
    time.sleep(3)
    os.system('cls')
    return menu()

def leave_to_menu(input_value):
    if input_value == 'l' or input_value == 'L':
        os.system('cls')
        time.sleep(1)
        menu()

def null_field(input_value):
    if input_value == '':
        os.system('cls')
        
        print('This field cannot be null')
        
        time.sleep(3)
        return menu()

def search_product():
    os.system('cls')
    time.sleep(1)
    
    print('Search for products or type "L" to back to menu \n')
    search = input('--> ')
    
    null_field(search)
    leave_to_menu(search)
    
    found_product = None

    for product in stock:
        if product._product.lower() == search.lower():
            found_product = product
            break

    if found_product:
        print(f'\nThe product "{search}" was found:\n{found_product}')
    else:
        print(f'\nThe product "{search}" was not found')

    time.sleep(3)
    menu()

def delete_product():
    os.system('cls')
    time.sleep(1)
    
    print('Type the name of the product you want to delete or click "L" to leave')
    delete = input('--> ')
    
    null_field(delete)
    leave_to_menu(delete)

    found_product = None

    for product in stock:
        if product._product.lower() == delete.lower():
            found_product = product
            break

    if found_product:
        stock.remove(found_product)
        print(f'The product "{delete}" was deleted.')
    else:
        print(f'The product "{delete}" was not found in the stock.')
    
    time.sleep(3)
    menu()
    
def shutdown():
    while True:
        os.system('cls')
        print('Turning off...')
        time.sleep(3)
        break

stock = []


def menu():
    os.system('cls')
    print('Type the number what corresponds to option you want select\n')
    print('1 - Add products')
    print('2 - Search for products')
    print('3 - Delete products')
    print('4 - End application\n')
    
    option = input('--> ')
    
    match option:
        case '1':
            add_product()
        case '2':
            search_product()
        case '3':
            delete_product()
        case '4':
            shutdown()


menu()
