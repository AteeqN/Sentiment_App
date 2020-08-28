import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import *
import pickle
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import re, string, random
from nltk.stem.wordnet import WordNetLemmatizer


class My_Dialog(QDialog):
    def __init__(self):
        super(My_Dialog, self).__init__()
        loadUi("dialog.ui", self)
        # self.mid_label.setText(My_Window.mid_label_nexttext)

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('view.ui', self)

        self.setWindowTitle("My App")

        self.button = self.findChild(QtWidgets.QPushButton, 'classifyBtn')
        self.input_txt = self.findChild(QtWidgets.QLineEdit, 'input_line')
        self.display_text = self.findChild(QtWidgets.QTextEdit, 'showResult')
        self.dis = self.findChild(QtWidgets.QTextEdit, 'editText')
        # self.textedit = QtWidgets.QTextEdit(readOnly=True)
        self.button.clicked.connect(self.classifyButtonPressed)

        self.show()

    def remove_noise(self, tweet_tokens, stop_words=()):

        cleaned_tokens = []

        for token, tag in pos_tag(tweet_tokens):
            token = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|[(/)+]' \
                           '(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', token)
            token = re.sub("(@[A-Za-z0-9_]+)", "", token)

            if tag.startswith("NN"):
                pos = 'n'
            elif tag.startswith('VB'):
                pos = 'v'
            else:
                pos = 'a'

            lemmatizer = WordNetLemmatizer()
            token = lemmatizer.lemmatize(token, pos)

            if len(token) > 0 and token not in string.punctuation and token.lower() not in stop_words:
                cleaned_tokens.append(token.lower())
        return cleaned_tokens

    def classifyButtonPressed(self):
        # print("classifyButtonPressed")
        self.textfromfield = self.input_txt.text()
        # self.extractText = self.display_text.get()
        # print(self.extractText)
        # sys.exit(0)
        # self.resultText = self.display_text.setText()
        # print(self.resultText)
        # print(self.textfromfield)

        with open('model_save_weight/model_train1/my_classifier.pickle', 'rb') as cfile:
            Naive_Classifier = pickle.load(cfile)

            custom_tokens = self.remove_noise(word_tokenize(self.textfromfield))
            # print(custom_tokens)

            self.result = Naive_Classifier.classify(dict([token, True] for token in custom_tokens))

            QMessageBox.question(self, 'Alert Message', " Sentiment: " + self.result, QMessageBox.Ok, QMessageBox.Ok)

app = QtWidgets.QApplication(sys.argv)
main_screen = Ui()
app.exec_()
