def main():
    email_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        name_check = input("Is your name {}? (Y/N) ".format(name))
        if name_check.upper() != "Y" and name_check != "":
            name = input("Name: ")
        email_name[email] = name
        email = input("Email: ")

    for email, name in email_name.items():
        print("{} ({})".format(name, email))


def get_name_from_email(email):
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()
