from sys import argv
import csv

class Print():

    def __init__(self, print_nr):
        gates = {}
        # dictionary of x, y coordinates with key "chip_nr"
        with open(f'gates&netlists/chip_{print_nr}/print_{print_nr}.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for chip, x, y in reader:

                # print(f"{chip}: {x}, {y}")
                gates[chip] = (x, y)

        print(gates)

class Netlist():
    def __init__(self, print_nr, netlist_nr):
        connections = []
        with open(f'gates&netlists/chip_{print_nr}/netlist_{netlist_nr}.csv', newline='') as csvfile:
            netlist = csv.reader(csvfile)
            for chip_a, chip_b in netlist:
                connections.append((chip_a, chip_b))
        print(connections)

if __name__ == "__main__":

    print_nr = input("Print_nr: ")
    netlist_nr = input("Netlist_nr: ")
    gates = Print(print_nr)
    print()
    netlist = Netlist(print_nr, netlist_nr)
    
    
