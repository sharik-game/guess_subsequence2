from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatIconButton
from kivymd.uix.button import MDIconButton
from kivymd.uix.button import MDRoundFlatButton
from kivymd.uix.label import MDLabel
from kivymd.font_definitions import theme_font_styles

# импортирование необходимых модулей
slovar = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'ten': '10', 'eleven': '11', 'tvelve': '12',
          'thirteen': '13', 'fourteen': '14', 'fifteen': '15',
          }
sub_for_easy = [['1', '3', '9', '27', '81'],
                ['1', '4', '16', '64', '256'],
                ['1', '2', '4', '8', '16'],
                ['1', '-4', '-9', '-14', '-19'],
                ['1', '-1', '-3', '-5', '-7'],
                [1, 3, 5, 7, 9],
                [1, -2, -5, -8, -11],
                [1, -5, -11, -17, -23],
                [1, 5, 25, 125, 625],
                [1, 6, 36, 216, 1296],
                [1, -3, -7, -11, -15],
                [1, 7, 13, 19, 25],
                [1, 6, 11, 16, 21],
                [1, 4, 7, 10, 13]]
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
            screen.clear_widgets()
            with open('levels.txt', 'r+') as f_for_levels:
                f_for_levels_2str = f_for_levels.readlines()
                e_p = ' '.join(f_for_levels_2str.readlines())
                e_p = e_p.replace('\n', '')
                e_p2 = list(e_p)
                e_p2 = e_p2.split(' ')
                del e_p2[-1]
            screen.add_widget(
                MDRoundFlatButton(
                    text=f_for_levels_2str,
                    pos_hint={"center_x": .1, "center_y": .8},
                    md_bg_color='blue',
                    on_press=lambda ne2: now_easy(mas=slovar, zislo2=f_for_levels_2str)

                )
            )
        el = lambda al2: easy_level()
        def now_easy(mas, zislo2):
            screen.clear_widgets()
            num_e = mas[zislo2]
            subseq_e = sub_for_easy[int(num_e)]
            subseq_e = ' '.join(subseq_e)

            screen.add_widget(
                MDLabel(
                    text=str(subseq_e),
                    pos_hint={"center_x": .6, "center_y": .5},
                    font_style=theme_font_styles[2],
                )
            )
            screen.add_widget(
                MDIconButton(
                    icon="language-python",
                    pos_hint={"center_x": .1, "center_y": .9},
                    # on_press=mw
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
