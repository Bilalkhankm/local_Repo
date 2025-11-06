import random
def welcome():
    """Greeting function"""
    print("You are welcome in Linear search in a list.")
#===========================================
def display_menu():
    print("\n====== LIST OPERATIONS MENU ======")
    print("1. Display List")
    print("2. Search an Element")
    print("3. Insert Element")
    print("4. Detect Duplicates")
    print("5. Delete an Element")
    print("6.Append Element")
    print("7. Exit")
    print("==================================")    
#===========================================
def list_generator():
    """Generate a list of random numbers"""
    num_list=[]
    list_length = random.randint(1,30)
    while len(num_list) < list_length:
        num = random.randint(1,100)
        num_list.append(num)    
    print("-------------------------------------")
    print("The list has been generated.") 
    return num_list
#============================================
def display(n_list):
    """"Display the list"""
    print()

            
    print(n_list)
  
#============================================
def user_input():
    """User enter the number for linear search"""
    while True:
            try :
                print()
                target = int(input("Enter the number you want to search : "))
                break
            except ValueError:
                print("_______________________________________")
                print("Invalid Input! Only integer is valid.")
    return target
#============================================
def search(n_list, n_target):
    """Liner Search"""
    counter=0
    found = False
    while counter< len(n_list) and not found:
        if n_list[counter] == n_target:
            found = True
            break
        else:
            counter= counter+1

    if found == False:
        print("_________________________________________")
        print("Item not found")
    elif found == True:
        print("__________________________________________")
        print("Item found")
  
#==============================================
def insertion(n_list):
    """Insert an element into the list at a user-specified index."""
    print("-----------------------------------")
    print("INDEX"+ " : " +"VALUES\n")
    for index,value in enumerate(n_list):
        print(index,"   :   ",value )
    while True:
        try:
            print()
            insert_index = int(input("Enter the index you want to insert element there : "))
            insert_element = int(input("Enter the element you want to insert : "))
            break
        except ValueError:
            print("Invalid Input.")    
    n_list.insert(insert_index,insert_element)
    print("-------------------------------------")
    print("The list has been updated.") 
    return n_list
#==============================================
def appendage(n_list):
    """Append an element into the list."""
    while True:
        try:
            append_element = int(input("Enter the element you want to append : "))
            break
        except ValueError:
            print("Invalid Input.")
    n_list.append(append_element) 
    print("-------------------------------------")
    print("The list has been updated.") 
    return n_list       
#==============================================
def deletion(n_list):
    """delete an element into the list at a user-specified index."""
    print("-----------------------------------")
    print("INDEX"+ " : " +"VALUES\n")
    for index,value in enumerate(n_list):
        print(index," : ",value )
    while True:
        try:
            delete_index = int(input("Enter the index of the element you want to remove in list : "))
            break
        except ValueError:
            print("Invalid Input.")
    print("This selected element now going to be delete",n_list[delete_index])        
    del n_list[delete_index]
    print("-------------------------------------")
    print("The list has been updated.") 
    return n_list
#=============================================
def duplicate_detector(n_list):
    """Check the duplicates in the list"""
    unique_list = list(set(n_list))
    print("The list has been updated.")
    return unique_list    
#==============================================
def main():
    print()
    welcome()
    display_menu()
    l=list_generator()
    
    while True:
        try:
            choice = int(input("Please enter your choice : "))
            if choice == 7:
                print("You are out of system.")
                break
            elif choice == 2:
                t=user_input()
                search(l,t)
            elif choice == 3:
                insertion(l)
                
            elif choice == 4:
                l=duplicate_detector(l)
                
            elif choice == 5:
                deletion(l)
                
            elif choice== 6:
                appendage(l)
                
            elif choice == 1:
                display(l)
            else:
                print("Invalid Input")                    
        except ValueError:
            print("You enter invalid entity")
#==============================================
if __name__ == "__main__":
    main()                                      
