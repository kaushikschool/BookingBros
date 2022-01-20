import pandas as pd
from datentime import user_week_no as wk
from seat_booking import seat_allotment



def billing_system(mode):
    if mode == 'card':
        user_name = input("Enter name: ")
        card_no   = int(input("Card no.: "))

    elif mode == 'app':
        user_name = input("Enter name: ")
        phone_no   = int(input("Phone no.: "))
        
    else:
        None


def main():
    print("\n1. for movies")
    print("2. for stream")
    first_input     = int(input("select any one: ")) # select movies/stream
    

    
    if first_input == 1:
        # date_of_booking = (input("Enter date in dd mm yyyy: ")).split(' ')
        # date = int(date_of_booking[0])

        date_entry  = input('Enter a date in YYYY-MM-DD format: ')
        date        = date_entry.split('-')[2] 
        df = pd.read_csv('movies_data/Movies_dataset.csv')

        if   wk(date_entry) == 1:
            print(df.iloc[0:4,:])
        elif wk(date_entry) == 2:
            print(df.iloc[4:8,:])
        elif wk(date_entry) == 3:
            print(df.iloc[8:12,:])
        elif wk(date_entry) == 4:
            print(df.iloc[12:16,:])
        elif wk(date_entry) == 5:
            print(df.iloc[16:20,:])
        elif wk(date_entry) == 6:
            print(df.iloc[20:24,:])
        else:
            print("Data will be avialbe soon")
           
        movie_id = int(input("enter movie id: "))
        print(seat_allotment(movie_id, date)) 
        '''  here is error   
        calling dunction but no output'''
        
    
    elif first_input == 2:
      
        
        for i in range(len(pkgs)):
            # print('-'* (int(len(max(pkgs[i],key=len)))+2)) => isko mai nahi hataunga x_x
            
            print('-'*20)
            print(f'Package for $: ',pkgs[i][-1],'\n')
            print(*pkgs[i][0:-1],sep="\n")
            print('-'*20)
    else:
        print("Choose either 1 or 2")
            

# while True:
main()




'''
this is important 
------------------------------------------ 
| show user: payment or books more seats |
|                                        |
|                                        |
------------------------------------------
'''