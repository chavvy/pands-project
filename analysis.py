#taking inspiration from applied databases project and making a menu for the user to interact with

#FUNCTIONS WILL BE IMPORTED HERE
from menu import show_data_info, summarise_data

def show_menu():
    print("\nIris Dataset Analysis\n---------\n")
    print("MENU\n====")
    print("1. Dataset information")
    print("2. Summarise data")
    print("3. Generate Histogram")
    print("4. Generate Scatterplot")
    print("x. Exit application")

def main():
    while True:
        show_menu()  #display the menu
        choice = input("Enter the number of your choice: ").strip().lower()  #get user's choice
        
        if choice == '1':
            show_data_info()
        elif choice == '2':
            summarise_data()
        elif choice == '3':
            generate_histogram()
        elif choice == '4':
            generate_scatterplot()
        elif choice == 'x':
            print("Exiting application...")
            break  #exit the loop and end the program
        else:
            print("Error: Please select a valid option.")

if __name__ == "__main__":
    main()
