# contact-book
a simple contact book creation using python
# Contact Book

A simple contact book application built using Python's Tkinter library. This application allows users to add, delete, find, and list contacts.

## Features

- Add new contacts with name, phone number, email, and address
- Delete contacts
- Find and display contact details
- List all contacts in a listbox

## Prerequisites

- Python 3.x
- Tkinter (comes pre-installed with standard Python distribution)

## Installation

1. Ensure Python 3.x is installed on your machine.
2. Clone the repository or download the script file.

## Usage

1. Run the script using Python:
    ```bash
    python contact_book.py
    ```

2. A window titled "CONTACT BOOK" will open.

3. Use the input fields to add a new contact:
    - **Name**: Enter the contact's name.
    - **Phone**: Enter the contact's phone number.
    - **Email**: Enter the contact's email address.
    - **Address**: Enter the contact's address.

4. Click the "Add Contact" button to add the contact to the list. If any field is empty, a warning message will be shown.

5. To search for a contact, enter the name in the "Search" field and click "Find Contact". If the contact is found, its details will be displayed in a message box.

6. To delete a contact, enter the name in the "Search" field and click "Delete Contact". If the contact is found, it will be removed from the list.

7. The contact list is displayed in the listbox at the bottom of the window.

## Script Breakdown

- **Imports**:
    - `tkinter` for GUI components
    - `tkinter.messagebox` for error and information messages

- **Main Window Setup**:
    - `window` to initialize the main window

- **Entry Widgets**:
    - `entry_Name`, `entry_Phone`, `entry_Email`, `entry_Address` for adding contact details
    - `entry_search` for searching and deleting contacts

- **Button Functions**:
    - `add_contact()`: Adds a new contact to the dictionary and updates the listbox.
    - `list_contacts()`: Lists all contacts in the console (not used in the GUI).
    - `find_contact()`: Searches for a contact by name and displays its details.
    - `delete_contact()`: Deletes a contact by name and updates the listbox.
    - `update_list()`: Updates the listbox with current contacts.

- **Buttons**:
    - `Add Contact` to add a new contact
    - `Delete Contact` to delete a contact
    - `Find Contact` to find and display a contact's details

- **Listbox**:
    - `contact_listbox` to display the list of contacts

## Error Handling

- The script includes error handling to ensure that all fields are filled before adding a contact and to handle cases where a contact is not found.

## License

This project is licensed under the MIT License.
