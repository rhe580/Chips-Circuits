from sys import argv
import csv

# class Print():
#     def __init__(self, print_nr):
#         self.gates = {}
#         # dictionary of x, y coordinates with key "chip_nr"
#         with open(f'gates&netlists/chip_{print_nr}/print_{print_nr}.csv', newline='') as csvfile:
#             reader = csv.reader(csvfile)
#             for chip, x, y in reader:

#                 # print(f"{chip}: {x}, {y}")
#                 self.gates[chip] = (x, y)

#         print(self.gates)

class Netlist():
    def __init__(self, print_nr, netlist_nr):
        self.gates = {}
        self.path = {}
        # dictionary of x, y coordinates with key "chip_nr"
        with open(f'gates&netlists/chip_{print_nr}/print_{print_nr}.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for chip, x, y in reader:

                # print(f"{chip}: {x}, {y}")
                try:
                    self.gates[int(chip)] = (int(x), int(y))
                except ValueError:
                    pass

        self.connections = []
        with open(f'gates&netlists/chip_{print_nr}/netlist_{netlist_nr}.csv', newline='') as csvfile:
            netlist = csv.reader(csvfile)
            for chip_a, chip_b in netlist:
                try:
                    self.connections.append((int(chip_a), int(chip_b)))
                except ValueError:
                    pass
        print(self.connections)
        print()


    def connect(self, connection):
        self.path[connection] = []
        chip_a = connection[0]
        chip_b = connection[1]
        print(connection)
        x_a = self.gates[chip_a][0]
        y_a = self.gates[chip_a][1]
        x_b = self.gates[chip_b][0]
        y_b = self.gates[chip_b][1]

        print(f"chip a: {x_a}, {y_a}\nchip_b: {x_b}, {y_b}")

        diff_x = x_b - x_a
        diff_y = y_b - y_a

        while x_a != x_b:
            if diff_x < 0:
                x_a -= 1
            else:
                x_a += 1 
            self.path[connection].append((x_a, y_a))

        while y_a != y_b:
            if diff_y < 0:
                y_a -= 1
            else:
                y_a += 1

            self.path[connection].append((x_a, y_a))

        print(self.path[connection])
    
    def check_if_chip(self, next_coor):
        for key in self.gates:
            # check if next point is a gate
            if next_coor in self.gates[key]:
                return True
        return False

    # def check_if_good_chip(self, next_coor)
    #     if self.gates[next_coor]
    #         return True
    #     else:
    #         return False
        

    
    


if __name__ == "__main__":

    print_nr = int(input("Print_nr: "))
    netlist_nr = int(input("Netlist_nr: "))
    print()
    print()
    
    netlist = Netlist(print_nr, netlist_nr)
    print(netlist.gates)
    for connection in netlist.connections:
        print()
        netlist.connect(connection)
        print()
    
    
