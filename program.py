import random
from rich.console import Console

class Game():
    def __init__(self):
        self.total_turns = 6
        self.turns_remaining = self.total_turns
        self.console = Console(width=60)
        self.guess_results = []
        self.remaining_letters = "abcdefghijklmnopqrstuvwxyz"
        with open("words.txt", "r") as file:
            words = file.read().split(" ")
            self.word = words[random.randint(0, len(words))]
        self.console.rule("[green]Wordle[/]")

    def handle_input(self, guess):
        letters = "abcdefghijklmnopqrstuvwxyz"
        for letter in guess:
            if not letters.__contains__(letter):
                print("That's not a word!")
                return False
        if len(guess) != 6:
            print("That's not 6 letters!")
            return False
        return True

    def display_results(self):
        for guess_result in self.guess_results:
            styled_guess = " "
            for letter in guess_result:
                if letter[0] == 0:
                    # self.console.print("[bold white on green]" + letter[1].upper() + "[/]", end="")
                    styled_guess += "[bold white on green]" + letter[1].upper() + "[/]"
                elif letter[0] == 1:
                    # self.console.print("[bold white on yellow]" + letter[1].upper() + "[/]", end="")
                    styled_guess += "[bold white on yellow]" + letter[1].upper() + "[/]"
                elif letter[0] == 2:
                    # self.console.print("[bold white on grey]" + letter[1].upper() + "[/]", end="")
                    styled_guess += "[bold white on grey]" + letter[1].upper() + "[/]"
            styled_guess += " "
            self.console.print(styled_guess, justify="center")
            print()
        pass

    def check_guess(self, guess):
        guess_result = []
        for i in range(len(guess)):
            if guess[i] == self.word[i]:
                guess_result.append((0, guess[i]))
                continue
            if self.word.__contains__(guess[i]):
                guess_result.append((1, guess[i]))
                continue
            else:
                guess_result.append((2, guess[i]))
                self.remaining_letters = self.remaining_letters.replace(guess[i], "")


        self.guess_results.append(guess_result)
        self.display_results()
        if guess == self.word:
            self.console.rule("[green]Correct! The word was " + self.word + ".[/]")
            exit()

    def take_turn(self):
        self.console.rule("Guess " + str(self.total_turns - self.turns_remaining + 1), style="rule.line: white")
        self.console.print("Remaining letters: " + self.remaining_letters, justify="center")
        print()
        guess = input("Guess: ").lower()
        print()
        if not self.handle_input(guess):
            return
        self.turns_remaining -= 1
        self.check_guess(guess)

    def play(self):
        print()
        while self.turns_remaining > 0:
            self.take_turn()
        self.console.rule("[red]Loser! The correct word was " + self.word + "[/]")
        exit()

Game().play()
