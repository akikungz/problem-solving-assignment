# import libraries
import networkx as nx
from os import system

# Creat a main function
def main(): 
    # Create a graph
    network = nx.Graph()
    provinces = ['Chumphon', 'Krabi', 'Nakhon Si Thammarat', 'Narathiwat', 'Pattani', 'Phang Nga', 
                'Phatthalung', 'Phuket', 'Ranong', 'Satun', 'Songkhla', 'Surat Thani', 'Trang', 'Yala']

    # Add nodes
    network.add_nodes_from(provinces)

    # Add edges
    network.add_edge('Chumphon', 'Ranong'), network.add_edge('Chumphon', 'Surat Thani'), 
    network.add_edge('Krabi', 'Phang Nga'), network.add_edge('Ranong', 'Phang Nga'), 
    network.add_edge('Ranong', 'Surat Thani'), network.add_edge('Surat Thani', 'Krabi'), 
    network.add_edge('Surat Thani', 'Nakhon Si Thammarat'), network.add_edge('Surat Thani', 'Phang Nga'), 
    network.add_edge('Krabi', 'Trang'), network.add_edge('Krabi', 'Nakhon Si Thammarat'), 
    network.add_edge('Trang', 'Nakhon Si Thammarat'), network.add_edge('Phatthalung', 'Nakhon Si Thammarat'), 
    network.add_edge('Songkhla', 'Nakhon Si Thammarat'), network.add_edge('Trang', 'Satun'), 
    network.add_edge('Phatthalung', 'Satun'), network.add_edge('Trang', 'Phatthalung'), 
    network.add_edge('Phatthalung', 'Songkhla'), network.add_edge('Songkhla', 'Pattani'), 
    network.add_edge('Pattani', 'Narathiwat'), network.add_edge('Pattani', 'Yala'), network.add_edge('Narathiwat', 'Yala'), 
    network.add_edge('Yala', 'Songkhla'), network.add_edge('Songkhla', 'Satun'), network.add_edge('Phuket', 'Phang Nga')
    
    # Add edge weights
    edge_labels = {('Chumphon', 'Ranong'): 123.0, ('Ranong', 'Chumphon'): 123.0,
                ('Surat Thani', 'Chumphon'): 217.8, ('Chumphon', 'Surat Thani'): 217.8,
                ('Phang Nga', 'Krabi'): 145.7, ('Krabi', 'Phang Nga'): 145.7, 
                ('Ranong', 'Phang Nga'): 212.3, ('Phang Nga', 'Ranong'): 212.3,
                ('Ranong', 'Surat Thani'): 240.2, ('Surat Thani', 'Ranong'): 240.2,
                ('Surat Thani', 'Krabi'): 120.9, ('Krabi', 'Surat Thani'): 120.9,
                ('Nakhon Si Thammarat', 'Surat Thani'): 137.7, ('Surat Thani', 'Nakhon Si Thammarat'): 137.7,
                ('Surat Thani', 'Phang Nga'): 115.6, ('Phang Nga', 'Surat Thani'): 115.6,
                ('Krabi', 'Trang'): 115.6, ('Trang', 'Krabi'): 115.6, 
                ('Krabi', 'Nakhon Si Thammarat'): 107.1, ('Nakhon Si Thammarat', 'Krabi'): 107.1, 
                ('Trang', 'Nakhon Si Thammarat'): 141.0, ('Nakhon Si Thammarat', 'Trang'): 141.0,
                ('Phatthalung', 'Nakhon Si Thammarat'): 154.8, ('Nakhon Si Thammarat', 'Phatthalung'): 154.8, 
                ('Nakhon Si Thammarat', 'Songkhla'): 252.1, ('Songkhla', 'Nakhon Si Thammarat'): 252.1,
                ('Trang', 'Satun'): 117.3, ('Satun', 'Trang'): 117.3, 
                ('Phatthalung', 'Satun'): 123.7, ('Satun', 'Phatthalung'): 123.7,
                ('Trang', 'Phatthalung'): 49.6, ('Phatthalung','Trang'): 49.6, 
                ('Phatthalung', 'Songkhla'): 124.1, ('Songkhla', 'Phatthalung'): 124.1, 
                ('Songkhla', 'Pattani'): 109.2, ('Pattani', 'Songkhla'): 109.2, 
                ('Pattani', 'Narathiwat'): 115.9, ('Narathiwat', 'Pattani'): 115.9,
                ('Pattani', 'Yala'): 90.3, ('Yala', 'Pattani'): 90.3,
                ('Narathiwat', 'Yala'): 103.0, ('Yala', 'Narathiwat'): 103.0,
                ('Yala', 'Songkhla'): 173.7, ('Songkhla', 'Yala'): 173.7,
                ('Songkhla', 'Satun'): 108.1, ('Satun', 'Songkhla'): 108.1,
                ('Phuket', 'Phang Nga'): 108.3, ('Phang Nga', 'Phuket'): 108.3}

    # Menu for the user to select the starting and ending provinces
    print(f"There are {network.number_of_nodes()} provinces in total.")
    print("Select a starting and ending province:")
    print("1. Chumphon")
    print("2. Krabi")
    print("3. Nakhon Si Thammarat")
    print("4. Narathiwat")
    print("5. Pattani")
    print("6. Phang Nga")
    print("7. Phatthalung")
    print("8. Phuket")
    print("9. Ranong")
    print("10. Satun")
    print("11. Songkhla")
    print("12. Surat Thani")
    print("13. Trang")
    print("14. Yala")

    # Get the province numbers from the user
    start_province = int(input("Enter the number of the starting province: "))
    end_province = int(input("Enter the number of the ending province: "))
    
    
    def confirm():
        
        choice = input("Confirm provinces (y/n): ")
        
        while True:
            
            if choice == "y":
                return
            elif choice == "n":
                system("cls")
                main()
    
    confirm()

    # Convert the province numbers to the province names
    start_province = provinces[start_province - 1]
    end_province = provinces[end_province - 1]

    # Print finding the shortest path
    print(f"You will be travelling from {start_province} to {end_province}")

    # Use the built-in shortest path algorithm to find the shortest path
    shortest_path = nx.shortest_path(network, start_province, end_province)

    # Calculate the total distance in kilometers by summing the edge weights
    total_distance = sum(edge_labels[(shortest_path[i], shortest_path[i+1])] for i in range(len(shortest_path)-1))
    total_distance = round(total_distance, 2)
    
    # Print the result to the user
    print(f"The shortest distance between {start_province} and {end_province} is {total_distance} km.")
    print(f"The shortest path is: {shortest_path}")

    # main program loop
    while True:

        # ask user if they want to do it again
        choice = input("Do you want to used again? (y/n): ").lower()
        
        # if yes, run main again
        if choice == "y":
            system("cls")
            main()
            
        # if no, break out of loop
        elif choice == "n":
            print("Thanks for using the program!")
            exit()

# run main function
main()