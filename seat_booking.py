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


    # def csv(csv,date,movie_id):

    #         seats = pd.read_csv(csv)
    #         del seats['Unnamed: 0']

    #         t1 = pd.DataFrame(seats.iloc[0:7,:])
    #         t2 = pd.DataFrame(seats.iloc[7:14,:])
    #         t3 = pd.DataFrame(seats.iloc[14:21,:])
    #         t4 = pd.DataFrame(seats.iloc[21:,:])

    #         if date<=7 and date>=1:
    #             if movie_id == 0:
    #                 print(t1)
    #                 seat_available_or_not(t1)
    #                 print(t1)
    #                 seats.to_csv(csv)
    #             elif movie_id == 1:
    #                 print(t2)
    #                 seat_available_or_not(t2)
    #                 print(t2)
    #                 seats.to_csv(csv)
    #             elif movie_id == 2:
    #                 print(t3)
    #                 seat_available_or_not(t3)
    #                 print(t3)
    #                 seats.to_csv(csv)
    #             elif movie_id == 3:
    #                 print(t4)
    #                 seat_available_or_not(t4)
    #                 print(t4)
    #                 seats.to_csv(csv)
    #             else:
    #                 None
    #         if date<=14 and date>=8:
    #             if movie_id == 4:
    #                 print(t1)
    #                 seat_available_or_not(t1)
    #                 print(t1)
    #                 seats.to_csv(csv)
    #             elif movie_id == 5:
    #                 print(t2)
    #                 seat_available_or_not(t2)
    #                 print(t2)
    #                 seats.to_csv(csv)
    #             elif movie_id == 6:
    #                 print(t3)
    #                 seat_available_or_not(t3)
    #                 print(t3)
    #                 seats.to_csv(csv)
    #             elif movie_id == 7:
    #                 print(t4)
    #                 seat_available_or_not(t4)
    #                 print(t4)
    #                 seats.to_csv(csv)
    #             else:
    #                 None
            
                
             
           
    # if date == 1:
    #     csv("data/day1.csv",date,movie_id)
    # elif date == 2:
    #     csv("data/day2.csv",date,movie_id)
    # elif date == 3:
    #     csv("date/day3.csv",date,movie_id)
    # elif date == 4:
    #     csv("date/day4.csv",date,movie_id)
    # elif date == 5:
    #     csv("date/day5.csv",date, movie_id)
    # elif date == 6:
    #     csv("date/day6.csv",date,movie_id)
    # elif date == 7:
    #     csv("date/day7.csv",date, movie_id)
    # elif date == 8:
    #     csv("date/day8.csv",date, movie_id)
    # elif date == 9:
    #     csv("date/day9.csv",date, movie_id)
    # elif date == 10:
    #     csv("date/day10.csv",date, movie_id)
    # elif date == 11:
    #     csv("date/day11.csv",date, movie_id)
    # elif date == 12:
    #     csv("date/day12.csv",date, movie_id)
    # elif date == 13:
    #     csv("date/day13.csv",date, movie_id)
    # elif date == 14:
    #     csv("date/day14.csv",date, movie_id)
    # elif date == 15:
    #     csv("date/day15.csv",date, movie_id)

    
    return a


seat_allotment(0,2)






