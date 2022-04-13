from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatIconButton
from kivymd.uix.button import MDIconButton
from kivymd.uix.button import MDRoundFlatButton
from kivymd.uix.label import MDLabel
from kivymd.font_definitions import theme_font_styles
from kivymd.uix.textfield import MDTextField
# from kivymd.uix.textfield import TextInput
from kivy.uix.textinput import TextInput

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
output_for_easy = []


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
            screen.add_widget(
                MDIconButton(
                    icon="language-python",
                    pos_hint={"center_x": .1, "center_y": .9},
                    on_press=mw
                )
            )
        settings_call = lambda sc: settings() # это лямбда функция передаёт функцию с настройками в переменную нажатия кнопки
        def main_window():


            """Эта функция - главное окно на которое будут ссылаться все кнопки назад из других окон.
               Все изменения, которые будут производиться здесь должны так же производиться и в начальном экране.
               При нажатие на кнопку настройки мы выполняем функцию settings(), которая в свою очередь, при нажатиии
               на кнопку назад вызывает эту функцию
            """
            screen.clear_widgets()
            screen.add_widget(
                MDRectangleFlatIconButton(
                    # easy level
                    text="easy",
                    icon="language-python",
                    line_color=(0, 0, 0, 0),
                    pos_hint={"center_x": .5, "center_y": .6},
                    on_press=el
                )
            )

            screen.add_widget(
                MDRectangleFlatIconButton(
                    # normal level
                    text="normal",
                    icon="language-python",
                    line_color=(0, 0, 0, 0),
                    pos_hint={"center_x": .5, "center_y": .5},
                )
            )
            screen.add_widget(
                MDRectangleFlatIconButton(
                    # hard level
                    text="hard",
                    icon="language-python",
                    line_color=(0, 0, 0, 0),
                    pos_hint={"center_x": .5, "center_y": .4},
                )
            )
            screen.add_widget(
                MDIconButton(
                    # This is settings
                    icon="language-python",
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

            with open('levels.txt', 'r+') as f_for_levels:
                f_for_levels_2str = f_for_levels.readlines()
                e_p = ' '.join(f_for_levels_2str)
                e_p = e_p.replace('\n', '')
                # e_p2 = list(e_p)
                e_p = e_p.split(' ')
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
                    icon="language-python",
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
            screen.add_widget(
                MDLabel(
                    text=str(subseq_e),
                    pos_hint={"center_x": .6, "center_y": .5},
                    font_style=theme_font_styles[2],
                )
            )
            screen.add_widget(
                MDLabel(
                    text='You need to write 2 number and form of writing must be so: 3 4 without , or something else',
                    pos_hint={"center_x": .5, "center_y": .7},
                    font_style=theme_font_styles[3],
                )
            )
            textinput = TextInput(size_hint=(.3, .05), pos_hint={"center_x": .5, "center_y": .5}, multiline=False)
            textinput.bind(text=on_text)
            screen.add_widget(textinput)
            screen.add_widget(
                MDIconButton(
                    icon="language-python",
                    pos_hint={"center_x": .1, "center_y": .9},
                    on_press=el,
                )
            )

        def victory_e(zislo3):
            """Эта функция выводится, когда мы ввели правильный ответ.
               Она выводит victory и также сохраняет все изменения в файл.
            """
            screen.clear_widgets()
            screen.add_widget(
                MDLabel(
                    text='VICTORY',
                    pos_hint={"center_x": .5, "center_y": .5},
                    font_style=theme_font_styles[2],
                )
            )
            screen.add_widget(
                MDIconButton(
                    icon="language-python",
                    pos_hint={"center_x": .1, "center_y": .9},
                    on_press=el,
                )
            )
            zislo3[0] = str(int(zislo3[0]) + 1)
            zislo3[1] = str(int(zislo3[1]) + 1)
            zislo3 = zislo3[:2]
            zislo4 = ' '.join(zislo3)
            zislo4 = zislo4.replace(' ', '\n')
            with open('levels.txt', 'w') as f_e2:
                f_e2.write(zislo4)
                f_e2.write('\n1\n0\n1\n0')

        def on_text(instance, value):
            """Эта функция считывает поле ввода и если ответ правильный вызывает функцию victory,
               а если ответ содержит некорректную форму записи выводит соответствуеще сообщение,
               вызывая функцию more2.
            """
            ans = value.split(' ')
            with open('levels.txt', 'r+') as easy_l:
                subseq_e2 = easy_l.readlines()
                subseq_e3 = ' '.join(subseq_e2)
                subseq_e3 = subseq_e3.replace('\n', '')
                subseq_e3 = subseq_e3.split(' ')
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
            screen.add_widget(
                MDLabel(
                    text='something wrong',
                    pos_hint={"center_x": .5, "center_y": .5},
                    font_style=theme_font_styles[2],
                )
            )
            screen.add_widget(
                MDLabel(
                    text='may be you wrote a letter or icon',
                    pos_hint={"center_x": .5, "center_y": .4},
                    font_style=theme_font_styles[3]
                )
            )
            screen.add_widget(
                MDIconButton(
                    icon="language-python",
                    pos_hint={"center_x": .1, "center_y": .9},
                    on_press=el,
                )
            )
        def last_easy(instance):
            """Эта функция вызывается для зелёных кнопок(уже решённых)"""
            self.now_button = str(instance.text)
            last_p = sub_for_easy[int(self.now_button) - 1]
            screen.clear_widgets()
            screen.add_widget(
                MDLabel(
                    text='You need to write 2 number and form of writing must be so: 3 4 without , or something else',
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
                    icon="language-python",
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
            screen.add_widget(
                MDLabel(
                    text='VICTORY',
                    pos_hint={"center_x": .5, "center_y": .5},
                    font_style=theme_font_styles[2],
                )
            )
            screen.add_widget(
                MDIconButton(
                    icon="language-python",
                    pos_hint={"center_x": .1, "center_y": .9},
                    on_press=el,
                )
            )






        # кнопки назад
        # self.theme_cls.material_style = "M3"
        screen.add_widget(
            MDRectangleFlatIconButton(
                # easy level
                text="easy",
                icon="language-python",
                line_color=(0, 0, 0, 0),
                pos_hint={"center_x": .5, "center_y": .6},
                on_press=el,
            )
        )

        # Эти строки исполняются в начале и должны содержать в себе всё что будет в функции main_window()
        screen.add_widget(
            MDRectangleFlatIconButton(
                # normal level
                text="normal",
                icon="language-python",
                line_color=(0, 0, 0, 0),
                pos_hint={"center_x": .5, "center_y": .5},
            )
        )
        screen.add_widget(
            MDRectangleFlatIconButton(
                # hard level
                text="hard",
                icon="language-python",
                line_color=(0, 0, 0, 0),
                pos_hint={"center_x": .5, "center_y": .4},

            )
        )
        screen.add_widget(
            MDIconButton(
                # This is settings
                icon="language-python",
                pos_hint={"center_x": .9, "center_y": .9},
                on_press=settings_call
            )
        )
        return screen
Guess_subsequence().run() # вызов главного класса