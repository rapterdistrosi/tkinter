import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game 🎮")
        self.root.geometry("400x300")

        # Difficulty settings
        self.difficulty_var = tk.StringVar(value="Medium")
        difficulty_frame = tk.Frame(root)
        tk.Label(difficulty_frame, text="Difficulty:").pack(side=tk.LEFT)
        for level in ["Easy", "Medium", "Hard"]:
            tk.Radiobutton(difficulty_frame, text=level, variable=self.difficulty_var, value=level).pack(side=tk.LEFT)
        difficulty_frame.pack(pady=5)

        self.label = tk.Label(root, text="Guess the number:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, justify='center')
        self.entry.pack()

        self.submit_button = tk.Button(root, text="Submit Guess", command=self.check_guess)
        self.submit_button.pack(pady=5)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

        self.restart_button = tk.Button(root, text="Restart Game", command=self.reset_game)
        self.restart_button.pack(pady=5)

        self.reset_game()

    def get_range(self):
        difficulty = self.difficulty_var.get()
        if difficulty == "Easy":
            return 1, 50
        elif difficulty == "Medium":
            return 1, 100
        else:
            return 1, 200

    def reset_game(self):
        min_val, max_val = self.get_range()
        self.number_to_guess = random.randint(min_val, max_val)
        self.attempts = 0
        self.result_label.config(text=f"Enter a number between {min_val} and {max_val}.")
        self.entry.delete(0, tk.END)
        print(f"[DEBUG] New number: {self.number_to_guess}")

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1
            if guess < self.number_to_guess:
                self.result_label.config(text="Too low! Try again.")
            elif guess > self.number_to_guess:
                self.result_label.config(text="Too high! Try again.")
            else:
                messagebox.showinfo("Correct!", f"You guessed it in {self.attempts} attempts!")
                self.reset_game()
        except ValueError:
            self.result_label.config(text="Please enter a valid number.")

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
