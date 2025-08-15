import sqlite3

from datetime import datetime #[Online][https://ioflood.com/blog/python-datetime-to-string/#:~:text=In%20this%20example%2C%20we've,HH%3AMM%3ASS'.Accessed[20 March 2024]

class Store:
    def __init__(self):
        self.conn = sqlite3.connect(r"C:\Users\hamza\OneDrive\Documents\ClaasWork ITAPA\ITAPA Project 1 (Hamzah Suleman-EDUV3475589)\Question 1\Stock.db")
        self.cursor = self.conn.cursor()
        #[Online][https://mylms.vossie.net/mod/book/view.php?id=416947&chapterid=704879]Accessed[15 March 2024]
    def addProduct(self):  
        ProductName = input("Please enter the name of the product: ")  
        Price = input("Please enter the price of the product: ")
        Quantity = input('Please enter the quantity for the product: ')
        self.cursor.execute("INSERT INTO Product (\"Product Name\", \"Product Price\", \"Product Quantity\") VALUES (?, ?, ?)", (ProductName, Price, Quantity))
        self.conn.commit() 
    #[Online][https://mylms.vossie.net/mod/book/view.php?id=416947&chapterid=704881]Accessed[15 March 2024]
    def removeProduct(self):
        ID=int(input("Enter the product ID to remove the product: "))
        self.cursor.execute('DELETE FROM Product WHERE "Product ID" = ?', (ID,))
        self.conn.commit()
      #[Online][https://mylms.vossie.net/mod/book/view.php?id=416947&chapterid=704880]Accessed[15 March 2024]  
    def updateProduct(self):
        ID = int(input("Enter the product ID to update: "))
        ProductName = input("Enter the new name of the product: ")
        Price = input("Enter the new price of the product: ")
        Quantity = input('Enter the new quantity for the product: ')
        self.cursor.execute('UPDATE Product SET "Product Name" = ?, "Product Price" = ?, "Product Quantity" = ? WHERE "Product ID" = ?', (ProductName, Price, Quantity, ID))
        self.conn.commit()

    def displayProducts(self):
        self.cursor.execute('SELECT * FROM Product')
        products = self.cursor.fetchall()
        for product in products:
            print(product)    

    def sellProduct(self):
        ID = int(input("Enter the product ID to sell: "))
        SaleQuantity = int(input("Enter the quantity to sell: "))
        
        self.cursor.execute('SELECT "Product Quantity", "Product Name","Product Price" FROM Product WHERE "Product ID" = ?', (ID,))
        product = self.cursor.fetchone()

        if product:
            product_quantity, product_name, product_price = product
            
            if product_quantity >= SaleQuantity:
            
                new_quantity = product_quantity - SaleQuantity
                self.cursor.execute('UPDATE Product SET "Product Quantity" = ? WHERE "Product ID" = ?', (new_quantity, ID))
                self.conn.commit()

              
                saleTotal = int(product_price) * SaleQuantity
                
           #[Online][https://ioflood.com/blog/python-datetime-to-string/#:~:text=In%20this%20example%2C%20we've,HH%3AMM%3ASS'.]Accessed[20 March 2024]
                saleDate = datetime.now().strftime('%Y-%m-%d')
                self.cursor.execute('INSERT INTO Sales ("Sale Date", "Product Name","Sale Total") VALUES (?, ?, ?)', (saleDate, product_name, saleTotal))
                self.conn.commit()
                
                print(f"{SaleQuantity} units of {product_name} sold successfully.")
            else:
                print("Insufficient quantity in stock.")
        else:
            print("Product not found.")

store = Store()
#[Online][https://www.freecodecamp.org/news/python-do-while-loop-example/]Accessed[20 March 2024]
while True:
    print("------WELCOME TO THE STORE MANAGEMENT SYSTEM------")
    print("1. ADD PRODUCT")
    print("2. REMOVE PRODUCT")
    print("3. UPDATE PRODUCT")
    print("4. DISPLAY PRODUCT")
    print("5. SELL PRODUCT")
    print("6. Exit\n")

    choice = int(input("Please enter your choice: "))

    if choice == 1:
        store.addProduct()
    elif choice == 2:
        store.removeProduct()
    elif choice == 3:
        store.updateProduct()
    elif choice == 4:
        store.displayProducts()
    elif choice == 5:
        store.sellProduct()
    elif choice == 6:
        print("Exiting. Thank you")
        break
    else:
        print('Enter valid option')
store.conn.close()