# запускати онлі з консолі 
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command =="change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command=="all":
            print(show_all(args, contacts))
        else:
            print("Invalid command.")


def input_error(func):
    def inner(*args,**kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return"Enter user name."
        except KeyError:
            return"Contact not found."
    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."
@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return"Contact updated."
    else:
        return "Contact not found."
@input_error
def  show_phone(args, contacts):
    name= args[0]
    if name in contacts:
        return contacts[name]
    else:
        return"Contact not found."
@input_error
def show_all(args, contacts):
    if not contacts:
        return"No contacts found"
    result=""
    for name , phone in contacts.items():
        result += f"{name}:{phone}\n"
    return result.strip()


if __name__ == "__main__":
    main()
