age = 20

is_vip = True
is_banned = False

if age >= 18 and is_vip:
    print("Access granted: VIP adult")

if age >= 18 or is_vip:
    print("Access granted: adult or VIP")

if not is_banned:
    print("User is not banned, access possible")

if age >= 18:
    if is_vip:
        print("Adult VIP user")
    else:
        print("Adult reqular user")
else:
    print("Minor")

if age < 18:
    print("Minor")
elif age >= 18 and is_vip:
    print("Adult VIP user")
else:
    print("Adult regular user")