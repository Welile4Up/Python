current_users = ["Steve", "Bob", "Tom", "Farah", "Mo"]
new_users = ["Bob", "Mpho", "Maako", "Tom", "Pheko"]

for new_user in new_users:
    if new_user in current_users:
        print(f"{new_user} is not available. Please enter a different username.")
    else:
        print(f"{new_user} is available as a username.")

