food_prices = {
"Chicken:$1.59", 
"Beef:$1.99",
"Cheese:$1.00",
"Milk:$2.50"
}
print(food_prices)
Wake_Up_Time = {
'Monday' : '7:00am',
'Tuesday' : '7:06am',
'Wednesday' : '8:00am',
'Thursday' : '7:30am'}
print(Wake_Up_Time)
food_prices = {
'Chicken': '$1.59', 
'Beef': '$1.99',
'Cheese': '$1.00',
'Milk': '$2.50'
}
chicken_price = food_prices['Chicken']
print(chicken_price)
beef_price = food_prices['Beef']
cheese_prices = food_prices['Cheese']
milk_prices = food_prices['Milk']
print(beef_price)
print(cheese_prices)
print(milk_prices)
monday_wake_up_time = Wake_Up_Time['Monday']
print(monday_wake_up_time)
tuesday_wake_up_time = Wake_Up_Time['Tuesday']
wednesday_wake_up_time = Wake_Up_Time['Wednesday']
thurday_day_wake_up_time = Wake_Up_Time['Thursday']
print(tuesday_wake_up_time)
print(wednesday_wake_up_time)
print(thurday_day_wake_up_time)
shoe_inventory = { 'Jordan' : 1,
'Yeezy' :8,
'Foamposite' : 10,
'Air Max' : 5,
'SB Dunk' : 20
}
print(shoe_inventory)
shoe_inventory['SB Dunk'] -= 2
shoe_inventory['Yeezy']+=1
print(shoe_inventory)
shoe_inventory['Jordan']+= 7
shoe_inventory['Yeezy']+= 7
shoe_inventory['Foamposite']+= 7
shoe_inventory['Air Max']+= 7
shoe_inventory['SB Dunk']+= 7
print(shoe_inventory)
shoe_inventory['Jordan'] -= 3
shoe_inventory['Yeezy'] -= 3
shoe_inventory['Foamposite'] -= 3
shoe_inventory['Air Max'] -= 3
shoe_inventory['SB Dunk'] -= 3
print(shoe_inventory)
shoe_inventory['Vans']=8
shoe_inventory['Converse']=7
shoe_inventory['Adidas']=6
print(shoe_inventory)
Wake_Up_Time['Friday']= '10:00am' 
Wake_Up_Time['Saturday']= '11:00am'
Wake_Up_Time['Sunday']= '12:00pm'
print(Wake_Up_Time)
food_prices['Eggs'] = '$1.20'
food_prices['Bacon'] = '$4.00'
food_prices['Cereal'] = '$2.00' 
print(food_prices)
del shoe_inventory['Converse']
del shoe_inventory['Adidas']
del Wake_Up_Time['Friday']
del Wake_Up_Time['Saturday']
del food_prices['Beef']
del food_prices['Bacon']
print(shoe_inventory)
print(Wake_Up_Time)
print(food_prices)