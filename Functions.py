#dictionary for data from the file
productList = {}
#dictionary for user data
userList = {}


#open the file
def file_open():
   with open("Products.txt") as file:
         #split the words and add them to dictionary productList
         for row in file:
            if not row:
               continue
            else:
               product, values = row.split(',')
               productList[product] = values



#user defined variables goes here
def add_product(product, gram):
   userList[product] = gram


def result():
   kcalValue = proteinValue = carbValue = fatValue = 0
   #check if user products are in the file
   for food in userList:
      if food in productList:
         (kcal, protein, carb, fat) = productList[food].split(':')
         #calculating the nutritional values
         kcalValue += int(userList[food]) / 100 * int(kcal)
         proteinValue += int(userList[food]) / 100 * int(protein)
         carbValue += int(userList[food]) / 100 * int(carb)
         fatValue += int(userList[food]) / 100 * int(fat)
         outcome = "Your product provided you with %d kcal, "\
         "%d protein, %d carbs oraz %d fat."\
         % (kcalValue, proteinValue, carbValue, fatValue)
      else:
         outcome = "Sorry, but we don't have this product in our database: %s, but you can add it! :)"% (food)
   return outcome










