import re

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args: tuple, contacts: dict) -> str:
        
        try: 
            contact_name, phone = args
            pattern = r"[\D]"
            contacts[contact_name] = re.sub(pattern, "", phone)
            return "Contact added."
        
        except ValueError:
            return "You need to type only 2 arguments (name and number) after ""add"" "


def change_contact(args: tuple, contacts: dict) -> str:
    try: 
        contact_name, phone = args

        if contact_name not in contacts.keys(): 
            return "You cant change contact, becouse it does not exist"
        else: 
            contacts[contact_name] = phone.strip()
            return "Contact updated."
        
    except ValueError:
        return "You need to type only 2 arguments (name and number) after ""change"" "



def show_phone(args: tuple, contacts: dict) -> str:
    try: 
        if len(args) != 1: 
            raise ValueError("You need to type only 1 argument (name) after ""phone"" ")
        
        contact_name = args[0]

        if contact_name not in contacts.keys():
            return "Contact does not exist"
        
        return f"{contact_name}: {contacts[contact_name]}"
    
    except Exception as error:
        return f"{error}"



def show_all(contacts: dict) -> str:

    if not contacts: 
        return "Your contacts list is empty"
    
    else:
        response = "Your contacts:"
        for name, number in contacts.items():
            response += f"\v\t {name}: {number}"

    return response





