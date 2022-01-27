import pandas as pd

# get all datasets
user_database = pd.read_csv('data/user_credentials.csv')
movie_database = pd.read_csv('dataset/Movies_dataset.csv')


def log_in_who_is_user(user_email):
    
    global uid
    
    email = user_email
    uid = user_database[(user_database['E-mail']==email)].iloc[0,0]

# get uid of who is user 
def who_is_user(user_email,user_password):
    
    global uid
    
    email = user_email
    pswd  = user_password

    # fetch user if from database
    uid = user_database[(user_database['E-mail']==email) & (user_database['Password']==pswd)].iloc[0,0]
    
    
# movie selected then
def movie(movie_name,price):
    
    user = uid
    Uname = user_database[user_database['uid']==user].iloc[0,1]
    Uemail = user_database[user_database['uid']==user].iloc[0,2]
 

# stream selected then   
def stream(stream_name,price):
    user = uid
    Uname = user_database[user_database['uid']==user].iloc[0,1]
    Uemail = user_database[user_database['uid']==user].iloc[0,2]

def buyticket(buy_ticket,price):
    user = uid
    Uname = user_database[user_database['uid']==user].iloc[0,1]
    Uemail = user_database[user_database['uid']==user].iloc[0,2]   


# user all data fram database
def user_data():
    user = uid
    Uname = user_database[user_database['uid']==user].iloc[0,1]
    Uemail = user_database[user_database['uid']==user].iloc[0,2]
    Uphone = user_database[user_database['uid']==user].iloc[0,3]
    
    Uinfo = [user,Uname,Uemail,Uphone]
    return Uinfo


def movie_by_week(week_no):
    wk = week_no
    if wk == 1:
        th_database = pd.read_csv('dataset/Theater_dataset.csv').iloc[1:4,0:1]
        return th_database
    elif wk == 2:
        th_database = pd.read_csv('dataset/Theater_dataset.csv').iloc[4:7,0:1]
        return th_database
    elif wk == 3:
        th_database = pd.read_csv('dataset/Theater_dataset.csv').iloc[7:10,0:1]
        return th_database
    elif wk == 4:
        th_database = pd.read_csv('dataset/Theater_dataset.csv').iloc[10:13,0:1]
        return th_database
    elif wk == 5:
        th_database = pd.read_csv('dataset/Theater_dataset.csv').iloc[13:16,0:1]
        return th_database
    elif wk == 6:
        th_database = pd.read_csv('dataset/Theater_dataset.csv').iloc[16:19,0:1]
        return th_database
    else:
        None
        pass
    

# buy ticket function
def buy_ticket(entered_date,movie):
    
    date = int(entered_date)
    if movie == 'M1':
        if date == 1:
            seat_database = pd.read_csv('data/MOVIE1/day1.csv')
            return seat_database
        
        elif date == 2:
            seat_database = pd.read_csv('data/MOVIE1/day2.csv')
            return seat_database
        
        elif date == 3:
            seat_database = pd.read_csv('data/MOVIE1/day3.csv')
            return seat_database
        
        elif date == 4:
            seat_database = pd.read_csv('data/MOVIE1/day4.csv')
            return seat_database
        
        elif date == 5:
            seat_database = pd.read_csv('data/MOVIE1/day5.csv')
            return seat_database
        
        elif date == 6:
            seat_database = pd.read_csv('data/MOVIE1/day6.csv')
            return seat_database
        
        elif date == 7:
            seat_database = pd.read_csv('data/MOVIE1/day7.csv')
            return seat_database
        
        elif date == 8:
            seat_database = pd.read_csv('data/MOVIE1/day8.csv')
            return seat_database
        
        elif date == 9:
            seat_database = pd.read_csv('data/MOVIE1/day9.csv')
            return seat_database
        
        elif date == 10:
            seat_database = pd.read_csv('data/MOVIE1/day10.csv')
            return seat_database
        elif date == 11:
            seat_database = pd.read_csv('data/MOVIE1/day11.csv')
            return seat_database
        elif date == 12:
            seat_database = pd.read_csv('data/MOVIE1/day12.csv')
            return seat_database
        elif date == 13:
            seat_database = pd.read_csv('data/MOVIE1/day13.csv')
            return seat_database
        elif date == 14:
            seat_database = pd.read_csv('data/MOVIE1/day14.csv')
            return seat_database
        elif date == 15:
            seat_database = pd.read_csv('data/MOVIE1/day15.csv')
            return seat_database
        elif date == 16:
            seat_database = pd.read_csv('data/MOVIE1/day16.csv')
            return seat_database
        elif date == 17:
            seat_database = pd.read_csv('data/MOVIE1/day17.csv')
            return seat_database
        elif date == 18:
            seat_database = pd.read_csv('data/MOVIE1/day18.csv')
            return seat_database
        elif date == 19:
            seat_database = pd.read_csv('data/MOVIE1/day19.csv')
            return seat_database
        elif date == 20:
            seat_database = pd.read_csv('data/MOVIE1/day20.csv')
            return seat_database
        elif date == 21:
            seat_database = pd.read_csv('data/MOVIE1/day21.csv')
            return seat_database
        elif date == 22:
            seat_database = pd.read_csv('data/MOVIE1/day22.csv')
            return seat_database
        elif date == 23:
            seat_database = pd.read_csv('data/MOVIE1/day23.csv')
            return seat_database
        elif date == 24:
            seat_database = pd.read_csv('data/MOVIE1/day24.csv')
            return seat_database
        elif date == 25:
            seat_database = pd.read_csv('data/MOVIE1/day25.csv')
            return seat_database
        elif date == 26:
            seat_database = pd.read_csv('data/MOVIE1/day26.csv')
            return seat_database
        elif date == 27:
            seat_database = pd.read_csv('data/MOVIE1/day27.csv')
            return seat_database
        elif date == 28:
            seat_database = pd.read_csv('data/MOVIE1/day28.csv')
            return seat_database
        elif date == 29:
            seat_database = pd.read_csv('data/MOVIE1/day29.csv')
            return seat_database
        elif date == 30:
            seat_database = pd.read_csv('data/MOVIE1/day30.csv')
            return seat_database
        elif date == 31:
            seat_database = pd.read_csv('data/MOVIE1/day31.csv')
            return seat_database
        else:
            None
            pass
        
    elif movie == 'M2':
        if date == 1:
            seat_database = pd.read_csv('data/MOVIE2/day1.csv')
            return seat_database
        
        elif date == 2:
            seat_database = pd.read_csv('data/MOVIE2/day2.csv')
            return seat_database
        
        elif date == 3:
            seat_database = pd.read_csv('data/MOVIE2/day3.csv')
            return seat_database
        
        elif date == 4:
            seat_database = pd.read_csv('data/MOVIE2/day4.csv')
            return seat_database
        
        elif date == 5:
            seat_database = pd.read_csv('data/MOVIE2/day5.csv')
            return seat_database
        
        elif date == 6:
            seat_database = pd.read_csv('data/MOVIE2/day6.csv')
            return seat_database
        
        elif date == 7:
            seat_database = pd.read_csv('data/MOVIE2/day7.csv')
            return seat_database
        
        elif date == 8:
            seat_database = pd.read_csv('data/MOVIE2/day8.csv')
            return seat_database
        
        elif date == 9:
            seat_database = pd.read_csv('data/MOVIE2/day9.csv')
            return seat_database
        
        elif date == 10:
            seat_database = pd.read_csv('data/MOVIE2/day10.csv')
            return seat_database
        elif date == 11:
            seat_database = pd.read_csv('data/MOVIE2/day11.csv')
            return seat_database
        elif date == 12:
            seat_database = pd.read_csv('data/MOVIE2/day12.csv')
            return seat_database
        elif date == 13:
            seat_database = pd.read_csv('data/MOVIE2/day13.csv')
            return seat_database
        elif date == 14:
            seat_database = pd.read_csv('data/MOVIE2/day14.csv')
            return seat_database
        elif date == 15:
            seat_database = pd.read_csv('data/MOVIE2/day15.csv')
            return seat_database
        elif date == 16:
            seat_database = pd.read_csv('data/MOVIE2/day16.csv')
            return seat_database
        elif date == 17:
            seat_database = pd.read_csv('data/MOVIE2/day17.csv')
            return seat_database
        elif date == 18:
            seat_database = pd.read_csv('data/MOVIE2/day18.csv')
            return seat_database
        elif date == 19:
            seat_database = pd.read_csv('data/MOVIE2/day19.csv')
            return seat_database
        elif date == 20:
            seat_database = pd.read_csv('data/MOVIE2/day20.csv')
            return seat_database
        elif date == 21:
            seat_database = pd.read_csv('data/MOVIE2/day21.csv')
            return seat_database
        elif date == 22:
            seat_database = pd.read_csv('data/MOVIE2/day22.csv')
            return seat_database
        elif date == 23:
            seat_database = pd.read_csv('data/MOVIE2/day23.csv')
            return seat_database
        elif date == 24:
            seat_database = pd.read_csv('data/MOVIE2/day24.csv')
            return seat_database
        elif date == 25:
            seat_database = pd.read_csv('data/MOVIE2/day25.csv')
            return seat_database
        elif date == 26:
            seat_database = pd.read_csv('data/MOVIE2/day26.csv')
            return seat_database
        elif date == 27:
            seat_database = pd.read_csv('data/MOVIE2/day27.csv')
            return seat_database
        elif date == 28:
            seat_database = pd.read_csv('data/MOVIE2/day28.csv')
            return seat_database
        elif date == 29:
            seat_database = pd.read_csv('data/MOVIE2/day29.csv')
            return seat_database
        elif date == 30:
            seat_database = pd.read_csv('data/MOVIE2/day30.csv')
            return seat_database
        elif date == 31:
            seat_database = pd.read_csv('data/MOVIE2/day31.csv')
            return seat_database
        else:
            None
            pass
        
    elif movie == 'M3':
        if date == 1:
            seat_database = pd.read_csv('data/MOVIE3/day1.csv')
            return seat_database
        
        elif date == 2:
            seat_database = pd.read_csv('data/MOVIE3/day2.csv')
            return seat_database
        
        elif date == 3:
            seat_database = pd.read_csv('data/MOVIE3/day3.csv')
            return seat_database
        
        elif date == 4:
            seat_database = pd.read_csv('data/MOVIE3/day4.csv')
            return seat_database
        
        elif date == 5:
            seat_database = pd.read_csv('data/MOVIE3/day5.csv')
            return seat_database
        
        elif date == 6:
            seat_database = pd.read_csv('data/MOVIE3/day6.csv')
            return seat_database
        
        elif date == 7:
            seat_database = pd.read_csv('data/MOVIE3/day7.csv')
            return seat_database
        
        elif date == 8:
            seat_database = pd.read_csv('data/MOVIE3/day8.csv')
            return seat_database
        
        elif date == 9:
            seat_database = pd.read_csv('data/MOVIE3/day9.csv')
            return seat_database
        
        elif date == 10:
            seat_database = pd.read_csv('data/MOVIE3/day10.csv')
            return seat_database
        elif date == 11:
            seat_database = pd.read_csv('data/MOVIE3/day11.csv')
            return seat_database
        elif date == 12:
            seat_database = pd.read_csv('data/MOVIE3/day12.csv')
            return seat_database
        elif date == 13:
            seat_database = pd.read_csv('data/MOVIE3/day13.csv')
            return seat_database
        elif date == 14:
            seat_database = pd.read_csv('data/MOVIE3/day14.csv')
            return seat_database
        elif date == 15:
            seat_database = pd.read_csv('data/MOVIE3/day15.csv')
            return seat_database
        elif date == 16:
            seat_database = pd.read_csv('data/MOVIE3/day16.csv')
            return seat_database
        elif date == 17:
            seat_database = pd.read_csv('data/MOVIE3/day17.csv')
            return seat_database
        elif date == 18:
            seat_database = pd.read_csv('data/MOVIE3/day18.csv')
            return seat_database
        elif date == 19:
            seat_database = pd.read_csv('data/MOVIE3/day19.csv')
            return seat_database
        elif date == 20:
            seat_database = pd.read_csv('data/MOVIE3/day20.csv')
            return seat_database
        elif date == 21:
            seat_database = pd.read_csv('data/MOVIE3/day21.csv')
            return seat_database
        elif date == 22:
            seat_database = pd.read_csv('data/MOVIE3/day22.csv')
            return seat_database
        elif date == 23:
            seat_database = pd.read_csv('data/MOVIE3/day23.csv')
            return seat_database
        elif date == 24:
            seat_database = pd.read_csv('data/MOVIE3/day24.csv')
            return seat_database
        elif date == 25:
            seat_database = pd.read_csv('data/MOVIE3/day25.csv')
            return seat_database
        elif date == 26:
            seat_database = pd.read_csv('data/MOVIE3/day26.csv')
            return seat_database
        elif date == 27:
            seat_database = pd.read_csv('data/MOVIE3/day27.csv')
            return seat_database
        elif date == 28:
            seat_database = pd.read_csv('data/MOVIE3/day28.csv')
            return seat_database
        elif date == 29:
            seat_database = pd.read_csv('data/MOVIE3/day29.csv')
            return seat_database
        elif date == 30:
            seat_database = pd.read_csv('data/MOVIE3/day30.csv')
            return seat_database
        elif date == 31:
            seat_database = pd.read_csv('data/MOVIE3/day31.csv')
            return seat_database
        else:
            None
            pass
    
    else:
        None
        pass
        
        
        
def df_to_csv(database,movie,date):
    if movie == 'M1':
        if date == 1:
            database.to_csv(    'data/MOVIE1/day1.csv',index=False)

        
        elif date == 2:
            database.to_csv(    'data/MOVIE1/day2.csv',index=False)

        
        elif date == 3:
            database.to_csv(    'data/MOVIE1/day3.csv',index=False)

        
        elif date == 4:
            database.to_csv(    'data/MOVIE1/day4.csv',index=False)

        
        elif date == 5:
            database.to_csv(    'data/MOVIE1/day5.csv',index=False)

        
        elif date == 6:
            database.to_csv(    'data/MOVIE1/day6.csv',index=False)

        
        elif date == 7:
            database.to_csv(    'data/MOVIE1/day7.csv',index=False)

        
        elif date == 8:
            database.to_csv(    'data/MOVIE1/day8.csv',index=False)

        
        elif date == 9:
            database.to_csv(    'data/MOVIE1/day9.csv',index=False)

        
        elif date == 10:
            database.to_csv(    'data/MOVIE1/day10.csv',index=False)

        elif date == 11:
            database.to_csv(    'data/MOVIE1/day11.csv',index=False)

        elif date == 12:
            database.to_csv(    'data/MOVIE1/day12.csv',index=False)

        elif date == 13:
            database.to_csv(    'data/MOVIE1/day13.csv',index=False)

        elif date == 14:
            database.to_csv(    'data/MOVIE1/day14.csv',index=False)

        elif date == 15:
            database.to_csv(    'data/MOVIE1/day15.csv',index=False)

        elif date == 16:
            database.to_csv(    'data/MOVIE1/day16.csv',index=False)

        elif date == 17:
            database.to_csv(    'data/MOVIE1/day17.csv',index=False)

        elif date == 18:
            database.to_csv(    'data/MOVIE1/day18.csv',index=False)

        elif date == 19:
            database.to_csv(    'data/MOVIE1/day19.csv',index=False)

        elif date == 20:
            database.to_csv(    'data/MOVIE1/day20.csv',index=False)

        elif date == 21:
            database.to_csv(    'data/MOVIE1/day21.csv',index=False)

        elif date == 22:
            database.to_csv(    'data/MOVIE1/day22.csv',index=False)

        elif date == 23:
            database.to_csv(    'data/MOVIE1/day23.csv',index=False)

        elif date == 24:
            database.to_csv(    'data/MOVIE1/day24.csv',index=False)

        elif date == 25:
            database.to_csv(    'data/MOVIE1/day25.csv',index=False)

        elif date == 26:
            database.to_csv(    'data/MOVIE1/day26.csv',index=False)

        elif date == 27:
            database.to_csv(    'data/MOVIE1/day27.csv',index=False)

        elif date == 28:
            database.to_csv(    'data/MOVIE1/day28.csv',index=False)

        elif date == 29:
            database.to_csv(    'data/MOVIE1/day29.csv',index=False)

        elif date == 30:
            database.to_csv(    'data/MOVIE1/day30.csv',index=False)

        elif date == 31:
            database.to_csv(    'data/MOVIE1/day31.csv',index=False)

        else:
            None
            pass
        
    elif movie == 'M2':
        if date == 1:
            database.to_csv(    'data/MOVIE2/day1.csv',index=False)

        
        elif date == 2:
            database.to_csv(    'data/MOVIE2/day2.csv',index=False)

        
        elif date == 3:
            database.to_csv(    'data/MOVIE2/day3.csv',index=False)

        
        elif date == 4:
            database.to_csv(    'data/MOVIE2/day4.csv',index=False)

        
        elif date == 5:
            database.to_csv(    'data/MOVIE2/day5.csv',index=False)

        
        elif date == 6:
            database.to_csv(    'data/MOVIE2/day6.csv',index=False)

        
        elif date == 7:
            database.to_csv(    'data/MOVIE2/day7.csv',index=False)

        
        elif date == 8:
            database.to_csv(    'data/MOVIE2/day8.csv',index=False)

        
        elif date == 9:
            database.to_csv(    'data/MOVIE2/day9.csv',index=False)

        
        elif date == 10:
            database.to_csv(    'data/MOVIE2/day10.csv',index=False)

        elif date == 11:
            database.to_csv(    'data/MOVIE2/day11.csv',index=False)

        elif date == 12:
            database.to_csv(    'data/MOVIE2/day12.csv',index=False)

        elif date == 13:
            database.to_csv(    'data/MOVIE2/day13.csv',index=False)

        elif date == 14:
            database.to_csv(    'data/MOVIE2/day14.csv',index=False)

        elif date == 15:
            database.to_csv(    'data/MOVIE2/day15.csv',index=False)

        elif date == 16:
            database.to_csv(    'data/MOVIE2/day16.csv',index=False)

        elif date == 17:
            database.to_csv(    'data/MOVIE2/day17.csv',index=False)

        elif date == 18:
            database.to_csv(    'data/MOVIE2/day18.csv',index=False)

        elif date == 19:
            database.to_csv(    'data/MOVIE2/day19.csv',index=False)

        elif date == 20:
            database.to_csv(    'data/MOVIE2/day20.csv',index=False)

        elif date == 21:
            database.to_csv(    'data/MOVIE2/day21.csv',index=False)

        elif date == 22:
            database.to_csv(    'data/MOVIE2/day22.csv',index=False)

        elif date == 23:
            database.to_csv(    'data/MOVIE2/day23.csv',index=False)

        elif date == 24:
            database.to_csv(    'data/MOVIE2/day24.csv',index=False)

        elif date == 25:
            database.to_csv(    'data/MOVIE2/day25.csv',index=False)

        elif date == 26:
            database.to_csv(    'data/MOVIE2/day26.csv',index=False)

        elif date == 27:
            database.to_csv(    'data/MOVIE2/day27.csv',index=False)

        elif date == 28:
            database.to_csv(    'data/MOVIE2/day28.csv',index=False)

        elif date == 29:
            database.to_csv(    'data/MOVIE2/day29.csv',index=False)

        elif date == 30:
            database.to_csv(    'data/MOVIE2/day30.csv',index=False)

        elif date == 31:
            database.to_csv(    'data/MOVIE2/day31.csv',index=False)

        else:
            None
            pass
        
    elif movie == 'M3':
        if date == 1:
            database.to_csv(    'data/MOVIE3/day1.csv',index=False)

        
        elif date == 2:
            database.to_csv(    'data/MOVIE3/day2.csv',index=False)

        
        elif date == 3:
            database.to_csv(    'data/MOVIE3/day3.csv',index=False)

        
        elif date == 4:
            database.to_csv(    'data/MOVIE3/day4.csv',index=False)

        
        elif date == 5:
            database.to_csv(    'data/MOVIE3/day5.csv',index=False)

        
        elif date == 6:
            database.to_csv(    'data/MOVIE3/day6.csv',index=False)

        
        elif date == 7:
            database.to_csv(    'data/MOVIE3/day7.csv',index=False)

        
        elif date == 8:
            database.to_csv(    'data/MOVIE3/day8.csv',index=False)

        
        elif date == 9:
            database.to_csv(    'data/MOVIE3/day9.csv',index=False)

        
        elif date == 10:
            database.to_csv(    'data/MOVIE3/day10.csv',index=False)

        elif date == 11:
            database.to_csv(    'data/MOVIE3/day11.csv',index=False)

        elif date == 12:
            database.to_csv(    'data/MOVIE3/day12.csv',index=False)

        elif date == 13:
            database.to_csv(    'data/MOVIE3/day13.csv',index=False)

        elif date == 14:
            database.to_csv(    'data/MOVIE3/day14.csv',index=False)

        elif date == 15:
            database.to_csv(    'data/MOVIE3/day15.csv',index=False)

        elif date == 16:
            database.to_csv(    'data/MOVIE3/day16.csv',index=False)

        elif date == 17:
            database.to_csv(    'data/MOVIE3/day17.csv',index=False)

        elif date == 18:
            database.to_csv(    'data/MOVIE3/day18.csv',index=False)

        elif date == 19:
            database.to_csv(    'data/MOVIE3/day19.csv',index=False)

        elif date == 20:
            database.to_csv(    'data/MOVIE3/day20.csv',index=False)

        elif date == 21:
            database.to_csv(    'data/MOVIE3/day21.csv',index=False)

        elif date == 22:
            database.to_csv(    'data/MOVIE3/day22.csv',index=False)

        elif date == 23:
            database.to_csv(    'data/MOVIE3/day23.csv',index=False)

        elif date == 24:
            database.to_csv(    'data/MOVIE3/day24.csv',index=False)

        elif date == 25:
            database.to_csv(    'data/MOVIE3/day25.csv',index=False)

        elif date == 26:
            database.to_csv(    'data/MOVIE3/day26.csv',index=False)

        elif date == 27:
            database.to_csv(    'data/MOVIE3/day27.csv',index=False)

        elif date == 28:
            database.to_csv(    'data/MOVIE3/day28.csv',index=False)

        elif date == 29:
            database.to_csv(    'data/MOVIE3/day29.csv',index=False)

        elif date == 30:
            database.to_csv(    'data/MOVIE3/day30.csv',index=False)

        elif date == 31:
            database.to_csv(    'data/MOVIE3/day31.csv',index=False)

        else:
            None
            pass
    
    else:
        None
        pass