from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QButtonGroup, QGroupBox, QWidget, QPushButton, QLabel, QVBoxLayout, QMessageBox, QRadioButton, QHBoxLayout
from random import shuffle, randint

class questionn():
    def __init__(self, question1, right, wrong1, wrong2, wrong3):
        self.question1 = question1
        self.right = right
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

qwst = list()
qwst.append(questionn('Государственный язык Бразилии', 'Португальский', 'Бразильский', 'Испанский', 'Итальянский'))
qwst.append(questionn('Какая страна является самой большой по площади в мире?', 'Россия', 'Канада', 'Китай', 'США'))
qwst.append(questionn('В какой стране находится город Тимбукту?', 'Мали', 'Египет', 'Марокко', 'Кения'))
qwst.append(questionn('Какая река считается самой длинной в мире?', 'Амазонка', 'Нил', 'Миссисипи', 'Янцзы'))
qwst.append(questionn('Столицей какого государства является город Оттава?', 'Канада', 'Австралия', 'Новая Зеландия', 'Исландия'))

def show_result():
    RGB.hide()
    AGB.show()
    answ.setText('Следующий вопрос')

def show_question():
    AGB.hide()
    RGB.show()
    answ.setText('Ответить')
    RadioGroup.setExclusive(False)
    g1.setChecked(False)
    g2.setChecked(False)
    g3.setChecked(False)
    g4.setChecked(False)
    RadioGroup.setExclusive(True)

def start_test():
    if answ.text()=='Ответить':
        check_answer()
    else:
        next_question()

def show_correct(df):
    text.setText(df)
    show_result()

def next_question():
    main_win.counter+=1
    rnd = randint(0, len(qwst)-1)
    ask1 = qwst[rnd]
    ask(ask1)

app = QApplication([])


main_win = QWidget()
main_win.resize(400, 200)
main_win.setWindowTitle('Memo Card')
quest = QLabel('Какой национальности не существует?')
RGB = QGroupBox('Варианты ответов')
g1 = QRadioButton('Энцы')
g2 = QRadioButton('Смурфы')
g3 = QRadioButton('Чулымцы')
g4 = QRadioButton('Алеуты')

RadioGroup = QButtonGroup()
RadioGroup.addButton(g1)
RadioGroup.addButton(g2)
RadioGroup.addButton(g3)
RadioGroup.addButton(g4)


AGB = QGroupBox('Результат теста')
text = QLabel('Правильно/Неправильно')
text1 = QLabel('Правильный ответ')

answ = QPushButton('Ответить')

layoutH1 = QHBoxLayout()
layoutH2 = QVBoxLayout()
layoutH3 = QVBoxLayout() 
layoutH4 = QVBoxLayout()
layoutH6 = QHBoxLayout()
layoutH5 = QVBoxLayout()

layoutH2.addWidget(g1, alignment = (Qt.AlignVCenter|Qt.AlignHCenter))
layoutH2.addWidget(g2, alignment = (Qt.AlignVCenter|Qt.AlignHCenter))

layoutH5.addWidget(text, alignment = (Qt.AlignVCenter|Qt.AlignLeft))
layoutH5.addWidget(text1, alignment = (Qt.AlignVCenter|Qt.AlignHCenter))

layoutH3.addWidget(g3, alignment = (Qt.AlignVCenter|Qt.AlignHCenter))
layoutH3.addWidget(g4, alignment = (Qt.AlignVCenter|Qt.AlignHCenter))

layoutH6.addLayout(layoutH2)
layoutH6.addLayout(layoutH3)

layoutH1.addLayout(layoutH2)
layoutH1.addLayout(layoutH3)

AGB.setLayout(layoutH5)
AGB.hide()

RGB.setLayout(layoutH6)
layoutH4.addWidget(quest)
layoutH4.addWidget(AGB)
layoutH4.addWidget(RGB)
layoutH4.addWidget(answ)

main_win.setLayout(layoutH4)
answers = [g1, g2, g3, g4]

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
        main_win.right_answ+=1
    else:
        show_correct('Неправильно')
    main_win.qwsttta+=1
    main_win.rate = main_win.right_answ / main_win.qwsttta * 100
    print(main_win.qwsttta)
    print(main_win.right_answ)
    print(main_win.rate)
def ask(ask1: questionn):
    shuffle(answers)
    answers[0].setText(ask1.right)
    answers[1].setText(ask1.wrong1)
    answers[2].setText(ask1.wrong2)
    answers[3].setText(ask1.wrong3)
    quest.setText(ask1.question1)
    text1.setText(ask1.right)
    show_question()



answ.clicked.connect(start_test)
main_win.counter = 0
main_win.qwsttta = 0
main_win.right_answ = 0
main_win.show()
app.exec()