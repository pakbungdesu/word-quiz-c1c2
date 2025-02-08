
import random

class QuizBrian:
    def __init__(self, data, idx):
        self.data = data
        self.idx = idx
        self.guess = None
        self.meaning = None
        self.ans = None
        self.other = None
        self.txt = None

    def setWord(self):
        self.guess = self.data[self.idx]["word"]

    def setMeaning(self):
        self.meaning = self.data[self.idx]["meaning"]

    def setAnswer(self, choice):  # 1 for synonym, 0 for antonym
        if choice == 1:
            self.ans = random.choice(self.data[self.idx]["synonyms"])
            self.txt = f"Pick a synonym of {self.guess}"
        else:
            self.ans = random.choice(self.data[self.idx]["antonyms"])
            self.txt = f"Pick an antonym of {self.guess}"

    def setOther(self):
        self.other = []
        while len(self.other) < 3:
            rand_idx = random.randint(0, len(self.data) - 1)

            if rand_idx != self.idx and rand_idx not in self.other:
                if rand_idx % 2 == 1:
                    self.other.append(random.choice(self.data[rand_idx]["synonyms"]))
                else:
                    self.other.append(random.choice(self.data[rand_idx]["antonyms"]))

    def getGuess(self):
        return self.guess

    def getMeaning(self):
        return self.meaning

    def getAnswer(self):
        return self.ans

    def getText(self):
        return self.txt

    def getOther(self):
        return self.other
