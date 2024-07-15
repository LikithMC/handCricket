import tkinter as tk
from tkinter import messagebox
import random

class HandCricketGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hand Cricket")
        self.root.geometry('600x400')

        self.coach = tk.StringVar()
        self.plyrs = []
        self.compplyrs = ["Bommai", "HD Kswamy", "Siddu"]

        self.setup_ui()

    def setup_ui(self):
        # Welcome Screen
        self.welcome_frame = tk.Frame(self.root)
        self.welcome_frame.pack()

        tk.Label(self.welcome_frame, text="HI, PLEASE REGISTER YOURSELF", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.welcome_frame, text="Enter the name of the team Coach:", font=("Arial", 12)).pack(pady=5)
        tk.Entry(self.welcome_frame, textvariable=self.coach, font=("Arial", 12)).pack(pady=5)
        tk.Button(self.welcome_frame, text="Next", command=self.register_players, font=("Arial", 12)).pack(pady=20)

    def register_players(self):
        self.welcome_frame.pack_forget()
        self.register_frame = tk.Frame(self.root)
        self.register_frame.pack()

        tk.Label(self.register_frame, text="Enter the names of 3 players:", font=("Arial", 16)).pack(pady=10)

        self.player_entries = []
        for i in range(3):
            entry = tk.Entry(self.register_frame, font=("Arial", 12))
            entry.pack(pady=5)
            self.player_entries.append(entry)

        tk.Button(self.register_frame, text="Start Game", command=self.start_game, font=("Arial", 12)).pack(pady=20)

    def start_game(self):
        self.plyrs = [entry.get() for entry in self.player_entries]
        if any(not name for name in self.plyrs):
            messagebox.showwarning("Warning", "Please enter all player names.")
            return

        self.register_frame.pack_forget()
        self.game_frame = tk.Frame(self.root)
        self.game_frame.pack()

        tk.Label(self.game_frame, text=f"Welcome {self.coach.get()} to the Hand Cricket League!", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.game_frame, text="Your team members are: " + ", ".join(self.plyrs), font=("Arial", 12)).pack(pady=5)

        tk.Button(self.game_frame, text="Toss", command=self.toss, font=("Arial", 12)).pack(pady=20)

    def toss(self):
        self.toss_frame = tk.Frame(self.root)
        self.toss_frame.pack(pady=20)

        tk.Label(self.toss_frame, text="Enter Head or Tail for the purpose of toss", font=("Arial", 12)).pack(pady=5)
        self.toss_entry = tk.Entry(self.toss_frame, font=("Arial", 12))
        self.toss_entry.pack(pady=5)
        tk.Button(self.toss_frame, text="Submit", command=self.toss_result, font=("Arial", 12)).pack(pady=10)

    def toss_result(self):
        self.toss_value = self.toss_entry.get().strip().lower()
        if self.toss_value not in ["head", "tail"]:
            messagebox.showwarning("Warning", "The entered value of toss is not matching.")
            return

        self.toss_frame.pack_forget()
        self.toss_outcome = random.choice(["head", "tail"])

        if self.toss_value == self.toss_outcome:
            messagebox.showinfo("Toss Result", "You won the toss")
            self.choice_frame = tk.Frame(self.root)
            self.choice_frame.pack(pady=20)
            tk.Label(self.choice_frame, text="Bat or Bowl?", font=("Arial", 12)).pack(pady=5)
            self.choice_entry = tk.Entry(self.choice_frame, font=("Arial", 12))
            self.choice_entry.pack(pady=5)
            tk.Button(self.choice_frame, text="Submit", command=self.player_choice, font=("Arial", 12)).pack(pady=10)
        else:
            messagebox.showinfo("Toss Result", "You lost the toss. Computer chooses to bat.")
            self.bowl()

    def player_choice(self):
        choice = self.choice_entry.get().strip().lower()
        if choice == "bat":
            self.bat()
        elif choice == "bowl":
            self.bowl()
        else:
            messagebox.showwarning("Warning", "The spelling may not be correct please RE-ENTER")

    def bat(self):
        self.game_frame.pack_forget()
        self.batting_frame = tk.Frame(self.root)
        self.batting_frame.pack()

        self.current_player = 0
        self.total_runs_player = 0
        self.ball_count = 0
        self.player_runs = 0

        self.batting_ui()

    def batting_ui(self):
        self.batting_frame.pack_forget()
        self.batting_frame = tk.Frame(self.root)
        self.batting_frame.pack()

        if self.current_player < len(self.plyrs):
            player_name = self.plyrs[self.current_player]

            tk.Label(self.batting_frame, text=f"Batsman: {player_name}", font=("Arial", 14)).pack(pady=10)
            tk.Label(self.batting_frame, text=f"Ball: {self.ball_count + 1}", font=("Arial", 12)).pack(pady=5)
            tk.Label(self.batting_frame, text=f"Runs: {self.player_runs}", font=("Arial", 12)).pack(pady=5)
            tk.Label(self.batting_frame, text="Enter your batting hit (1-6):", font=("Arial", 12)).pack(pady=5)
            self.batting_entry = tk.Entry(self.batting_frame, font=("Arial", 12))
            self.batting_entry.pack(pady=5)
            tk.Button(self.batting_frame, text="Hit", command=self.batting_hit, font=("Arial", 12)).pack(pady=10)
        else:
            self.batting_frame.pack_forget()
            self.bowl()

    def batting_hit(self):
        hit = self.batting_entry.get().strip()
        if not hit.isdigit() or not (1 <= int(hit) <= 6):
            messagebox.showwarning("Warning", "The entered value is not within range 1-6.")
            return

        hit = int(hit)
        ball = random.randint(1, 6)

        if hit == ball:
            messagebox.showinfo("Out", f"Player {self.plyrs[self.current_player]} is out!")
            self.total_runs_player += self.player_runs
            self.current_player += 1
            self.ball_count = 0
            self.player_runs = 0
        else:
            self.player_runs += hit
            self.ball_count += 1

            if self.ball_count >= 6:
                messagebox.showinfo("Over", f"Player {self.plyrs[self.current_player]}'s over is completed.")
                self.total_runs_player += self.player_runs
                self.current_player += 1
                self.ball_count = 0
                self.player_runs = 0

        self.batting_ui()

    def bowl(self):
        self.game_frame.pack_forget()
        self.bowling_frame = tk.Frame(self.root)
        self.bowling_frame.pack()

        self.current_computer = 0
        self.total_runs_computer = 0
        self.ball_count = 0
        self.computer_runs = 0

        self.bowling_ui()

    def bowling_ui(self):
        self.bowling_frame.pack_forget()
        self.bowling_frame = tk.Frame(self.root)
        self.bowling_frame.pack()

        if self.current_computer < len(self.compplyrs):
            computer_name = self.compplyrs[self.current_computer]

            tk.Label(self.bowling_frame, text=f"Batsman: {computer_name}", font=("Arial", 14)).pack(pady=10)
            tk.Label(self.bowling_frame, text=f"Ball: {self.ball_count + 1}", font=("Arial", 12)).pack(pady=5)
            tk.Label(self.bowling_frame, text=f"Runs: {self.computer_runs}", font=("Arial", 12)).pack(pady=5)
            tk.Label(self.bowling_frame, text="Enter your bowling hit (1-6):", font=("Arial", 12)).pack(pady=5)
            self.bowling_entry = tk.Entry(self.bowling_frame, font=("Arial", 12))
            self.bowling_entry.pack(pady=5)
            tk.Button(self.bowling_frame, text="Bowl", command=self.bowling_hit, font=("Arial", 12)).pack(pady=10)
        else:
            self.bowling_frame.pack_forget()
            self.show_result(self.total_runs_player, self.total_runs_computer)

    def bowling_hit(self):
        hit = self.bowling_entry.get().strip()
        if not hit.isdigit() or not (1 <= int(hit) <= 6):
            messagebox.showwarning("Warning", "The entered value is not within range 1-6.")
            return

        hit = int(hit)
        ball = random.randint(1, 6)

        if hit == ball:
            messagebox.showinfo("Out", f"Player {self.compplyrs[self.current_computer]} is out!")
            self.total_runs_computer += self.computer_runs
            self.current_computer += 1
            self.ball_count = 0
            self.computer_runs = 0
        else:
            self.computer_runs += ball
            self.ball_count += 1

            if self.ball_count >= 6:
                messagebox.showinfo("Over", f"Player {self.compplyrs[self.current_computer]}'s over is completed.")
                self.total_runs_computer += self.computer_runs
                self.current_computer += 1
                self.ball_count = 0
                self.computer_runs = 0

        self.bowling_ui()

    def show_result(self, totalrunsplayer, totalrunscomp):
        self.result_frame = tk.Frame(self.root)
        self.result_frame.pack(pady=20)

        if totalrunscomp > totalrunsplayer:
            m = f"Computer won by {totalrunscomp - totalrunsplayer} runs"
        else:
            m = f"You won by {totalrunsplayer - totalrunscomp} runs"
        
        m2 = "Thank You"
        
        tk.Label(self.result_frame, text=m, fg="lime", bg="black", width="100", height="2").pack(pady=10)
        tk.Label(self.result_frame, text=m2, fg="black", bg="lime", width="100", height="2").pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    game = HandCricketGame(root)
    root.mainloop()