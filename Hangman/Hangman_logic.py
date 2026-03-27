
import random
import os

class HangmanGame:
    def __init__(self, word=None):
        if word is None:
            word = get_random_word()
        self.word = word.upper()
        self.word_show = "_" * len(self.word)
        self.try_num = 0
        self.ok_list = []
        self.no_list = []
        self.guess_history = []
        self.max_try = 7
        self.finished = False
        self.won = False

    def guess(self, ans):
        ans = ans.upper()
        if ans in self.ok_list or ans in self.no_list or len(ans) != 1 or not ans.isalpha():
            return  # 이미 시도했거나 잘못된 입력
        self.guess_history.append(ans)
        result = self.word.find(ans)
        if result == -1:
            self.try_num += 1
            self.no_list.append(ans)
        else:
            self.ok_list.append(ans)
            self.word_show = "".join(c if c in self.ok_list else "_" for c in self.word)
        if self.try_num >= self.max_try:
            self.finished = True
            self.won = False
        elif "_" not in self.word_show:
            self.finished = True
            self.won = True

    def get_display(self):
        return self.word_show

    def get_history(self):
        return self.guess_history

    def get_wrong(self):
        return self.no_list

    def get_right(self):
        return self.ok_list

    def is_finished(self):
        return self.finished

    def is_won(self):
        return self.won

    def get_word(self):
        return self.word

# read_txt.py에서 단어를 가져오는 함수 제공
def get_random_word():
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "hangman_words.txt")
    f = open(file_path, "r", encoding="utf-8")
    raw_data = f.read()
    f.close()
    data_list = raw_data.split("\n")
    data_list = [w for w in data_list if w.strip()]
    while True:
        r_index = random.randrange(0, len(data_list))
        word = data_list[r_index].replace(u"\xa0", u" ").split(" ")[-1].strip()
        if word.isascii() and word.isalpha() and 2 <= len(word) <= 6:
            return word