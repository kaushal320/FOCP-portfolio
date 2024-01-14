def login_user(username, password):
    with open('passwd.txt', 'r') as f:
        for line in f:
            u, _, p = line.strip().split(':')
            if u == username and p == password:
                print("Access granted.")
                return
    print("Access denied.")
