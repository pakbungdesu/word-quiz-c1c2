from ui import QuizInterface
from program import QuizBrian
import random
import json

# ------------------ CONSTANT ---------------------- #
THEME_COLOR = "#375362"
WHITE = "#FFFFFF"
BLACK = "#000000"
GREEN = "#E1FFBB"
RED = "#FFC5C5"
FONT = ("Arial", 15, "italic")
FONT_NAME = "Arial"
index = -1
ans = None
data = None
words = None
commands = None

# ------------------ UI SETUP -------------------- #
ui = QuizInterface()
ui.set_window("Welcome to My Quizzer!", 20, 20, THEME_COLOR)
ui.set_canvas(300, 250, WHITE)
ui.set_blank("A blank", THEME_COLOR, THEME_COLOR, FONT_NAME)


# ------------------ FUNCTION ---------------------- #

def loadjson(filename):
    """Load json from json file"""
    with open(filename, "r") as file:
        jsonf = json.load(file)
    return jsonf

def start_quiz(word_list):
    """Initialize quiz with the chosen word list."""
    global data, index
    data = word_list
    index = -1  # Reset index
    generate_question()


def show_homepage():
    """Display the homepage with word list choices."""
    ui.set_canvas(300, 250, WHITE)
    ui.write_canvas(150, 125, 280, "Choose a Word List", BLACK, FONT)
    ui.home_button("Word List 1", "Word List 2",
                   lambda: start_quiz(loadjson("w1_clean.json")),
                   lambda: start_quiz(loadjson("w2_clean.json")), THEME_COLOR)


def generate_question():
    """Randomly generate a question and update the UI."""
    global ans, commands, words, index
    index += 1

    # Prepare the question
    quiz = QuizBrian(data, index)
    quiz.setWord()
    quiz.setMeaning()
    syn_ant = random.randint(0, 1)
    quiz.setAnswer(syn_ant)
    quiz.setOther()

    meaning = quiz.getMeaning()
    ans = quiz.getAnswer()
    other = quiz.getOther()
    txt = quiz.getText() + "\n: " + meaning

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
w1 = loadjson("w1_clean.json")
w2 = loadjson("w2_clean.json")

# ------------------ START QUIZ -------------------- #
show_homepage()
ui.run()
