import pandas as pd


def seat_allotment(movie_id,date):
 
    def seat_available_or_not(theatre):
        global row,column,a

        available = False
        while available == False:
            column = 's' + str(input("Column: "))
            row =  int(input("Row: "))
            if theatre[column][row] == 1:
                print("seat",column+'-'+str(row),"is already Booked!")
            else:
                theatre[column][row]=1
                print("seat available",column+'-'+str(row))
                print("Booking seat...")
                # print("seat booked!")
                a = str(row,column,'is booked!')
                available = True
        return a

seat_allotment(0,2)






