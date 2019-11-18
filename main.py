import json
import random

def get_dictionary():
    with open("dict.json", "r") as dict_file:
        contents = dict_file.read()
    return json.loads(contents)

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

class TypingMonkey:

    def __init__(self, gene_pool=None):
        gene_pool = gene_pool or ALPHABET
        self.alphabet = random.sample(gene_pool, 10)

    def write_word(self):
        return "".join([random.choice(self.alphabet) for _ in range(80)])

    def write(self):
        monkey_text = ""
        for i in range(20):
            chars = 0
            line = ""
            while len(line) < 80:
                line += self.write_word()

            monkey_text += line
        return monkey_text

class WordMonkey:

    def __init__(self, words):
        self.words = words

    def write_word(self):
        return random.choice(self.words)

    def write(self):
        line = ""
        for i in range(20):
            chars = 0
            line = ""
            while len(line) < 80:
                line += self.write_word() + " "
        return line

def get_allowed_words(text):
    allowed_words = []
    for k, v in get_dictionary().items():
        if k.lower() in text:
            if "Obs." in v or "English alphabet" in v:
                continue
            allowed_words.append(k.lower())
    return allowed_words


def reproduce(monkey_a, monkey_b, number_of_children):
    gene_pool = set(monkey_a.alphabet + monkey_b.alphabet)
    return [TypingMonkey(gene_pool) for _ in range(number_of_children)]


def main():
    best_monkey = [0, None]
    second_best_monkey = [0, None]

    # Initial population
    monkeys = [TypingMonkey() for _ in range(5)]
    for gen in range(8):
        best_monkey = [0, None]
        second_best_monkey = [0, None]
        for i, tm in enumerate(monkeys):
            print(f"Monkey {i}")
            monkey_text = tm.write()

            wm = WordMonkey(get_allowed_words(monkey_text))

            words = wm.write()
            score = len(words)
            if score > best_monkey[0]:
                best_monkey = [score, tm]
            elif score > second_best_monkey[0]:
                second_best_monkey = [score, tm]

        print(f"Strongest monkeys of generation {gen}")
        print(best_monkey)
        print(second_best_monkey)

        monkeys = reproduce(best_monkey[1], second_best_monkey[1], 5)

if __name__ == "__main__":
    main()
