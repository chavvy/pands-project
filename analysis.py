#taking inspiration from applied databases project and making a menu for the user to interact with

#FUNCTIONS WILL BE IMPORTED HERE

def show_menu():
    print("\nIris Dataset Analysis\n---------\n")
    print("MENU\n====")
    print("1. Summarising the data")
    print("2. Histograms")
    print("3. Scatterplots")
    print("4. [placeholder]")
    print("x. Exit application")

def main():
    while True:
        show_menu()  #display the menu
        choice = input("Enter the number of your choice: ").strip().lower()  #get user's choice
        
        if choice == '1':
            placeholder1()
        elif choice == '2':
            placeholder2()
        elif choice == '3':
            placeholder3()
        elif choice == '4':
            placeholder4()
        elif choice == 'x':
            print("Exiting application...")
            break  #exit the loop and end the program
        else:
            print("Error: Please select a valid option.")

if __name__ == "__main__":
    main()
