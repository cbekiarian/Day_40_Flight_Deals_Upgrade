import requests
url =
def add_user():
    print("Welcome to Chris Flight Club\n We find the best deals and email you")
    f_name = input("What is your first name?")
    l_name =  input("What is your last name?")
    email =  input("What is your email?")
    c_email =  input("Type your email again.")
    if not  email == c_email:
        print("You typed your email wrong, try again")
        add_user()
    else:
        print("you are in the club")
        user_info = {
            "user":{

                "firstName": f_name,
                "lastName": l_name,
                "email": email,

            }
        }
        response = requests.post(url=url,json=user_info)
        response.raise_for_status()
        print(response.text)

def get_user():
    response = requests.get(url=url)
    response.raise_for_status()
    list = response.json()["users"]
    print(list)
    return list