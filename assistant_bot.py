"""
Module for an assistant bot that recognizes commands entered from the keyboard 
and responds according to the entered command.

This module demonstrates a simple implementation of a command-based interaction with a user,
handling predefined commands like greeting, help, and exit.
"""
from collections import defaultdict

def input_error(func):
    """
    The input_error decorator is designed to enhance error handling in functions by catching 
    and responding to common exceptions such as KeyError, ValueError, and IndexError. 
    """
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError as e:
            return f"Given key not found {e}"
        except IndexError:
            return "Insufficient data provided."

    return inner


def parse_input(user_input):
    """
    Parses the user input into a command and its arguments.

    Args:
        user_input (str): The full command input by the user.

    Returns:
        tuple: A tuple where the first element is the command (str) 
        and the rest are arguments (list).
    """
    cmd, *args = user_input.split()
    return cmd.lower(), args


@input_error
def add_contact(args, contacts):
    """
    Adds or updates a contact in the contact book.

    Args:
        args (list): List containing the name and phone number.
        contacts (dict): The contact book dictionary.

    Returns:
        str: A confirmation message.
    """
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    """
    Changes an existing contact's phone number.

    Args:
        args (list): List containing the name and the new phone number.
        contacts (dict): The contact book dictionary.

    Returns:
        str: A confirmation message or an error message if the contact doesn't exist.
    """
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        raise KeyError(f"Contact {name} not found.")

@input_error
def show_phone(args, contacts):
    """
    Shows the phone number of a specified contact.

    Args:
        args (list): List containing the name of the contact.
        contacts (dict): The contact book dictionary.

    Returns:
        str: The contact's phone number or an error message if the contact doesn't exist.
    """
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."

def show_all(contacts):
    """
    Shows all contacts in the contact book.

    Args:
        contacts (dict): The contact book dictionary.

    Returns:
        str: A string representation of all contacts or a message if there are no contacts.
    """
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    else:
        return "No contacts found."

def main():
    """
    The main function to run the assistant bot. It initializes the contact book and
    processes commands until the user decides to exit.
    """
    contacts = defaultdict(str)
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
    