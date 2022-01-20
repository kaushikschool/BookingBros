import pandas as pd


user_database = pd.read_csv('data/user_credentials.csv')
movie_database = pd.read_csv('movies_data/Movies_dataset.csv')

# uid = 0 

def who_is_user(user_email,user_password):
    
    global uid
    
    email = user_email
    pswd  = user_password

    
    # fetch user if from database
    uid = user_database[(user_database['E-mail']==email) & (user_database['Password']==pswd)].iloc[0,0]
    
    
    
    

def movie(movie_name,price):
    
    user = uid
    Uname = user_database[user_database['uid']==user].iloc[0,1]
    Uemail = user_database[user_database['uid']==user].iloc[0,2]
    
def stream(stream_name,price):
    user = uid
    Uname = user_database[user_database['uid']==user].iloc[0,1]
    Uemail = user_database[user_database['uid']==user].iloc[0,2]


def user_data():
    user = uid
    Uname = user_database[user_database['uid']==user].iloc[0,1]
    Uemail = user_database[user_database['uid']==user].iloc[0,2]
    Uphone = user_database[user_database['uid']==user].iloc[0,3]
    
    Uinfo = [user,Uname,Uemail,Uphone]
    return Uinfo
