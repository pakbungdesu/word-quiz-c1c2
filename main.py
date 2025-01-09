from ui import QuizInterface
from program import QuizBrian
import json
import random

# ------------------ CONSTANT ---------------------- #
THEME_COLOR = "#375362"
WHITE = "#FFFFFF"
BLACK = "#000000"
GREEN = "#E1FFBB"
RED = "#FFC5C5"
FONT = ("Arial", 15, "italic")
FONT_NAME = "Arial"
ans = None
commands = None
words = None


# ------------------ UI SETUP -------------------- #
ui = QuizInterface()
ui.set_window("My Quizzer", 20, 20, THEME_COLOR)
ui.set_canvas(300, 250, WHITE)
ui.set_blank("A blank", THEME_COLOR, THEME_COLOR, FONT_NAME)


# ------------------ FUNCTION ---------------------- #
def generate_question():
    """Randomly generate a question and update the UI."""
    global ans, commands, words

    # Choose data source randomly
    c1_c2 = random.randint(0, 1)
    data = c1 if c1_c2 == 1 else c2

    # Prepare the question
    myc = QuizBrian(data)
    myc.setWord()
    syn_ant = random.randint(0, 1)
    myc.setAnswer(syn_ant)
    myc.setOther()

    ans = myc.getAnswer()
    other = myc.getOther()
    txt = myc.getText()

    # Shuffle answers
    words = other + [ans]
    random.shuffle(words)

    # Generate commands for buttons
    commands = [lambda t=text: button_click(t, ans) for text in words]

    # Update UI with the new question
    ui.set_canvas(300, 250, WHITE)
    ui.set_button(words[0], words[1], words[2], words[3], THEME_COLOR, commands)
    ui.write_canvas(150, 125, 280, txt, BLACK, FONT)


def button_click(text, answer):
    """Handle button click and randomize the next question."""
    if text == answer:
        ui.set_canvas(300, 250, GREEN)
        ui.write_canvas(150, 125, 280, "Right!", BLACK, FONT)
    else:
        ui.set_canvas(300, 250, RED)
        ui.write_canvas(150, 125, 280, f"Wrong! The answer is {answer}", BLACK, FONT)

    # Wait a moment and randomize the next question
    ui.window.after(1000, generate_question)


# ------------------ LOAD DATA -------------------- #
with open("c1_clean.json", "r") as file:
    c1 = json.load(file)

with open("c2_clean.json", "r") as file:
    c2 = json.load(file)


# ------------------ START QUIZ -------------------- #
generate_question()
ui.run()
