# -*- coding: utf-8 -*-
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatIconButton
from kivymd.uix.button import MDIconButton
from kivymd.uix.button import MDRoundFlatButton
from kivymd.uix.label import MDLabel
from kivymd.font_definitions import theme_font_styles
# from kivymd.uix.textfield import MDTextField
# from kivymd.uix.textfield import TextInput
from kivy.uix.textinput import TextInput
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.material_resources import dp

import re


# импортирование необходимых модулей
sub_for_easy = [['1', '3', '9', '27', '81'],
                ['1', '4', '16', '64', '256'],
                ['1', '2', '4', '8', '16'],
                ['1', '-4', '-9', '-14', '-19'],
                ['1', '-1', '-3', '-5', '-7'],
                ['1', '3', '5', '7', '9'],
                ['1', '-2', '-5', '-8', '-11'],
                ['1', '-5', '-11', '-17', '-23'],
                ['1', '5', '25', '125', '625'],
                ['1', '6', '36', '216', '1296'],
                ['1', '-3', '-7', '-11', '-15'],
                ['1', '7', '13', '19', '25'],
                ['1', '6', '11', '16', '21'],
                ['1', '4', '7', '10', '13']]
sub_for_normal = [['1', '5', '13', '25', '41', '61'],
                  ['1', '3', '7', '13', '21', '31'],
                  ['1', '4', '10', '19', '31', '46'],
                  ['1', '2', '7', '16', '29', '46'],
                  ['1', '2', '8', '19', '35', '56'],
                  ['1', '2', '6', '13', '23', '36'],
                  ['1', '5', '11', '19', '29', '41'],
                  ['1', '3', '10', '22', '39', '61'],
                  ['1', '4', '11', '22', '37', '56'],
                  ['1', '4', '12', '25', '43', '66'],
                  ['1', '6', '15', '28', '45', '66'],
                  ['1', '2', '5', '10', '17', '26'],
                  ['1', '6', '13', '22', '33', '46'],
                  ['1', '3', '8', '16', '27', '41'],
                  ['1', '5', '10', '16', '23', '31'],
                  ['1', '2', '4', '7', '11', '16'],
                  ['1', '6', '16', '31', '51', '76'],
                  ['1', '6', '12', '19', '27', '36'],
                  ['1', '5', '14', '28', '47', '71'],
                  ['1', '4', '9', '16', '25', '36'],
                  ['1', '3', '6', '10', '15', '21'],
                  ['1', '6', '14', '25', '39', '56'],
                  ['1', '3', '9', '19', '33', '51'],
                  ['1', '5', '12', '22', '35', '51'],
                  ['1', '4', '8', '13', '19', '26']]
sub_for_hard = [['15', '20', '20', '6', '6'], ['16', '5', '20', '25', '17'], ['16', '06', '68', '88', '28']]

language = ['language', 'язык']
c_language1 = ['english', 'английский']
c_language2 = ['russian', 'русский']
easy = ['easy', 'лёгкий']
normal = ['normal', 'нормальный']
hard = ['hard', 'сложный']
victory = ['VICTORY', 'ПОБЕДА']
task = ['You need to write 2 number and form of writing must be so: 3 4 without , or something else', 'Тебе надо написать 2 числа и форма записи должна быть без пробелов или , например: 3 4']
wrong_ans = ['something wrong', 'что-то ты намудрил']
message_m = ['may be you wrote a letter or icon', 'может быть ты написал букву или символ']
how_to_play = ['how to play?', 'как играть?']
advice = ['You need to understand the principle of subsequence and continue it(in hard you need to think unusual).', 'Тебе нужно понять принцып построения последовательности и продолжить её(в сложном уровне нужно хорошенько пораскинуть мозгами и думать не стандартно).']
way_easy = '/date/loco/easy'
class Guess_subsequence(MDApp):
    """ Главный класс"""
    def build(self):
        """Создание виджетов (кнопок).
           Главная функция.
           При первом посещении.
        """

        screen = MDScreen()


        def settings():
            """ Эта функция вызывается при нажатии на кнопку настройки.
                В ней будут такие настройки как: звук, магазин,о разработчике, язык(English, Russian).
            """
            screen.clear_widgets()
            with open('language.txt', 'r+') as n_lan:
                last_lan = n_lan.read()
            screen.add_widget(
                MDIconButton(
                    icon="back.png",
                    pos_hint={"center_x": .1, "center_y": .9},
                    on_press=mw
                )
            )
            screen.add_widget(
                # language
                MDRectangleFlatIconButton(
                    text=how_to_play[int(last_lan)],
                    icon="book",
                    line_color=(0, 0, 0, 0),
                    pos_hint={"center_x": .5, "center_y": .5},
                    on_press=lambda hrdv: book(),
                )
            )
            screen.add_widget(
                # language
                MDRectangleFlatIconButton(
                    text=language[int(last_lan)],
                    icon="flag",
                    line_color=(0, 0, 0, 0),
                    pos_hint={"center_x": .5, "center_y": .6},
                    on_press=lambda pokl: f_language(),
                )
            )
        settings_call = lambda sc: settings() # это лямбда функция передаёт функцию с настройками в переменную нажатия кнопки
        def f_language():
            """Эта функция вызывается для смены языка"""
            screen.clear_widgets()
            with open('language.txt', 'r+') as n_lan1:
                last_lan1 = n_lan1.read()
            screen.add_widget(
                MDRectangleFlatIconButton(
                    text=c_language2[int(last_lan1)],
                    line_color=(0, 0, 0, 0),
                    icon='flag',
                    pos_hint={"center_x": .3, "center_y": .5},
                    on_press=lambda jklh2: press_russian()
                )
            )
            screen.add_widget(
                MDRectangleFlatIconButton(
                    text=c_language1[int(last_lan1)],
                    icon='flag',
                    pos_hint={"center_x": .5, "center_y": .5},
                    line_color=(0, 0, 0, 0),
                    on_press=lambda jklh: press_english()
                )
            )
            screen.add_widget(
                MDIconButton(
                    icon="back.png",
                    pos_hint={"center_x": .1, "center_y": .9},
                    on_press=settings_call,
                )
            )

        def press_english():
            """Эта функция вызывается при нажатии на кнопку английский или english и меняет язык на английский"""
            with open('language.txt', 'w') as english:
               english.write('0')
        def press_russian():
            """Эта функция вызывается при нажатии на кнопку русский или russian и меняет язык на русский"""
            with open('language.txt', 'w') as russian:
               russian.write('1')
        def book():
            screen.clear_widgets()
            with open('language.txt', 'r+') as n_lan22:
                last_lan22 = n_lan22.read()
            screen.add_widget(
                MDLabel(
                    text=advice[int(last_lan22)],
                    pos_hint={"center_x": .5, "center_y": .8},
                    font_style=theme_font_styles[4],
                )
            )
            screen.add_widget(
                MDIconButton(
                    icon="back.png",
                    pos_hint={"center_x": .1, "center_y": .9},
                    on_press=settings_call,
                )
            )
        def main_window():


            """Эта функция - главное окно на которое будут ссылаться все кнопки назад из других окон.
               Все изменения, которые будут производиться здесь должны так же производиться и в начальном экране.
               При нажатие на кнопку настройки мы выполняем функцию settings(), которая в свою очередь, при нажатиии
               на кнопку назад вызывает эту функцию
            """
            screen.clear_widgets()
            with open('language.txt', 'r+') as n_lan3:
                last_lan3 = n_lan3.read()
            screen.add_widget(
                MDRectangleFlatIconButton(
                    # easy level
                    text=easy[int(last_lan3)],
                    line_color=(0, 0, 0, 0),
                    icon="android",
                    pos_hint={"center_x": .5, "center_y": .6},
                    on_press=el
                )
            )

            screen.add_widget(
                MDRectangleFlatIconButton(
                    # normal level
                    text=normal[int(last_lan3)],
                    icon="android",
                    line_color=(0, 0, 0, 0),
                    pos_hint={"center_x": .5, "center_y": .5},
                    on_press=nl,
                )
            )
            screen.add_widget(
                MDRectangleFlatIconButton(
                    # hard level
                    text=hard[int(last_lan3)],
                    icon="android",
                    line_color=(0, 0, 0, 0),
                    pos_hint={"center_x": .5, "center_y": .4},
                    on_press=hl,
                )
            )
            screen.add_widget(
                MDIconButton(
                    # This is settings
                    icon="set.png",
                    pos_hint={"center_x": .9, "center_y": .9},
                    on_press=settings_call
                )
            )
        mw = lambda mv2: main_window() # Эта лямбда функция ссылается на функцию главного окна и используется при обработки в окне настроик функция settings()
        def easy_level():
            """Эта функция вызывается при нажатии на кнопку easy.
               Она создаёт 14 кнопок для каждой последовательности.
               Синяя кнопка означает, что этот уровень открыт, но не решён.
               Зелёная, что уровень открыт и решён.
               Серая, что уровень не открыт и не решён и нажатия на эту кнопку обрабатываться не будут.
            """
            screen.clear_widgets()

            with open('easy.txt', 'r+') as f_for_levels:
                f_for_levels_2str = f_for_levels.readlines()
                e_p = ' '.join(f_for_levels_2str)
                e_p = e_p.replace('\n', '')
                # e_p2 = list(e_p)
                e_p = e_p.split(' ')
                if e_p[0] == '':
                    del e_p[-1] # список номеров кнопок
            for i in range(int(e_p[1])):
                screen.add_widget(
                    MDRoundFlatButton(
                            text=str(i + 1),
                            pos_hint={"center_x": .5, "center_y": 0.95 - i / 10 + (0.03 * i)},
                            # halign="center",
                            line_color=(0, 1, 0, 1),
                            text_color=(0, 1, 0, 1),
                            font_size="10sp",
                            line_width=2,
                            # ids=str(i + 1),
                            on_press=last_easy
                    )
                )
            if e_p[0] != '0':
                screen.add_widget(
                    MDRoundFlatButton(
                        text=e_p[0], # синяя кнопка
                        pos_hint={"center_x": .5, "center_y": 0.95 - int(e_p[1]) / 10 + (0.03 * int(e_p[1]))},
                        #halign="center",
                        line_width=2,
                        font_size="10sp",
                        on_press=lambda ne2: now_easy(zislo2=e_p[0]),

                    )
                )
            for e in range(14 - int(e_p[1]) - 1):
                screen.add_widget(
                    MDRoundFlatButton(
                        text=str(int(e_p[0]) + e + 1),
                        pos_hint={"center_x": .5, "center_y": 0.95 - (e + int(e_p[0])) / 10 + (0.03 * (e + int(e_p[0])))},
                        # halign="center",
                        line_color="#808080",
                        text_color="#808080",
                        font_size="10sp",
                        line_width=2,
                    )
                )
            screen.add_widget(
                MDIconButton(
                    icon="back.png",
                    pos_hint={"center_x": .1, "center_y": .9},
                    on_press=mw,
                )
            )

        el = lambda al2: easy_level()
        def now_easy(zislo2):
            """Эта функция выводит поле ввода с вопросом для синий(текущей кнопки)"""
            screen.clear_widgets()

            subseq_e = sub_for_easy[int(zislo2) - 1]
            subseq_e = subseq_e[:3]
            subseq_e = ' '.join(subseq_e)
            with open('language.txt', 'r+') as n_lan13:
                last_lan13 = n_lan13.read()
            screen.add_widget(
                MDLabel(
                    text=str(subseq_e),
                    pos_hint={"center_x": .6, "center_y": .5},
                    font_style=theme_font_styles[2],
                )
            )
            screen.add_widget(
                MDLabel(
                    text=task[int(last_lan13)],
                    pos_hint={"center_x": .5, "center_y": .7},
                    font_style=theme_font_styles[3],
                )
            )
            textinput = TextInput(size_hint=(.3, .05), pos_hint={"center_x": .5, "center_y": .5}, multiline=False)
            textinput.bind(text=on_text)
            screen.add_widget(textinput)
            screen.add_widget(
                MDIconButton(
                    icon="back.png",
                    pos_hint={"center_x": .1, "center_y": .9},
                    on_press=el,
                )
            )

        def victory_e(zislo3):
            """Эта функция выводится, когда мы ввели правильный ответ.
               Она выводит victory и также сохраняет все изменения в файл.
            """
            screen.clear_widgets()
            with open('language.txt', 'r+') as n_lan12:
                last_lan12 = n_lan12.read()
            screen.add_widget(
                MDLabel(
                    text=victory[int(last_lan12)],
                    pos_hint={"center_x": .5, "center_y": .5},
                    font_style=theme_font_styles[2],
                )
            )
            screen.add_widget(
                MDIconButton(
                    icon="back.png",
                    pos_hint={"center_x": .1, "center_y": .9},
                    on_press=el,
                )
            )
            zislo3[0] = str(int(zislo3[0]) + 1)
            zislo3[1] = str(int(zislo3[1]) + 1)
            # zislo3 = zislo3[:2]
            zislo4 = ' '.join(zislo3)
            zislo4 = zislo4.replace(' ', '\n')
            if zislo4[-1] == '':
                del zislo4[-1]
            with open('easy.txt', 'w') as f_e2:
                f_e2.write(zislo4)


        def on_text(instance, value):
            """Эта функция считывает поле ввода и если ответ правильный вызывает функцию victory,
               а если ответ содержит некорректную форму записи выводит соответствуеще сообщение,
               вызывая функцию more2.
            """
            ans = value.split(' ')
            with open('easy.txt', 'r+') as easy_l:
                subseq_e2 = easy_l.readlines()
                subseq_e3 = ' '.join(subseq_e2)
                subseq_e3 = subseq_e3.replace('\n', '')
                subseq_e3 = subseq_e3.split(' ')
                if subseq_e3[-1] == '':
                    del subseq_e3[-1]
            try:
                if ans[-1] == '':
                    del ans[-1]
                if len(ans) > 2:
                    more2()
                else:
                    if len(ans) < 0 or len(ans) < 1:
                        pass
                    elif ans[0] == sub_for_easy[int(subseq_e3[0]) - 1][-2] and ans[1] == sub_for_easy[int(subseq_e3[0]) - 1][-1]:
                        victory_e(zislo3=subseq_e3)
            except IndexError:
                pass
            # print(instance)
        def more2():
            """Эта функция выводит сообщение об некоректной форме записи"""
            screen.clear_widgets()
            with open('language.txt', 'r+') as n_lan11:
                last_lan11 = n_lan11.read()
            screen.add_widget(
                MDLabel(
                    text=wrong_ans[int(last_lan11)],
                    pos_hint={"center_x": .5, "center_y": .5},
                    font_style=theme_font_styles[2],
                )
            )
            screen.add_widget(
                MDLabel(
                    text=message_m[int(last_lan11)],
                    pos_hint={"center_x": .5, "center_y": .4},
                    font_style=theme_font_styles[3]
                )
            )
            screen.add_widget(
                MDIconButton(
                    icon="back.png",
                    pos_hint={"center_x": .1, "center_y": .9},
                    on_press=el,
                )
            )
        def last_easy(instance):
            """Эта функция вызывается для зелёных кнопок(уже решённых)"""
            self.now_button = str(instance.text)
            last_p = sub_for_easy[int(self.now_button) - 1]
            screen.clear_widgets()
            with open('language.txt', 'r+') as n_lan10:
                last_lan10 = n_lan10.read()
            screen.add_widget(
                MDLabel(
                    text=task[int(last_lan10)],
                    pos_hint={"center_x": .5, "center_y": .7},
                    font_style=theme_font_styles[3],
                )
            )
            last_p2 = last_p[:3]
            last_p3 = ' '.join(last_p2)
            screen.add_widget(
                MDLabel(
                    text=last_p3,
                    pos_hint={"center_x": .6, "center_y": .5},
                    font_style=theme_font_styles[2],
                )
            )
            screen.add_widget(
                MDIconButton(
                    icon="back.png",
                    pos_hint={"center_x": .1, "center_y": .9},
                    on_press=el,
                )
            )
            textinput2 = TextInput(size_hint=(.3, .05), pos_hint={"center_x": .5, "center_y": .5}, multiline=False)
            textinput2.bind(text=on_text2)
            screen.add_widget(textinput2)
        def on_text2(instance, value):
            """Эта функция обрабатывает текстовое поле для easy зелёных кнопок"""
            ans2 = value.split(' ')

            try:
                if ans2[-1] == '':
                    del ans2[-1]
                if len(ans2) > 2:
                    more2()
                else:
                    if len(ans2) < 0 or len(ans2) < 1:
                        pass
                    elif ans2[0] == sub_for_easy[int(self.now_button) - 1][-2] and ans2[1] == sub_for_easy[int(self.now_button) - 1][-1]:
                        last_victory_e()
            except IndexError:
                pass
        def last_victory_e():
            """Эта функция вызывается если ответ верный для зелёных кнопок.
               Эта функция в файле ничего не меняет.
            """
            screen.clear_widgets()
            with open('language.txt', 'r+') as n_lan9:
                last_lan9 = n_lan9.read()
            screen.add_widget(
                MDLabel(
                    text=victory[int(last_lan9)],
                    pos_hint={"center_x": .5, "center_y": .5},
                    font_style=theme_font_styles[2],
                )
            )
            screen.add_widget(
                MDIconButton(
                    icon="back.png",
                    pos_hint={"center_x": .1, "center_y": .9},
                    on_press=el,
                )
            )
        def normal_level():
            """Эта функция вызывается при нажатии на кнопку normal на начальном экране.
               В свою же очередь эта функция вызывает функцию next_screen_n из-за того что на экран не могут поместиться столько кнопок.
            """
            # print("yes")
            screen.clear_widgets()
            s = 0
            p = ''
            with open('normal.txt', 'r+') as normal_file:
                normal_file3str = normal_file.readlines()
                n_p = ' '.join(normal_file3str)
                n_p = n_p.replace('\n', '')
                # e_p2 = list(e_p)
                n_p = n_p.split(' ')
                if n_p[-1] == '':
                    del n_p[-1]  # список номеров кнопок
            for i in range(int(n_p[1])):
                if s >= 14:
                    p = 'g'
                    break
                else:
                    s += 1
                screen.add_widget(
                    MDRoundFlatButton(
                            text=str(i + 1),
                            pos_hint={"center_x": .5, "center_y": 0.95 - i / 10 + (0.03 * i)},
                            # halign="center",
                            line_color=(0, 1, 0, 1),
                            text_color=(0, 1, 0, 1),
                            font_size="10sp",
                            line_width=2,
                            on_press=last_normal
                            # ids=str(i + 1),
                            # on_press=last_easy
                    )
                )
            if n_p[0] != '0':
                if s <= 13:
                    screen.add_widget(
                        MDRoundFlatButton(
                            text=n_p[0], # синяя кнопка
                            pos_hint={"center_x": .5, "center_y": 0.95 - int(n_p[1]) / 10 + (0.03 * int(n_p[1]))},
                            #halign="center",
                            line_width=2,
                            font_size="10sp",
                            on_press=lambda yt: now_normal(zislo_n=n_p[0])
                            # on_press=lambda ne2: now_easy(zislo2=n_p[2]),

                        )
                    )
                else:
                    if p == '':
                        p = 'b'
                    s += 1
            for e in range(25 - int(n_p[1]) - 1):
                if s >= 13:
                    if p == '':
                        p = 'c'
                    break
                else:
                    s += 1
                screen.add_widget(
                    MDRoundFlatButton(
                        text=str(int(n_p[0]) + e + 1),
                        pos_hint={"center_x": .5, "center_y": 0.95 - (e + int(n_p[0])) / 10 + (0.03 * (e + int(n_p[0])))},
                        # halign="center",
                        line_color="#808080",
                        text_color="#808080",
                        font_size="10sp",
                        line_width=2,
                    )
                )
            screen.add_widget(
                MDIconButton(
                    icon="back.png",
                    pos_hint={"center_x": .1, "center_y": .9},
                    on_press=mw,
                )
            )
            screen.add_widget(
                MDIconButton(
                    icon="front.png",
                    pos_hint={"center_x": .9, "center_y": .1},
                    on_press=lambda n_next: next_screen_n(place=p, n_p2=n_p),
                )
            )
            # print(p)
        nl = lambda nl2: normal_level()
        def next_screen_n(place, n_p2):
            """Эта функция вызывается функцией normal_level и служит её продолжением."""
            screen.clear_widgets()
            # i2 = 0
            screen.add_widget(
                MDIconButton(
                    icon="back.png",
                    pos_hint={"center_x": .1, "center_y": .1},
                    on_press=nl,
                )
            )

            if place == 'g' and n_p2[1] != '14':
                for i2 in range(int(n_p2[1]) - 14):
                    screen.add_widget(
                        MDRoundFlatButton(
                                text=str(i2 + 15),
                                pos_hint={"center_x": .5, "center_y": 0.95 - i2 / 10 + (0.03 * i2)},
                                # halign="center",
                                line_color=(0, 1, 0, 1),
                                text_color=(0, 1, 0, 1),
                                font_size="10sp",
                                line_width=2,
                                on_press=last_normal
                        )
                    )
                if n_p2[0] != '0':
                    screen.add_widget(
                        MDRoundFlatButton(
                            text=n_p2[0],  # синяя кнопка
                            pos_hint={"center_x": .5, "center_y": 0.95 - (i2 + 1) / 10 + (0.03 * (i2 + 1))},
                            # halign="center",
                            line_width=2,
                            font_size="10sp",
                            on_press=lambda asdfe: now_normal(zislo_n=n_p2[0]),

                        )
                    )
                for e in range(11 - i2 - 2):
                    screen.add_widget(
                        MDRoundFlatButton(
                            text=str(int(n_p2[0]) + e + 1),
                            pos_hint={"center_x": .5,
                                      "center_y": 0.95 - (e + i2 + 2) / 10 + (0.03 * (e + i2 + 2))},
                            # halign="center",
                            line_color="#808080",
                            text_color="#808080",
                            font_size="10sp",
                            line_width=2,
                        )
                    )
            elif place == 'b':
                if n_p2[0] != '0':
                    screen.add_widget(
                        MDRoundFlatButton(
                            text=n_p2[0],  # синяя кнопка
                            pos_hint={"center_x": .5, "center_y": 0.95 - 1 / 10 + (0.03 * 1)},
                            # halign="center",
                            line_width=2,
                            font_size="10sp",
                            on_press=lambda xyz: now_normal(zislo_n=n_p2[0]),
                            # on_press=lambda ne2: now_easy(zislo2=n_p[2]),

                        )
                    )
                for e2 in range(10):
                    screen.add_widget(
                        MDRoundFlatButton(
                            text=str(int(n_p2[0]) + e2 + 1),
                            pos_hint={"center_x": .5,
                                      "center_y": 0.95 - (e2 + 2) / 10 + (0.03 * (e2 + 2))},
                            # halign="center",
                            line_color="#808080",
                            text_color="#808080",
                            font_size="10sp",
                            line_width=2,
                        )
                    )
            elif place == 'c':
                for e in range(11):
                    screen.add_widget(
                        MDRoundFlatButton(
                            text=str(14 + e + 1),
                            pos_hint={"center_x": .5,
                                      "center_y": 0.95 - (e + 1) / 10 + (0.03 * (e + 1))},
                            # halign="center",
                            line_color="#808080",
                            text_color="#808080",
                            font_size="10sp",
                            line_width=2,
                        )
                    )
        def now_normal(zislo_n):
            screen.clear_widgets()

            subseq_n = sub_for_normal[int(zislo_n) - 1]
            subseq_n = subseq_n[:4]
            subseq_n = ' '.join(subseq_n)
            with open('language.txt', 'r+') as n_lan8:
                last_lan8 = n_lan8.read()
            screen.add_widget(
                MDLabel(
                    text=str(subseq_n),
                    pos_hint={"center_x": .6, "center_y": .5},
                    font_style=theme_font_styles[2],
                )
            )
            screen.add_widget(
                MDLabel(
                    text=task[int(last_lan8)],
                    pos_hint={"center_x": .5, "center_y": .7},
                    font_style=theme_font_styles[3],
                )
            )
            textinput = TextInput(size_hint=(.3, .05), pos_hint={"center_x": .5, "center_y": .5}, multiline=False)
            textinput.bind(text=on_textn)
            screen.add_widget(textinput)
            screen.add_widget(
                MDIconButton(
                    icon="back.png",
                    pos_hint={"center_x": .1, "center_y": .9},
                    on_press=nl,
                )
            )
        def on_textn(instance, value):
            ansn = value.split(' ')
            with open('normal.txt', 'r+') as normal_l:
                subseq_n2 = normal_l.readlines()
                subseq_n3 = ' '.join(subseq_n2)
                subseq_n3 = subseq_n3.replace('\n', '')
                subseq_n3 = subseq_n3.split(' ')
                if subseq_n3[-1] == '':
                    del subseq_n3[-1]
            try:
                if ansn[-1] == '':
                    del ansn[-1]
                if len(ansn) > 2:
                    more3()
                else:
                    if len(ansn) < 0 or len(ansn) < 1:
                        pass
                    elif ansn[0] == sub_for_normal[int(subseq_n3[0]) - 1][-2] and ansn[1] == \
                            sub_for_normal[int(subseq_n3[0]) - 1][-1]:
                        victory_n(zislo_n2=subseq_n3)

            except IndexError:
                pass
            # print(i2)
        def more3():
            screen.clear_widgets()
            with open('language.txt', 'r+') as n_lan7:
                last_lan7 = n_lan7.read()
            screen.add_widget(
                MDLabel(
                    text=wrong_ans[int(last_lan7)],
                    pos_hint={"center_x": .5, "center_y": .5},
                    font_style=theme_font_styles[2],
                )
            )
            screen.add_widget(
                MDLabel(
                    text=message_m[int(last_lan7)],
                    pos_hint={"center_x": .5, "center_y": .4},
                    font_style=theme_font_styles[3]
                )
            )
            screen.add_widget(
                MDIconButton(
                    icon="back.png",
                    pos_hint={"center_x": .1, "center_y": .9},
                    on_press=nl,
                )
            )
        def victory_n(zislo_n2):
            screen.clear_widgets()
            with open('language.txt', 'r+') as n_lan6:
                last_lan6 = n_lan6.read()
            screen.add_widget(
                MDLabel(
                    text=victory[int(last_lan6)],
                    pos_hint={"center_x": .5, "center_y": .5},
                    font_style=theme_font_styles[2],
                )
            )
            screen.add_widget(
                MDIconButton(
                    icon="back.png",
                    pos_hint={"center_x": .1, "center_y": .9},
                    on_press=nl,
                )
            )
            zislo_n2[0] = str(int(zislo_n2[0]) + 1)
            zislo_n2[1] = str(int(zislo_n2[1]) + 1)
            # zislo_n2 = zislo_n2[:-4]
            # zislo_n2 = zislo_n2[:2]
            zislo5 = ' '.join(zislo_n2)
            zislo5 = zislo5.replace(' ', '\n')
            with open('normal.txt', 'w') as f_n2:
                f_n2.write(zislo5)
        def last_normal(instance):
            self.button_n = str(instance.text)
            last_pn = sub_for_normal[int(self.button_n) - 1]
            screen.clear_widgets()
            with open('language.txt', 'r+') as n_lan5:
                last_lan5 = n_lan5.read()
            screen.add_widget(
                MDLabel(
                    text=task[int(last_lan5)],
                    pos_hint={"center_x": .5, "center_y": .7},
                    font_style=theme_font_styles[3],
                )
            )
            last_pn2 = last_pn[:4]
            last_pn3 = ' '.join(last_pn2)
            screen.add_widget(
                MDLabel(
                    text=last_pn3,
                    pos_hint={"center_x": .6, "center_y": .5},
                    font_style=theme_font_styles[2],
                )
            )
            screen.add_widget(
                MDIconButton(
                    icon="back.png",
                    pos_hint={"center_x": .1, "center_y": .9},
                    on_press=nl,
                )
            )
            textinput3 = TextInput(size_hint=(.3, .05), pos_hint={"center_x": .5, "center_y": .5}, multiline=False)
            textinput3.bind(text=on_text3n)
            screen.add_widget(textinput3)
        def on_text3n(instance, value):
            ans_last_n = value.split(' ')

            try:
                if ans_last_n[-1] == '':
                    del ans_last_n[-1]
                if len(ans_last_n) > 2:
                    more3()
                else:
                    if len(ans_last_n) < 0 or len(ans_last_n) < 1:
                        pass
                    elif ans_last_n[0] == sub_for_normal[int(self.button_n) - 1][-2] and ans_last_n[1] == \
                            sub_for_normal[int(self.button_n) - 1][-1]:
                        last_victory_n()
            except IndexError:
                pass
        def last_victory_n():
            screen.clear_widgets()
            with open('language.txt', 'r+') as n_lan4:
                last_lan4 = n_lan4.read()
            screen.add_widget(
                MDLabel(
                    text=victory[int(last_lan4)],
                    pos_hint={"center_x": .5, "center_y": .5},
                    font_style=theme_font_styles[2],
                )
            )
            screen.add_widget(
                MDIconButton(
                    icon="back.png",
                    pos_hint={"center_x": .1, "center_y": .9},
                    on_press=nl,
                )
            )
        def hard_level():
            """Эта функция вызывается при нажатии на кнопку hard """
            screen.clear_widgets()

            with open('hard.txt') as hard_levelstr:
                hard_levelstr = hard_levelstr.readlines()
                h_p = ' '.join(hard_levelstr)
                h_p = h_p.replace('\n', '')
                # e_p2 = list(e_p)
                h_p = h_p.split(' ')
                if h_p[0] == '':
                    del h_p[-1]  # список номеров кнопок
            if h_p[1] == '0':
                screen.add_widget(
                    MDRoundFlatButton(
                        text='1',
                        pos_hint={"center_x": .5, "center_y": .5},
                        line_width=2,
                        font_size="40sp",
                        on_press=lambda cvfds: now_hard(numer_h='1'),
                    )
                )
                screen.add_widget(
                    MDRoundFlatButton(
                        text='2',
                        pos_hint={"center_x": .5, "center_y": .3},
                        line_width=2,
                        font_size="40sp",
                        line_color="#808080",
                        text_color="#808080",
                    )
                )
            elif h_p[1] == '1':
                screen.add_widget(
                    MDRoundFlatButton(
                        text='1',
                        pos_hint={"center_x": .5, "center_y": .5},
                        line_width=2,
                        font_size="40sp",
                        line_color=(0, 1, 0, 1),
                        text_color=(0, 1, 0, 1),
                        on_press=lambda kljh: last_hard(number_hl='1'),
                    )
                )
                screen.add_widget(
                    MDRoundFlatButton(
                        text='2',
                        pos_hint={"center_x": .5, "center_y": .3},
                        line_width=2,
                        font_size="40sp",
                        on_press=lambda cofds: now_hard(numer_h='2'),
                    )
                )
            elif h_p[1] == '2':
                screen.add_widget(
                    MDRoundFlatButton(
                        text='1',
                        pos_hint={"center_x": .5, "center_y": 0.5},
                        line_width=2,
                        font_size="40sp",
                        line_color=(0, 1, 0, 1),
                        text_color=(0, 1, 0, 1),
                        on_press=lambda klih: last_hard(number_hl='1'),
                    )
                )
                screen.add_widget(
                    MDRoundFlatButton(
                        text='2',
                        pos_hint={"center_x": .5, "center_y": 0.3},
                        line_width=2,
                        font_size="40sp",
                        line_color=(0, 1, 0, 1),
                        text_color=(0, 1, 0, 1),
                        on_press=lambda kljhw: last_hard(number_hl='2'),
                    )
                )
            screen.add_widget(
                MDIconButton(
                    icon="back.png",
                    pos_hint={"center_x": .1, "center_y": .9},
                    on_press=mw,
                )
            )
        hl = lambda rtyu: hard_level()
        def now_hard(numer_h):
            """Эта функция вызывается при нажатии на синию кнопку"""
            screen.clear_widgets()
            with open('language.txt', 'r+') as n_lan14:
                last_lan14 = n_lan14.read()
            if numer_h == '1':
                if last_lan14 == '0':
                    self.subseq_h = sub_for_hard[0]
                    self.subseq_h2 = self.subseq_h[:3]
                    self.subseq_h2 = ' '.join(self.subseq_h2)
                else:
                    self.subseq_h = sub_for_hard[1]
                    self.subseq_h2 = self.subseq_h[:3]
                    self.subseq_h2 = ' '.join(self.subseq_h2)
            else:
                self.subseq_h = sub_for_hard[2]
                self.subseq_h2 = self.subseq_h[:3]
                self.subseq_h2 = ' '.join(self.subseq_h2)


            screen.add_widget(
                MDLabel(
                    text=task[int(last_lan14)],
                    pos_hint={"center_x": .5, "center_y": .7},
                    font_style=theme_font_styles[3],
                )
            )
            screen.add_widget(
                MDLabel(
                    text=str(self.subseq_h2),
                    pos_hint={"center_x": .6, "center_y": .5},
                    font_style=theme_font_styles[2],
                )
            )
            textinput = TextInput(size_hint=(.3, .05), pos_hint={"center_x": .5, "center_y": .5}, multiline=False)
            textinput.bind(text=on_texth)
            screen.add_widget(textinput)
            screen.add_widget(
                MDIconButton(
                    icon="back.png",
                    pos_hint={"center_x": .1, "center_y": .9},
                    on_press=hl,
                )
            )
        def on_texth(instance, value):
            """Эта функция считывает ответ с поля ввода"""
            ans4 = value.split(' ')
            with open('language.txt', 'r+') as n_lan15:
                last_lan15 = n_lan15.read()
            with open('hard.txt', 'r+') as hard_l:
                subseq_h22 = hard_l.readlines()
                subseq_h3 = ' '.join(subseq_h22)
                subseq_h3 = subseq_h3.replace('\n', '')
                subseq_h3 = subseq_h3.split(' ')
                if subseq_h3[-1] == '':
                    del subseq_h3[-1]
            try:
                # print(self.subseq_h)
                if ans4[-1] == '':
                    del ans4[-1]
                if len(ans4) > 2:
                    more4()
                else:

                    # print(ans4)
                    if len(ans4) < 0 or len(ans4) < 1:
                        pass
                    elif str(sub_for_hard.index(self.subseq_h)) == '0':
                        if ans4 == ['6', '6']:
                            victory_h(zisloh=subseq_h3)
                    elif str(sub_for_hard.index(self.subseq_h)) == '1':
                        print("yes")
                        if ans4 == ['25', '17']:
                            victory_h(zisloh=subseq_h3)
                    elif str(sub_for_hard.index(self.subseq_h)) == '2':
                        if ans4[0] == sub_for_hard[2][-2] and ans4[1] == \
                                    sub_for_hard[2][-1]:
                            victory_h(zisloh=subseq_h3)
            except IndexError:
                pass

        def more4():
            """Эта функция выводит сообщение, что что-то у нас пошло не так"""
            screen.clear_widgets()
            with open('language.txt', 'r+') as n_lan16:
                last_lan16 = n_lan16.read()
            screen.add_widget(
                MDLabel(
                    text=wrong_ans[int(last_lan16)],
                    pos_hint={"center_x": .5, "center_y": .5},
                    font_style=theme_font_styles[2],
                )
            )
            screen.add_widget(
                MDLabel(
                    text=message_m[int(last_lan16)],
                    pos_hint={"center_x": .5, "center_y": .4},
                    font_style=theme_font_styles[3]
                )
            )
            screen.add_widget(
                MDIconButton(
                    icon="back.png",
                    pos_hint={"center_x": .1, "center_y": .9},
                    on_press=hl,
                )
            )
        def victory_h(zisloh):
            """Эта функция выводится для синей кнопки и выводит сообщение о победе и меняет файл"""
            screen.clear_widgets()
            with open('language.txt', 'r+') as n_lan17:
                last_lan17 = n_lan17.read()
            screen.add_widget(
                MDLabel(
                    text=victory[int(last_lan17)],
                    pos_hint={"center_x": .5, "center_y": .5},
                    font_style=theme_font_styles[2],
                )
            )
            screen.add_widget(
                MDIconButton(
                    icon="back.png",
                    pos_hint={"center_x": .1, "center_y": .9},
                    on_press=hl,
                )
            )
            zisloh[0] = str(int(zisloh[0]) + 1)
            zisloh[1] = str(int(zisloh[1]) + 1)
            # zislo_n2 = zislo_n2[:-4]
            # zislo_n2 = zislo_n2[:2]
            zisloh2 = ' '.join(zisloh)
            zisloh2 = zisloh2.replace(' ', '\n')
            with open('hard.txt', 'w') as f_h2:
                f_h2.write(zisloh2)
        def last_hard(number_hl):
            """Эта функция выводится для зелёных кнопок"""
            screen.clear_widgets()
            with open('language.txt', 'r+') as n_lan18:
                last_lan18 = n_lan18.read()
            if number_hl == '1':
                if last_lan18 == '0':
                    self.subseq_lh = sub_for_hard[0]
                    self.subseq_lh2 = self.subseq_lh[:3]
                    self.subseq_lh2 = ' '.join(self.subseq_lh2)
                else:
                    self.subseq_lh = sub_for_hard[1]
                    self.subseq_lh2 = self.subseq_lh[:3]
                    self.subseq_lh2 = ' '.join(self.subseq_lh2)
            else:
                self.subseq_lh = sub_for_hard[2]
                self.subseq_lh2 = self.subseq_lh[:3]
                self.subseq_lh2 = ' '.join(self.subseq_lh2)


            screen.add_widget(
                MDLabel(
                    text=task[int(last_lan18)],
                    pos_hint={"center_x": .5, "center_y": .7},
                    font_style=theme_font_styles[3],
                )
            )
            screen.add_widget(
                MDLabel(
                    text=str(self.subseq_lh2),
                    pos_hint={"center_x": .6, "center_y": .5},
                    font_style=theme_font_styles[2],
                )
            )
            textinput = TextInput(size_hint=(.3, .05), pos_hint={"center_x": .5, "center_y": .5}, multiline=False)
            textinput.bind(text=on_textlh)
            screen.add_widget(textinput)
            screen.add_widget(
                MDIconButton(
                    icon="back.png",
                    pos_hint={"center_x": .1, "center_y": .9},
                    on_press=hl,
                )
            )
        def on_textlh(instance, value):
            """Эта функция считывает поле ввода для зелёных кнопок"""
            ans5 = value.split(' ')
            with open('language.txt', 'r+') as n_lan19:
                last_lan19 = n_lan19.read()
            with open('hard.txt', 'r+') as hard_l:
                subseq_lh4 = hard_l.readlines()
                subseq_lh3 = ' '.join(subseq_lh4)
                subseq_lh3 = subseq_lh3.replace('\n', '')
                subseq_lh3 = subseq_lh3.split(' ')
                # print(self.subseq_lh)
                # print(str(sub_for_hard.index(self.subseq_lh)))
                if subseq_lh3[-1] == '':
                    del subseq_lh3[-1]
            try:
                if ans5[-1] == '':
                    del ans5[-1]
                if len(ans5) > 2:
                    more4()
                else:
                    # print(type(last_lan19))
                    # print(ans5)
                    if len(ans5) < 0 or len(ans5) < 1:
                        pass
                    elif str(sub_for_hard.index(self.subseq_lh)) == '0':
                        if ans5 == ['6', '6']:
                            victory_lh()
                    elif str(sub_for_hard.index(self.subseq_lh)) == '1':
                        if ans5 == ['25', '17']:
                            victory_lh()
                    elif str(sub_for_hard.index(self.subseq_lh)) == '2':
                        if ans5[0] == sub_for_hard[2][-2] and ans5[1] == \
                                    sub_for_hard[2][-1]:
                            victory_lh()
            except IndexError:
                pass
        def victory_lh():
            """Эта функция выводит сообщение о победе для зелёных кнопок"""
            screen.clear_widgets()
            with open('language.txt', 'r+') as n_lan20:
                last_lan20 = n_lan20.read()
            screen.add_widget(
                MDLabel(
                    text=victory[int(last_lan20)],
                    pos_hint={"center_x": .5, "center_y": .5},
                    font_style=theme_font_styles[2],
                )
            )
            screen.add_widget(
                MDIconButton(
                    icon="back.png",
                    pos_hint={"center_x": .1, "center_y": .9},
                    on_press=hl,
                )
            )
        with open('language.txt', 'r+') as n_lan2:
            last_lan2 = n_lan2.read()
        screen.add_widget(
            MDRectangleFlatIconButton(
                # easy level
                text=easy[int(last_lan2)],
                icon='android',
                line_color=(0, 0, 0, 0),
                pos_hint={"center_x": .5, "center_y": .6},
                on_press=el,
            )
        )


        # Эти строки исполняются в начале и должны содержать в себе всё что будет в функции main_window()
        screen.add_widget(
            MDRectangleFlatIconButton(
                # normal level
                text=normal[int(last_lan2)],
                icon="android",
                line_color=(0, 0, 0, 0),
                pos_hint={"center_x": .5, "center_y": .5},
                on_press=nl,
            )
        )
        screen.add_widget(
            MDRectangleFlatIconButton(
                # hard level
                text=hard[int(last_lan2)],
                icon="android",
                line_color=(0, 0, 0, 0),
                pos_hint={"center_x": .5, "center_y": .4},
                on_press=hl,

            )
        )
        screen.add_widget(
            MDIconButton(
                # This is settings
                icon="set.png",
                pos_hint={"center_x": .9, "center_y": .9},
                on_press=settings_call
            )
        )
        return screen
Guess_subsequence().run() # вызов главного класса