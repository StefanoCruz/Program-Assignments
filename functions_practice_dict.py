food_prices = {
"Chicken:$1.59", 
"Beef:$1.99",
"Cheese:$1.00",
"Milk:$2.50"
}
Wake_Up_Time = {
'Monday' : '7:00am',
'Tuesday' : '7:06am',
'Wednesday' : '8:00am',
'Thursday' : '7:30am'}
food_prices = {
'Chicken': 1.59, 
'Beef': 1.99,
'Cheese': 1.00,
'Milk': 2.50
}
chicken_price = food_prices['Chicken']
beef_price = food_prices['Beef']
cheese_prices = food_prices['Cheese']
milk_prices = food_prices['Milk']
monday_wake_up_time = Wake_Up_Time['Monday']
tuesday_wake_up_time = Wake_Up_Time['Tuesday']
wednesday_wake_up_time = Wake_Up_Time['Wednesday']
thurday_day_wake_up_time = Wake_Up_Time['Thursday']
shoe_inventory = { 'Jordan' : 1,
'Yeezy' :8,
'Foamposite' : 10,
'Air Max' : 5,
'SB Dunk' : 20
}
shoe_inventory['SB Dunk'] -= 2
shoe_inventory['Yeezy']+=1
shoe_inventory['Jordan']+= 7
shoe_inventory['Yeezy']+= 7
shoe_inventory['Foamposite']+= 7
shoe_inventory['Air Max']+= 7
shoe_inventory['SB Dunk']+= 7
shoe_inventory['Jordan'] -= 3
shoe_inventory['Yeezy'] -= 3
shoe_inventory['Foamposite'] -= 3
shoe_inventory['Air Max'] -= 3
shoe_inventory['SB Dunk'] -= 3
shoe_inventory['Vans']=8
shoe_inventory['Converse']=7
shoe_inventory['Adidas']=6
Wake_Up_Time['Friday']= '10:00am' 
Wake_Up_Time['Saturday']= '11:00am'
Wake_Up_Time['Sunday']= '12:00pm'
food_prices['Eggs'] = 1.20
food_prices['Bacon'] = 4.00
food_prices['Cereal'] = 2.00 
del shoe_inventory['Converse']
del shoe_inventory['Adidas']
del Wake_Up_Time['Friday']
del Wake_Up_Time['Saturday']
del food_prices['Beef']
del food_prices['Bacon']
#arithmetic operators
def total_price(food_item1, food_item2):
    total_price = food_prices[food_item1]+food_prices[food_item2]
    return total_price

print(total_price('Cheese','Cereal')) 

def price_difference(food_item1, food_item2):
    price_difference= food_prices[food_item1]-food_prices[food_item2]
    return abs(price_difference)

print(price_difference('Cheese','Cereal'))

def shoe_restock(shoe,num):
    shoe_inventory[shoe] *= num
    return shoe_inventory

print(shoe_restock('Yeezy',3))

def clearance_sale(shoe,num):
    shoe_inventory[shoe] //= num
    return shoe_inventory

print(clearance_sale('SB Dunk', 2))

def restock_alert(dict):
    smallest=5
    supply= ''

    for key in dict.keys():
        if dict[key]<=smallest:
            smallest=dict[key]
            supply = key
    return (supply,smallest)

print(restock_alert(shoe_inventory))