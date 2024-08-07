# Декоратор для обробки помилок
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Invalid input, please try again."
    return inner

# Бот-помічник з командами
contacts = {}

@input_error
def add_contact(args):
    name, phone = args.split()
    contacts[name] = phone
    return "Contact added."

@input_error
def get_phone(args):
    name = args.strip()
    return contacts[name]

@input_error
def show_all(args):
    return '\n'.join(f"{name}: {phone}" for name, phone in contacts.items())

def main():
    COMMANDS = {
        'add': add_contact,
        'phone': get_phone,
        'all': show_all,
    }

    while True:
        command = input("Enter a command: ").strip().lower()
        if command in COMMANDS:
            args = input("Enter the argument for the command: ").strip()
            print(COMMANDS[command](args))
        elif command in ['exit', 'close', 'goodbye']:
            print("Goodbye!")
            break
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()
