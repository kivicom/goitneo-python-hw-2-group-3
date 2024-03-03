"""
This module implements a system for managing an address book.

It contains classes for storing contact information such as name, phone number, etc.
Also provides functionality for adding, deleting, searching, and editing contacts.
"""

from collections import UserDict

class Field:
    """
    A base class for different types of fields in a contact record.
    """
    def __init__(self, value):
        self.value = value

class Name(Field):
    """
    A class representing a contact's name, inherits from Field.
    """

class Phone(Field):
    """
    A class representing a contact's phone number, inherits from Field.
    
    Validates that the phone number is 10 digits.
    """

    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must be 10 digits")
        super().__init__(value)

class Record:
    """
    A class for storing a contact record, including name and phone numbers.
    """
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        """
        Adds a new phone number to the contact's list of phones.
        
        Parameters:
        - phone: The phone number to add as a string.
        """
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        """
        Removes a phone number from the contact's list of phones.
        
        Parameters:
        - phone: The phone number to remove as a string.
        """
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        """
        Edits an existing phone number in the contact's list of phones.
        
        Parameters:
        - old_phone: The current phone number to be replaced as a string.
        - new_phone: The new phone number as a string.
        
        Raises:
        - ValueError: If the old phone number is not found.
        """
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                return
        raise ValueError("Phone not found")

    def find_phone(self, phone):
        """Searching for a specific phone in a record"""
        for p in self.phones:
            if p.value == phone:
                return p.value
        return None

class AddressBook(UserDict):
    """
    A class for storing and managing contacts in an address book.

    This class provides methods to add, delete, search, and edit contacts.
    Each contact is stored as a Record object.
    """

    def add_record(self, record):
        """
        Adds a new contact record to the address book.
        
        Parameters:
        - record: The Record object to add.
        """
        self.data[record.name.value] = record

    def find(self, name):
        """Finding and editing the phone for John"""
        return self.data.get(name, None)

    def delete(self, name):
        """Deleting name's record"""
        if name in self.data:
            del self.data[name]

# Example usage
if __name__ == "__main__":
    # Creating a new address book
    book = AddressBook()

    # Creating a record for John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Adding John's record to the address book
    book.add_record(john_record)

    # Creating and adding a new record for Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Printing all records in the book
    for c_name, c_record in book.data.items():
        print(c_record)

    # Finding and editing the phone for John
    john = book.find("John")
    if john:
        john.edit_phone("1234567890", "1112223333")

    print(john)  # Output: Contact name: John, phones: 1112223333; 5555555555

    # Searching for a specific phone in John's record
    found_phone = john.find_phone("5555555555")
    if found_phone:
        print(f"{john.name.value}: {found_phone}")  # Output: John: 5555555555

    # Deleting Jane's record
    book.delete("Jane")
