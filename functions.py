#Functions for the nutrition app
#dict for data from the file
productList = {}


def file_open():
    """Opens the file, adds data into dict"""
    with open("Products.txt") as file:
        #split the words and add them to dictionary productList
        for row in file:
            if not row:
                continue
            else:
                product, values = row.split(',')
                productList[product] = values


def result(product, gram):
    """Calculates the nutritional values and returns result"""
    kcalValue = proteinValue = carbValue = fatValue = 0
    #check if user products are in the file
    if product in productList:
        (kcal, protein, carb, fat) = productList[product].split(':')
        #calculating the nutritional values
        kcalValue += gram / 100 * int(kcal)
        proteinValue += gram / 100 * int(protein)
        carbValue += gram / 100 * int(carb)
        fatValue += gram / 100 * int(fat)
        outcome = "Your product provided you with %d kcal, "\
           "%d protein, %d carbs oraz %d fat."\
           % (kcalValue, proteinValue, carbValue, fatValue)
    else:
        outcome = "Sorry, but we don't have this product in our database: %s, but you can add it! :)"% (product)
    return outcome











