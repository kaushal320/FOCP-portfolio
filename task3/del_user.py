def delete_user(username):
    with open('passwd.txt', 'r') as f:
        lines = f.readlines()

    found = False
    with open('passwd.txt', 'w') as f:
        for line in lines:
            if not line.startswith(f"{username}:"):
                f.write(line)
            else:
                found = True

    if found:
        print("User Deleted.")
    else:
        print("User not found. Nothing changed.")
