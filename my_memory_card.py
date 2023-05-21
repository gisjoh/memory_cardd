#создай приложение для запоминания информации
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QRadioButton, QGroupBox, QVBoxLayout, QHBoxLayout, QButtonGroup,  QMessageBox
)
from random import shuffle

app=QApplication([])
window=QWidget()
lbl_question = QLabel('Сколько дней в году имеет 28 дней?')
rbtn_1 = QRadioButton('Ни один')
rbtn_2 = QRadioButton('Один')
rbtn_3 = QRadioButton('Два')
rbtn_4 = QRadioButton('Три')
btn_next = QPushButton('Ответить')
grpbox_anwers = QGroupBox('Ответы')
grpbox_result = QGroupBox('Результат')
lbl_result = QLabel('Вы ответили правильно!')
lbl_right_anwers = QLabel('Все')
grpbox_result.hide()


btn_group = QButtonGroup()
btn_group.addButton(rbtn_1)
btn_group.addButton(rbtn_2)
btn_group.addButton(rbtn_3)
btn_group.addButton(rbtn_4)

v_result = QVBoxLayout()
v_result.addWidget(lbl_result)
v_result.addWidget(lbl_right_anwers)
grpbox_result.setLayout(v_result)

v_main = QVBoxLayout()
h_main_1 = QHBoxLayout()
h_main_2 = QHBoxLayout()
h_main_3 = QHBoxLayout()

h_grpbox = QHBoxLayout()
v_grpbox_1 = QVBoxLayout()
v_grpbox_2 = QVBoxLayout()

h_main_1.addWidget(lbl_question)
h_main_2.addWidget(grpbox_anwers)
h_main_2.addWidget(grpbox_result)
h_main_3.addWidget(btn_next)

v_grpbox_1.addWidget(rbtn_1)
v_grpbox_1.addWidget(rbtn_2)
v_grpbox_2.addWidget(rbtn_3)
v_grpbox_2.addWidget(rbtn_4)

h_grpbox.addLayout(v_grpbox_1)
h_grpbox.addLayout(v_grpbox_2)

v_main.addLayout(h_main_1)
v_main.addLayout(h_main_2)
v_main.addLayout(h_main_3)

grpbox_anwers.setLayout(h_grpbox)
window.setLayout(v_main)

class Question:
    def __init__(self, question, right_anwers, wrong1, wrong2, wrong3):
        self.question = question
        self.right_anwers = right_anwers
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

def ask(_q):
    shuffle(buttons)
    buttons[0].setText(_q.right_anwers)
    buttons[1].setText(_q.wrong1)
    buttons[2].setText(_q.wrong2)
    buttons[3].setText(_q.wrong3)
    lbl_question.setText(_q.question)
    lbl_right_anwers.setText('Правильно: ' +_q.right_anwers)
    show_question()

def get_procent(score):
    procent = score / len(questions)*100
    procent = round(procent, 1)
    result = 'Вы ответили на ' + str(score)
    result += ' вопросов из ' + str(len(questions)) + '\n'
    result += 'Процент верных ответов ' + str(procent)
    return result
    
cur_question = 0
score = 0
buttons = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
questions = [
    Question('Сколько градусов сегодня?', '10','-100','-196','5000'),
    Question('Какой сегодня день?', 'четверг','пятница','суббота','воскресенье'),
    Question('Что из этого фрукт?', 'яблоко','морковка','лук','тыква'),
    Question('Сколько мне лет?', '15','10','11','13')
]

def next_question():
    global cur_question, score
    cur_question += 1
    if cur_question >= len(questions):
        msg = QMessageBox()
        msg.setText(get_procent(score))
        msg.setWindowTitle('Результат')
        msg.exec()
        cur_question = 0
        score = 0
    ask(questions[cur_question])

def show_result():
    if is_all_checked():
        if buttons[0].isChecked():
            global score
            score += 1
            lbl_result.setText('Вы ответили правильно!')
        else:
            lbl_result.setText('Вы ответили неправильно!')
        grpbox_anwers.hide()
        grpbox_result.show()
        btn_next.setText('Следующий вопрос')

def show_question():
    grpbox_anwers.show()
    grpbox_result.hide()
    btn_next.setText('Ответить')
    btn_group.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    btn_group.setExclusive(True)

def is_all_checked():
    flag = False
    for btn in buttons:
        if btn.isChecked():
            flag = True
    return flag

def click_next():
    if btn_next.text() == 'Ответить':
        show_result()
    else:
        next_question()
btn_next.clicked.connect(click_next)

ask(questions[cur_question])

window.setLayout(v_main)
window.show()
app.exec()
