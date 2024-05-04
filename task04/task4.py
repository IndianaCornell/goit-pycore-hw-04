# Напишіть функції обробники для різних команд, такі як add_contact(), change_contact(), show_phone(), all() тощо. 

# Використовуйте словник Python для зберігання імен і номерів телефонів. Ім'я буде ключем, а номер телефону – значенням.

# Ваша програма має вміти ідентифікувати та повідомляти про неправильно введені команди.

from command_handlers.handlers import *


hello_commands = ["hello", "hi"]
close_commands = ["close", "exit", "leave", "baye"]
add_command = ["add"]
change_command = ["change"]
get_all_contacts_command = ["all"]
get_contact_command = ["phone"]


def handler(command, contacts, *args):
        
        if command in close_commands:
            print("Good bye!")
            exit()
            
        elif command in hello_commands:
            print("How can I help you?")

        elif command in add_command:
            print(add_contact(args, contacts))

        elif command in change_command: 
            print(change_contact(args, contacts))

        elif command in get_contact_command:
            print(show_phone(args, contacts))

        elif command in get_all_contacts_command: 
            print(show_all(contacts))   

        else:
            print("Invalid command.")


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        handler(command, contacts, *args)



if __name__ == "__main__":
    main()
 
 