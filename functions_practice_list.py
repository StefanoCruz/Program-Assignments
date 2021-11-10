Cities = ['Oakland', 'Atlanta', 'New York City', 
'Seattle', 'Memphis', 'Miami', 
'Boston', 'Los Angeles', 'Denver', 'New Orleans']
Assassins_Creed_Games = ['1.Assassin’s Creed (2007)',
'2. Assassin’s Creed II (2009)',
'3. Assassin’s Creed: Brotherhood (2010)',
'4. Assassin’s Creed: Revelations (2011)',
'5. Assassin’s Creed III (2012)',
'6. Assassin’s Creed IV: Black Flag (2013)',
'7. Assassin’s Creed: Rogue (2014)',
'8. Assassin’s Creed: Unity (2014)',
'9. Assassin’s Creed: Syndicate (2015',
'10. Assassin’s Creed: Origins (2017)',
'11. Assassin’s Creed: Odyssey (2018)',
'12. Assassin’s Creed: Valhalla (2021)']
Cities[0] = 'San Francisco' 
Cities[2] = 'Brooklyn'
Cities[7] = 'Hollywood'
Cities[5] = 'Tampa'
Cities . append ('Oakland')
Cities . extend (['Los Angeles', 'New York City,'])
Cities . insert (0, 'Miami')
del Cities [3]
Cities.pop (6)
Cities.remove('Atlanta')

def print_city(list):
    for el in list:
        print(el)
        return "All cities printed"

print(print_city(Cities))
print(Cities)

def reorganize_list(list):
    counter=0
    while counter < len(list):
        item1=list[counter]
        item2=list[counter +1] 

        if len(item1) >= len(item2):
            counter += 1
            continue
        elif counter + 1 == len(list) -1:
            break
        else:
            list.remove(item1)
            list.append(item1)
            counter +=1

        return list

print(reorganize_list(Cities))

def sort_list(list):
    return list

print(sort_list(Assassins_Creed_Games))

