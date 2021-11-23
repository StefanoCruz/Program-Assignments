#creating empty list
checklist = []

# CREATE
def create(item):
    checklist.append(item)

    return "added {} to checklist".format(item)

# READ
def read(index):
    print(checklist[index])

    return checklist[index]

# UPDATE 
def update(index, item):
    old = checklist[index]
    checklist[index] = item

    return "changed {} to {}".format(old, item)
   
# DESTROY
def destroy(index):
    removed = checklist[index]
    checklist.pop(index)

    return "removed {} from checklist".format(removed)

#get all items 
def all_items():

    items = []

    for el in checklist:
        print(el)
        items.append(el)
    return items

#completed items
def complete(index):
     
    unchecked = checklist[index]

    checklist[index] = "√" + unchecked
    
    return checklist[index]

#user input function
def user_input(prompt):

    entry = input(prompt)

    return entry

#user choice function
def user_choice():
    #initialize variable for while loop
    editing = True
    
    while editing:

        choice = user_input("Which function would you like to use? Enter C for create, R for read. U for update, and D for destroy.")

        if choice == "C" or choice == "c":
            item = user_input("What item do you wish to create?  Type out the name of your desired item.")
            create(item)
            continue

        elif choice == "R" or choice == "r":
            index = user_input("What item do you wish to read?  Give a number for the position of the item.")
            read(int(index))
            continue

        elif choice == "U" or choice == "u":
            update_index = user_input("What item do you wish to update?  Give a number for the position of the  item")
            
            new_item = user_input("Type out the name of your new item.")
            update(int(update_index), new_item)
            continue

        elif choice == "D" or choice == "d":
            destroy_index = user_input("What item do you wish to destroy?  Give a number for the position of the  item")
            destroy(int(destroy_index))
            continue

        else:
            end = user_input("Do you wish to quit? Enter Y for yes or N for no.")

            if end == "Y" or end == "y":
                print(checklist)
                editing = False
            
            else:
                continue

#testing
def test():
    
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")

    '''print(read(0))
    print(all_items())
    print(complete(0))
    print(user_input("Is this working?"))'''
    user_choice()

user_choice()


