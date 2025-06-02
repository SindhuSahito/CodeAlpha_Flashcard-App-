import tkinter as tk
from tkinter import simpledialog, messagebox

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flashcard Quiz App")
        self.flashcards = [
            {"question": "What is the capital of France?", "answer": "Paris"},
            {"question": "What is 2 + 2?", "answer": "4"},
            {"question": "Who are you?", "answer": "Just an App"},
            {"question": "Do you like coding?", "answer": "Yup"},

        ]
        self.index = 0
        self.showing_answer = False

        self.show_welcome_screen()

    def show_welcome_screen(self):
        self.clear_screen()
        welcome_label = tk.Label(self.root, text="Welcome to the Flashcard Quiz App!", font=("Arial", 18))
        welcome_label.pack(pady=30)

        start_button = tk.Button(self.root, text="Start Quiz", font=("Arial", 14), command=self.show_flashcards)
        start_button.pack(pady=20)

    def show_flashcards(self):
        self.clear_screen()

        self.card_text = tk.Label(self.root, text="", width=40, height=5, font=("Arial", 16), wraplength=300)
        self.card_text.pack(pady=20)

        btn_frame = tk.Frame(self.root)
        btn_frame.pack()

        tk.Button(btn_frame, text="Previous", command=self.prev_card).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Show Answer", command=self.toggle_answer).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Next", command=self.next_card).grid(row=0, column=2, padx=5)

        edit_frame = tk.Frame(self.root)
        edit_frame.pack(pady=10)

        tk.Button(edit_frame, text="Add", command=self.add_card).grid(row=0, column=0, padx=5)
        tk.Button(edit_frame, text="Edit", command=self.edit_card).grid(row=0, column=1, padx=5)
        tk.Button(edit_frame, text="Delete", command=self.delete_card).grid(row=0, column=2, padx=5)

        self.update_card()

    def update_card(self):
        if not self.flashcards:
            self.card_text.config(text="No flashcards available.")
        else:
            current = self.flashcards[self.index]
            text = current["answer"] if self.showing_answer else current["question"]
            self.card_text.config(text=text)

    def toggle_answer(self):
        self.showing_answer = not self.showing_answer
        self.update_card()

    def next_card(self):
        if self.flashcards:
            self.index = (self.index + 1) % len(self.flashcards)
            self.showing_answer = False
            self.update_card()

    def prev_card(self):
        if self.flashcards:
            self.index = (self.index - 1) % len(self.flashcards)
            self.showing_answer = False
            self.update_card()

    def add_card(self):
        q = simpledialog.askstring("Add Flashcard", "Enter the question:")
        a = simpledialog.askstring("Add Flashcard", "Enter the answer:")
        if q and a:
            self.flashcards.append({"question": q, "answer": a})
            self.index = len(self.flashcards) - 1
            self.showing_answer = False
            self.update_card()

    def edit_card(self):
        if not self.flashcards:
            return
        current = self.flashcards[self.index]
        q = simpledialog.askstring("Edit Flashcard", "Edit the question:", initialvalue=current["question"])
        a = simpledialog.askstring("Edit Flashcard", "Edit the answer:", initialvalue=current["answer"])
        if q and a:
            self.flashcards[self.index] = {"question": q, "answer": a}
            self.showing_answer = False
            self.update_card()

    def delete_card(self):
        if not self.flashcards:
            return
        del self.flashcards[self.index]
        self.index = max(0, self.index - 1)
        self.showing_answer = False
        self.update_card()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Run the app
root = tk.Tk()
app = FlashcardApp(root)
root.mainloop()
