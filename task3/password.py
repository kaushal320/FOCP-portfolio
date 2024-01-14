def change_password(username, current_password, new_password):
    with open('passwd.txt', 'r') as f:
        lines = f.readlines()

    found = False
    with open('passwd.txt', 'w') as f:
        for line in lines:
            if line.startswith(f"{username}:") and line.endswith(f":{current_password}\n"):
                found = True
                f.write(f"{username}:{line.split(':')[1]}:{new_password}\n")
            else:
                f.write(line)
    if found:
        print("Password changed.")
    else:
        print("User not found or current password is incorrect. Nothing changed.")