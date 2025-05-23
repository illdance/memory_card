from PyQt5.QtCore  import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QButtonGroup, QHBoxLayout, QGroupBox, QRadioButton
from random import shuffle
from random import choice

class Question():
    def __init__(self, q, r_a, w_a1, w_a2, w_a3):
        self.winnower = q
        self.right_answer = r_a
        self.wrong_answer1 = w_a1
        self.wrong_answer2 = w_a2
        self.wrong_answer3 = w_a3

def next_skibidi():
    random_question = choice(questions)
    ask(random_question)

def ask(q: Question):
    shuffle(buttons)
    buttons[0].setText(q.right_answer)
    buttons[1].setText(q.wrong_answer1)
    buttons[2].setText(q.wrong_answer2)    
    buttons[3].setText(q.wrong_answer3)
    winnower.setText(q.winnower)
    right_ans.setText(q.right_answer)
    show_question()

def check_answer():
    if buttons[0].isChecked():
        right_wrong.setText('Правильно! Поздравляем!')
        windower.correct_answer += 1
        windower.total_question += 1
        rating = windower.correct_answer/windower.total_question * 100
        print('Кол-во правильных ответов:', windower.correct_answer, '\n', 'Кол-во вопросов:', windower.total_question, '\n', 'Рейтинг:', rating, '%')
        show_result()
    elif buttons[1].isChecked() or buttons[2].isChecked() or buttons[3].isChecked():
        right_wrong.setText("Неправильно! Позор!")
        windower.total_question += 1
        rating = windower.correct_answer/windower.total_question * 100
        print('Кол-во правильных ответов:', windower.correct_answer, '\n', 'Кол-во вопросов:', windower.total_question, '\n', 'Рейтинг:', rating, '%')
        show_result()

def show_result():
    gruppe.hide()
    otv_gruppe.show()
    bution.setText('Следующий вопрос')

def show_question():
    otv_gruppe.hide()
    gruppe.show()
    bution.setText('Ответить')
    radioGruppe.setExclusive(False)
    otv1.setChecked(False)
    otv2.setChecked(False)
    otv3.setChecked(False)
    otv4.setChecked(False)
    radioGruppe.setExclusive(True)

def start_test():
    if bution.text() == 'Ответить':
        check_answer()
    elif bution.text() == ('Следующий вопрос'):
        ask(questions[0])
        next_skibidi()

app = QApplication([])
windower = QWidget()
windower.correct_answer = 0
windower.total_question = 0


windower.setWindowTitle('Memo Card')
windower.resize(500, 225)
winnower = QLabel('Какая национальность существует?')
ans_v_line = QVBoxLayout()

bution = QPushButton('Ответить')

gruppe = QGroupBox('Варианты')

otv_gruppe = QGroupBox('Результат теста')
otv_gruppe.hide()
right_ans = QLabel('Правильный ответ')
right_wrong = QLabel('Правильно/неправильно')
ans_v_line.addWidget(right_wrong)
ans_v_line.addWidget(right_ans, alignment = Qt.AlignCenter)
otv_gruppe.setLayout(ans_v_line)
v_line = QVBoxLayout()
h_line = QHBoxLayout()
h_line1 = QHBoxLayout()
h_line2 = QHBoxLayout()
h_line.addWidget(winnower, alignment = Qt.AlignCenter)
h_line1.addWidget(gruppe, alignment = Qt.AlignCenter)
h_line1.addWidget(otv_gruppe)
h_line2.addStretch(1)
h_line2.addWidget(bution, stretch = 2)
h_line2.addStretch(1)

v_line.addLayout(h_line)
v_line.addLayout(h_line1)
v_line.addLayout(h_line2)

otv1 = QRadioButton('Хайлицы')
otv2 = QRadioButton('Шайлушаи')
otv3 = QRadioButton('Татаро-Монголы')
otv4 = QRadioButton('Пупсы')

buttons = [otv1, otv2, otv3, otv4]
shuffle(buttons)

grH_line = QHBoxLayout()
grV_line1 = QVBoxLayout()
grV_line2 = QVBoxLayout()

radioGruppe = QButtonGroup()
radioGruppe.addButton(otv1)
radioGruppe.addButton(otv2)
radioGruppe.addButton(otv3)
radioGruppe.addButton(otv4)

grH_line.addLayout(grV_line1)
grH_line.addLayout(grV_line2)

grV_line1.addWidget(otv1, alignment = Qt.AlignCenter)
grV_line1.addWidget(otv3, alignment = Qt.AlignCenter)
grV_line2.addWidget(otv2, alignment = Qt.AlignCenter)
grV_line2.addWidget(otv4, alignment = Qt.AlignCenter)

bution.clicked.connect(start_test)
windower.setLayout(v_line)
gruppe.setLayout(grH_line)

questions = []
questions.append(Question("Кем ты являешься?", "Пупс!", "Пупсимен...", "АНТИПУПС!", "Человек"))
questions.append(Question("Сколько дней в году?(на марсе)", "686.94", "365", "1365.23", "100.37"))
questions.append(Question("Способностью быстрой смены чего славятся хамелеоны?", "Цветов", "Шнурков", "Обуви", "Шляп"))
questions.append(Question("Какое мясо используется для супа харчо?", "Баранина", "Свинина", "Курица", "Телятина"))
questions.append(Question("Какой мифологический царь сумел разгадать загадку сфинкса, после чего та сбросилась со скалы и разбилась?", "Эдит", "Одиссей", "Креорс", "Парис"))

next_skibidi()

windower.show()
app.exec_()