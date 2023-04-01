import sys
import networkx as nx
from os import system
import eel

network = nx.Graph()
provinces = ['Chumphon', 'Krabi', 'Nakhon Si Thammarat', 'Narathiwat', 'Pattani', 'Phang Nga', 'Phatthalung', 'Phuket', 'Ranong', 'Satun', 'Songkhla', 'Surat Thani', 'Trang', 'Yala']

# Add nodes
network.add_nodes_from(provinces)

# Add edges
network.add_edge('Chumphon', 'Ranong')
network.add_edge('Chumphon', 'Surat Thani')
network.add_edge('Krabi', 'Phang Nga')
network.add_edge('Ranong', 'Phang Nga')
network.add_edge('Ranong', 'Surat Thani')
network.add_edge('Surat Thani', 'Krabi')
network.add_edge('Surat Thani', 'Nakhon Si Thammarat')
network.add_edge('Surat Thani', 'Phang Nga')
network.add_edge('Krabi', 'Trang')
network.add_edge('Krabi', 'Nakhon Si Thammarat')
network.add_edge('Trang', 'Nakhon Si Thammarat')
network.add_edge('Phatthalung', 'Nakhon Si Thammarat')
network.add_edge('Songkhla', 'Nakhon Si Thammarat')
network.add_edge('Trang', 'Satun')
network.add_edge('Phatthalung', 'Satun')
network.add_edge('Trang', 'Phatthalung')
network.add_edge('Phatthalung', 'Songkhla')
network.add_edge('Songkhla', 'Pattani')
network.add_edge('Pattani', 'Narathiwat')
network.add_edge('Pattani', 'Yala')
network.add_edge('Narathiwat', 'Yala')
network.add_edge('Yala', 'Songkhla')
network.add_edge('Songkhla', 'Satun')
network.add_edge('Phuket', 'Phang Nga')

# Add edge weights
edge_labels = {
    ('Chumphon', 'Ranong'): 123.0, 
    ('Ranong', 'Chumphon'): 123.0,
    ('Surat Thani', 'Chumphon'): 217.8,
    ('Chumphon', 'Surat Thani'): 217.8,
    ('Phang Nga', 'Krabi'): 145.7, 
    ('Krabi', 'Phang Nga'): 145.7, 
    ('Ranong', 'Phang Nga'): 212.3, 
    ('Phang Nga', 'Ranong'): 212.3,
    ('Ranong', 'Surat Thani'): 240.2, 
    ('Surat Thani', 'Ranong'): 240.2,
    ('Surat Thani', 'Krabi'): 120.9, 
    ('Krabi', 'Surat Thani'): 120.9,
    ('Nakhon Si Thammarat', 'Surat Thani'): 137.7, 
    ('Surat Thani', 'Nakhon Si Thammarat'): 137.7,
    ('Surat Thani', 'Phang Nga'): 115.6, 
    ('Phang Nga', 'Surat Thani'): 115.6,
    ('Krabi', 'Trang'): 115.6, 
    ('Trang', 'Krabi'): 115.6, 
    ('Krabi', 'Nakhon Si Thammarat'): 107.1, 
    ('Nakhon Si Thammarat', 'Krabi'): 107.1, 
    ('Trang', 'Nakhon Si Thammarat'): 141.0, 
    ('Nakhon Si Thammarat', 'Trang'): 141.0,
    ('Phatthalung', 'Nakhon Si Thammarat'): 154.8, 
    ('Nakhon Si Thammarat', 'Phatthalung'): 154.8, 
    ('Nakhon Si Thammarat', 'Songkhla'): 252.1, 
    ('Songkhla', 'Nakhon Si Thammarat'): 252.1,
    ('Trang', 'Satun'): 117.3, 
    ('Satun', 'Trang'): 117.3, 
    ('Phatthalung', 'Satun'): 123.7, 
    ('Satun', 'Phatthalung'): 123.7,
    ('Trang', 'Phatthalung'): 49.6, 
    ('Phatthalung','Trang'): 49.6, 
    ('Phatthalung', 'Songkhla'): 124.1, 
    ('Songkhla', 'Phatthalung'): 124.1, 
    ('Songkhla', 'Pattani'): 109.2, 
    ('Pattani', 'Songkhla'): 109.2, 
    ('Pattani', 'Narathiwat'): 115.9, 
    ('Narathiwat', 'Pattani'): 115.9,
    ('Pattani', 'Yala'): 90.3, 
    ('Yala', 'Pattani'): 90.3,
    ('Narathiwat', 'Yala'): 103.0, 
    ('Yala', 'Narathiwat'): 103.0,
    ('Yala', 'Songkhla'): 173.7, 
    ('Songkhla', 'Yala'): 173.7,
    ('Songkhla', 'Satun'): 108.1, 
    ('Satun', 'Songkhla'): 108.1,
    ('Phuket', 'Phang Nga'): 108.3, 
    ('Phang Nga', 'Phuket'): 108.3
}

@eel.expose
def helloWorld():
    print("Hello, World!")

@eel.expose
def getShortestPath(start, end):
    shortestPath = nx.shortest_path(network, start, end)
    totalDistance = sum(edge_labels[(shortestPath[i], shortestPath[i+1])] for i in range(len(shortestPath)-1))
    totalDistance = round(totalDistance, 2)

    return shortestPath, totalDistance

@eel.expose
def stop():
    sys.exit()

eel.init("web")
eel.start("index.html")

system("cls")