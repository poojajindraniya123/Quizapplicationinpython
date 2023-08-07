import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")

        self.questions = [
            {
                'question': 'What is the capital of France?',
                'choices': ['Paris', 'Berlin', 'London', 'Madrid'],
                'correct_answer': 'Paris'
            },
            {
                'question': 'Which planet is known as the Red Planet?',
                'choices': ['Venus', 'Mars', 'Jupiter', 'Saturn'],
                'correct_answer': 'Mars'
            },
            {
                'question': 'What is the largest mammal?',
                'choices': ['Elephant', 'Blue Whale', 'Giraffe', 'Hippopotamus'],
                'correct_answer': 'Blue Whale'
            }
            # Add more questions here
        ]

        self.question_index = 0
        self.score = 0

        self.question_label = tk.Label(root, text='', wraplength=300)
        self.question_label.pack(pady=10)

        self.choice_buttons = []
        for i in range(4):
            button = tk.Button(root, text='', command=lambda i=i: self.check_answer(i))
            button.pack(pady=5)
            self.choice_buttons.append(button)

        self.next_question()

    def next_question(self):
        if self.question_index < len(self.questions):
            question = self.questions[self.question_index]
            self.question_label.config(text=question['question'])

            for i, choice in enumerate(question['choices']):
                self.choice_buttons[i].config(text=choice)
            
            self.question_index += 1
        else:
            self.show_score()

    def check_answer(self, choice_index):
        question = self.questions[self.question_index - 1]
        selected_choice = question['choices'][choice_index]

        if selected_choice == question['correct_answer']:
            self.score += 1

        self.next_question()

    def show_score(self):
        messagebox.showinfo("Quiz Completed", f"Your final score is: {self.score}/{len(self.questions)}")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
