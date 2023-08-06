import tkinter as tk
from tkinter import messagebox

class LibraryManagementSystem:
    def _init_(self, root):
        self.root = root
        self.root.title("Library Management System")

        self.books = []

        self.label_title = tk.Label(root, text="Library Management System", font=("Helvetica", 16))
        self.label_title.pack(pady=10)

        self.label_book_name = tk.Label(root, text="Book Name:")
        self.label_book_name.pack()
        self.entry_book_name = tk.Entry(root)
        self.entry_book_name.pack()

        self.label_author = tk.Label(root, text="Author:")
        self.label_author.pack()
        self.entry_author = tk.Entry(root)
        self.entry_author.pack()

        self.btn_add_book = tk.Button(root, text="Add Book", command=self.add_book)
        self.btn_add_book.pack(pady=5)

        self.btn_delete_book = tk.Button(root, text="Delete Book", command=self.delete_book)
        self.btn_delete_book.pack(pady=5)

        self.label_books = tk.Label(root, text="Books in Library:")
        self.label_books.pack()
        self.listbox_books = tk.Listbox(root)
        self.listbox_books.pack()

    def add_book(self):
        book_name = self.entry_book_name.get()
        author = self.entry_author.get()

        if book_name and author:
            self.books.append((book_name, author))
            self.listbox_books.insert(tk.END, f"{book_name} by {author}")
            messagebox.showinfo("Success", "Book added successfully.")
            self.entry_book_name.delete(0, tk.END)
            self.entry_author.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter both book name and author.")

    def delete_book(self):
        selected_index = self.listbox_books.curselection()
        if selected_index:
            index = selected_index[0]
            self.listbox_books.delete(index)
            del self.books[index]
            messagebox.showinfo("Success", "Book deleted successfully.")
        else:
            messagebox.showerror("Error", "Please select a book to delete.")

def main():
    root = tk.Tk()
    app = LibraryManagementSystem(root)
    root.mainloop()

if  __name__ == "_main_":
    main()