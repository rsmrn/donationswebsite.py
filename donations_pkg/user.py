def login( database, username, password):

    if username in database:
        if password == database[username]:
            print("Welcome back", username ,"!")
            return username
        print("Incorrect password for",username,".")
        return ""
    print("User is not found.Please register") 
    return ""


def register(database,username,password):
    if username in database:
        print("Username already registered.")
        return ""
    print("Username",username,"has been registered")
    return username 
