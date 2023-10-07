
class Star_Cinema:
    hall_list = []
    
    @classmethod
    def entry_hall(cls, hall_data):
        cls.hall_list.append(hall_data)
        
             

class Hall:
    def __init__(self, rows, cols, hall_no):
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        Star_Cinema.entry_hall(self)
        
    def __allocate_seats(self, id):
        #make all seats
        seats = [[0 for i in range(self.__cols)] for j in range(self.__rows)]
        # #or 
        # seats = []
        # for i in range(self.__rows):
        #     col = []
        #     for j in range(self.__cols):
        #         col.append(0)
        #     seats.append(col)
        self.__seats[id] = seats
        
        
    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.__show_list.append(show_info)
        self.__allocate_seats(id)
        
        
    def book_seats(self, id, row, col):
        if id not in self.__seats:
            print("Invalid show ID.")
            return
        seats = self.__seats[id]

        if row < 1 or row > self.__rows or col < 1 or col > self.__cols:
            print(f"Invalid seat: Row {row}, Column {col}.")
        if seats[row - 1][col - 1] == 0:
            seats[row - 1][col - 1] = 1
            print(f"Seat {row, col} has booked successfully.")
        else:
            print(f"Seat {row, col} is already booked.")
                
                
    def view_show_list(self):
        for show_info in self.__show_list:
            print(f"Show ID: {show_info[0]}, Movie: {show_info[1]}, Time: {show_info[2]}")

    def view_available_seats(self, id):
        if id not in self.__seats:
            print("Invalid show ID.")
            return
        seats = self.__seats[id]
        print(f"Available seats for show {id}:")
        for row in range(self.__rows):
            for col in range(self.__cols):
                # if seats[row][col] == 0:
                #     print(f"Row {row + 1}, Column {col + 1}")
                if seats[row][col] == 0:
                    print(" 0 ", end=' ')
                else:
                    print(" X ", end=' ')
            print()
            
            
hall_1 = Hall(rows = 8, cols = 8, hall_no = 1)

hall_1.entry_show('111', "Thor 4", "11 AM")
hall_1.entry_show('222', "Premer Agun", "2 PM")


while True:
    print("\n1. Press 1 for View All Show Today : ")
    print("2. Press 2 for View Available Seats : ")
    print("3. Press 3 for Book Ticket. ")
    print("4. Press 4 for Exit.\n")

    option = int(input("OPTIONS : "))
    
    if option == 1:
        print("Running movies are : ")
        hall_1.view_show_list()
    
    elif option == 2:
        id = input("Enter movie Id : ")
        hall_1.view_available_seats(id)
    elif option == 3:
        id = input("Enter movie Id : ")
        row = int(input("Enter row : "))
        col = int(input("Enter column : "))
        hall_1.book_seats(id, row, col)
        
    elif option == 4:
        continue