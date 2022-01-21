import pandas as pd

# get all datasets
user_database = pd.read_csv('data/user_credentials.csv')
movie_database = pd.read_csv('dataset/Movies_dataset.csv')


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

# user all data fram database
def user_data():
    user = uid
    Uname = user_database[user_database['uid']==user].iloc[0,1]
    Uemail = user_database[user_database['uid']==user].iloc[0,2]
    Uphone = user_database[user_database['uid']==user].iloc[0,3]
    
    Uinfo = [user,Uname,Uemail,Uphone]
    return Uinfo

# buy ticket function
def buy_ticket(entered_date):
    
    date = int(entered_date)
    
    if date == 1:
        seat_database = pd.read_csv('data/MOVIE1/day1.csv')
        return seat_database
    
    elif date == 2:
        seat_database = pd.read_csv('data/day2.csv')
        return seat_database
    
    elif date == 3:
        seat_database = pd.read_csv('data/day3.csv')
        return seat_database
    
    elif date == 4:
        seat_database = pd.read_csv('data/day4.csv')
        return seat_database
    
    elif date == 5:
        seat_database = pd.read_csv('data/day5.csv')
        return seat_database
    
    elif date == 6:
        seat_database = pd.read_csv('data/day6.csv')
        return seat_database
    
    elif date == 7:
        seat_database = pd.read_csv('data/day7.csv')
        return seat_database
    
    elif date == 8:
        seat_database = pd.read_csv('data/day8.csv')
        return seat_database
    
    elif date == 9:
        seat_database = pd.read_csv('data/day9.csv')
        return seat_database
    
    elif date == 10:
        seat_database = pd.read_csv('data/day10.csv')
        return seat_database
    
def seats(datbase):
    df = datbase
    print(df)