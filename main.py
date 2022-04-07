from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatIconButton
from kivymd.uix.button import MDIconButton
# импортирование необходимых модулей





class Guess_subsequence(MDApp):
    """ Главный класс"""



    def build(self):
        """Создание виджетов (кнопок).
           Главная функция.
        """
        screen = MDScreen()




        def settings():
            """ Эта функция вызывается при нажатии на кнопку настройки.
                В ней будут такие настройки как: звук, магазин,о разработчике, язык(English, Russian).
            """
            screen.clear_widgets()
            print(7)
        settings_call = lambda sc: settings() # это лямбда функция передаёт функцию с настройками в переменную нажатия кнопки
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
