import tkinter as tk
from tkinter import messagebox

class ContactBookApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Contact Book")
        
        self.contacts = {}

        self.create_widgets()

    def create_widgets(self):
        # Labels
        tk.Label(self.master, text="Name:").grid(row=0, column=0, sticky="e")
        tk.Label(self.master, text="Phone:").grid(row=1, column=0, sticky="e")
        tk.Label(self.master, text="Email:").grid(row=2, column=0, sticky="e")
        tk.Label(self.master, text="Address:").grid(row=3, column=0, sticky="e")

        # Entry fields
        self.name_entry = tk.Entry(self.master)
        self.name_entry.grid(row=0, column=1)
        self.phone_entry = tk.Entry(self.master)
        self.phone_entry.grid(row=1, column=1)
        self.email_entry = tk.Entry(self.master)
        self.email_entry.grid(row=2, column=1)
        self.address_entry = tk.Entry(self.master)
        self.address_entry.grid(row=3, column=1)

        # Buttons
        tk.Button(self.master, text="Add Contact", command=self.add_contact).grid(row=4, column=0, columnspan=2, pady=10)
        tk.Button(self.master, text="View Contact List", command=self.view_contact_list).grid(row=5, column=0, columnspan=2, pady=10)
        tk.Button(self.master, text="Search Contact", command=self.search_contact).grid(row=6, column=0, columnspan=2, pady=10)
        tk.Button(self.master, text="Update Contact", command=self.update_contact).grid(row=7, column=0, columnspan=2, pady=10)
        tk.Button(self.master, text="Delete Contact", command=self.delete_contact).grid(row=8, column=0, columnspan=2, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name.strip() == "":
            messagebox.showerror("Error", "Name cannot be empty!")
            return

        if name in self.contacts:
            messagebox.showerror("Error", "Contact already exists!")
            return

        self.contacts[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }

        messagebox.showinfo("Success", "Contact added successfully!")

    def view_contact_list(self):
        if not self.contacts:
            messagebox.showinfo("Info", "No contacts available.")
            return

        contact_list = "Contact List:\n\n"
        for name, details in self.contacts.items():
            contact_list += f"Name: {name}\nPhone: {details['phone']}\nEmail: {details['email']}\nAddress: {details['address']}\n\n"

        messagebox.showinfo("Contact List", contact_list)

    def search_contact(self):
        search_name = tk.simpledialog.askstring("Search Contact", "Enter name to search:")
        if search_name:
            if search_name in self.contacts:
                details = self.contacts[search_name]
                messagebox.showinfo("Search Result", f"Name: {search_name}\nPhone: {details['phone']}\nEmail: {details['email']}\nAddress: {details['address']}")
            else:
                messagebox.showinfo("Info", "Contact not found.")

    def update_contact(self):
        name = tk.simpledialog.askstring("Update Contact", "Enter name to update:")
        if name:
            if name in self.contacts:
                phone = self.phone_entry.get()
                email = self.email_entry.get()
                address = self.address_entry.get()

                self.contacts[name] = {
                    "phone": phone,
                    "email": email,
                    "address": address
                }

                messagebox.showinfo("Success", "Contact updated successfully!")
            else:
                messagebox.showinfo("Info", "Contact not found.")

    def delete_contact(self):
        name = tk.simpledialog.askstring("Delete Contact", "Enter name to delete:")
        if name:
            if name in self.contacts:
                del self.contacts[name]
                messagebox.showinfo("Success", "Contact deleted successfully!")
            else:
                messagebox.showinfo("Info", "Contact not found.")

def main():
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
