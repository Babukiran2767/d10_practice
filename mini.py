class Product:
    def __init__(self,id,name,price,rating):
        self.id = id
        self.name = name
        self.price = price
        self.rating = rating
class User:
    def __init__(self):
        self.products = []

    def add_product(self):
        id = int(input('enter Procut ID:  '))
        for product in self.products:
            if product.id == id:
                print('prodcut with this ID is already Exist')
                return
        name = input('enter product name:  ')
        price = int(input('enter product price:  '))
        rating = float(input('enter product rating:  '))    
        product =Product(id,name,price,rating)
        self.products.append(product)
        print('product is successfully added..!')


    def remove_product(self):
        if len(self.products) == 0:
            print('no Product Available')
            return  
        id = int(input('enter Product ID:  '))  
        for product in self.products:
            if product.id == id:
                self.products.remove(product)
                print('Product is Removed Successfully')
                return
            print("Product with this is doesn't exist...!")


    def update_product(self):
        if len(self.products) == 0:
            print('No Products Available..!')
            return
        id = int(input('Enter Product ID:'))
        for product in self.products:
            if product.id == id:
                while True:
                 print('SELECT -> 1 TO UPDATE NAME')
                 print('SELECT -> 2 TO UPDATE PRICE')
                 print('SELECT -> 3 TO UPDATE RATING')
                 print('SELECT -> 4 TO UPDATE ALL DETAILS')
                 print('SELECT -> 5 TO PROCED WITH THE CHANGES')
                 
                 choice = int (input('Enter your choice:  '))
                 match choice:
                     case 1:
                         new_name = input ('Enter New Name')
                         product.name = new_name
                         print('Product Name is updated successfully..!') 
                     case 2:
                          new_price = input ('Enter New Price')
                          product.price = new_price 
                          print('Product price is updated successfully..!') 
                     case 3:
                          new_rating = float ('Enter New Rating')
                          product.rating = new_rating
                          print('Product rating is updated successfully..!') 
                     case  4:
                            new_name = input ('Enter New Name')   
                            new_price = input ('Enter New Price')
                            new_rating = float ('Enter New Rating')
                            product.name,product.price,product.rating = new_name,new_price,new_rating
                            print('All details updated successfully..!') 

                     case 5:
                         print('New changes reflected in your product ')
                         return
                     case _:
                         print('Invalid choice,Try Again...!')
                        

        print("Product with this ID doesn't exist...!")
    def show_products(self):
        if len(self.products) == 0:
            print('No Products Available..!')
            return
        
        print('|  ID  |  NAME  |  PRICE  |  RATING |')
        print('-'*38)
        for product in self.products:
            print(f'|  {product.id}  |  {product.name}  |  {product.price}  |  {product.rating}  |')
            print('-'*38)


    def search_product(self): 
            if len(self.products) == 0:
                print('No Products Available..!')
                return
            id = int(input('Enter Product ID:')) 
            for product in self.products:
                if product.id == id : 
                      print('-'*38)
                      print('|  ID  |  NAME  |  PRICE  |  RATING |')
                      print('-'*38)
                      print(f'|  {product.id}  |  {product.name}  |  {product.price}  |  {product.rating}  |')
                      print('-'*38)
                      return
                print("product with this id doesn't exist")

    def sort_price(self):
        if len(self.products) == 0:
                print('No Products Available..!')
                return
        
        self.products.sort(key=lambda product:product.price,reverse=False)
        print('product are sorted from low to high..!')

        
    def sort_rating(self):
        if len(self.products) == 0:
                print('No Products Available..!')
                return 
        self.products.sort(key=lambda product:product.rating,reverse=True)  
        print('product ratings are stored from high to low..!')


print(',----------PRODUCT MANAGEMENT SYSTEM --------->')
user = User()


while True:
    print('SELECT -> 1 TO ADD PRODUCT')
    print('SELECT -> 2 TO REMOVE PRODUCT')
    print('SELECT -> 3 TO UPDATE PRODUCT')
    print('SELECT -> 4 TO SHOW ALL PRODUCTS')
    print('SELECT -> 5 TO SEARCH A PRODUCT')
    print('SELECT -> 6 TO SORT PRODUCT PRICES')
    print('SELECT -> 7 TO SORT PRODUCT RATING')
    print('SELECT -> 8 TO EXIST FROM THE APP')

    choice =int(input('Enter your choice:'))
    match choice:
        case 1 : user.add_product()
        case 2 : user.remove_product()
        case 3 : user.update_product()
        case 4 : user.show_products()
        case 5 : user.search_product()
        case 6 : user.sort_price()
        case 7 : user.sort_rating()
        case 8:
            print('THANK YOU ,VISIT AGAIN')
            break
        case _:
             print('Invalid choice,Try Again...!')