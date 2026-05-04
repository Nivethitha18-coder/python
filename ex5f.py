class InvalidOptionError(Exception):
    pass

class Quiz:
    def __init__(self):
        # Questions (8 questions)
        self.questions = [
            "1. Largest planet?\nA. Earth\nB. Mars\nC. Jupiter",
            "2. 5 + 3 = ?\nA. 6\nB. 8\nC. 9",
            "3. Capital of India?\nA. Mumbai\nB. Delhi\nC. Chennai",
            "4. Water formula?\nA. CO2\nB. H2O\nC. O2",
            "5. Sun is a?\nA. Planet\nB. Star\nC. Satellite",
            "6. 10 - 4 = ?\nA. 6\nB. 5\nC. 4",
            "7. National animal of India?\nA. Lion\nB. Tiger\nC. Elephant",
            "8. Which is a programming language?\nA. Python\nB. Snake\nC. Cobra"
        ]

        # Correct answers
        self.answers = ['C', 'B', 'B', 'B', 'B', 'A', 'B', 'A']

        # score variable
        self.score = 0

    def start_quiz(self):
        for i in range(len(self.questions)):
            try:
                print(self.questions[i])
                user_ans = input("Enter option (A/B/C): ").upper()

                # check invalid input
                if user_ans not in ['A', 'B', 'C']:
                    raise InvalidOptionError

                # check correct answer
                if user_ans == self.answers[i]:
                    print("Correct!\n")
                    self.score += 1
                else:
                    print("Wrong!\n")

            except InvalidOptionError:
                print("Invalid Option Selected! Please enter A, B, or C.\n")

    def display_score(self):
        print("Your Final Score is:", self.score, "/", len(self.questions))


# Create Object and call methods
obj = Quiz()
obj.start_quiz()
obj.display_score()