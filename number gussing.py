import tkinter as tk
import random

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")
        self.master.geometry("450x500")

        self.range_min = 1
        self.range_max = 100
        self.max_attempts = 10
        self.wins = 0
        self.losses = 0
        self.dark_theme = False

        self.create_widgets()
        self.reset_game()
        self.apply_theme()

    def create_widgets(self):
        self.title_label = tk.Label(self.master, text="🎯 Guess the Number!", font=("Arial", 18, "bold"))
        self.title_label.pack(pady=10)

        self.instruction = tk.Label(self.master, text="", font=("Arial", 12))
        self.instruction.pack()

        self.entry = tk.Entry(self.master, font=("Arial", 14), justify='center')
        self.entry.pack(pady=10)

        self.submit_btn = tk.Button(self.master, text="Submit Guess", font=("Arial", 12), command=self.check_guess)
        self.submit_btn.pack()

        self.feedback = tk.Label(self.master, text="", font=("Arial", 12))
        self.feedback.pack(pady=10)

        self.attempts_label = tk.Label(self.master, text="", font=("Arial", 12))
        self.attempts_label.pack()

        self.score_label = tk.Label(self.master, text="", font=("Arial", 12))
        self.score_label.pack(pady=5)

        self.restart_btn = tk.Button(self.master, text="Restart Game", font=("Arial", 12), command=self.reset_game)
        self.restart_btn.pack(pady=5)

        self.theme_btn = tk.Button(self.master, text="🌙 Toggle Theme", font=("Arial", 12), command=self.toggle_theme)
        self.theme_btn.pack(pady=5)

    def reset_game(self):
        self.secret_number = random.randint(self.range_min, self.range_max)
        self.remaining_attempts = self.max_attempts
        self.instruction.config(text=f"Guess a number between {self.range_min} and {self.range_max}")
        self.feedback.config(text="")
        self.attempts_label.config(text=f"Attempts left: {self.remaining_attempts}")
        self.score_label.config(text=f"Wins: {self.wins} | Losses: {self.losses}")
        self.entry.config(state='normal')
        self.submit_btn.config(state='normal')
        self.entry.delete(0, tk.END)

    def check_guess(self):
        guess = self.entry.get()
        if not guess.isdigit():
            self.feedback.config(text="❌ Enter a valid number!", fg="red")
            return

        guess = int(guess)
        self.remaining_attempts -= 1
        self.attempts_label.config(text=f"Attempts left: {self.remaining_attempts}")

        if guess == self.secret_number:
            self.feedback.config(text=f"🎉 Correct! The number was {self.secret_number}.", fg="green")
            self.wins += 1
            self.end_game()
        elif guess < self.secret_number:
            self.feedback.config(text="🔼 Too low!", fg="blue")
        else:
            self.feedback.config(text="🔽 Too high!", fg="blue")

        if self.remaining_attempts == 0 and guess != self.secret_number:
            self.feedback.config(text=f"💀 Out of attempts! The number was {self.secret_number}.", fg="red")
            self.losses += 1
            self.end_game()

    def end_game(self):
        self.entry.config(state='disabled')
        self.submit_btn.config(state='disabled')
        self.score_label.config(text=f"Wins: {self.wins} | Losses: {self.losses}")

    def toggle_theme(self):
        self.dark_theme = not self.dark_theme
        self.apply_theme()

    def apply_theme(self):
        bg_color = "#222222" if self.dark_theme else "#f0f0f0"
        fg_color = "#ffffff" if self.dark_theme else "#000000"

        self.master.config(bg=bg_color)
        widgets = [
            self.title_label, self.instruction, self.feedback,
            self.attempts_label, self.score_label, self.entry,
            self.submit_btn, self.restart_btn, self.theme_btn
        ]

        for widget in widgets:
            widget.config(bg=bg_color, fg=fg_color)

if __name__ == "__main__":
    root = tk.Tk()
    app = NumberGuessingGame(root)
    root.mainloop()
