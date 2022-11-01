#start with userss that need to be verified,
# and an empty list to holdconfirmed users

unconfirmed_users = ['alice', 'brian','candance']
confirmed_users = []

#verified each user untill there are more unconfirmed users,
# move each verified user into the list confirmed users
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

#display all confirmed users
print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())