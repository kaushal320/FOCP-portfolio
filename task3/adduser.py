def check_existing_username(username):
    existing=[]
    with open('passwd.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            a=line.split(':')
            username=a[0]
            existing.append(username)
        return username in existing

def add_user(username, real_name, passwords):
    if check_existing_username(username) is True:
        print("Cannot add.Most likely username already exists.")
    else:
        with open('passwd.txt', 'a') as f:
            f.write(f"{username}:{real_name}:{passwords}\n")
        print("User Created.")
