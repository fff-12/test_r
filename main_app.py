# напиши тут свою програму
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from instructions import txt_instruction, txt_test1, txt_test2, txt_test3, txt_sits

class Result(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        outhe = BoxLayout(orientation = "vertical", padding = 8, spacing = 8)

        lb1 = Label(text = "place for results")
        
        outhe.add_widget(lb1)

        self.add_widget(outhe)

class PulseScr2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        outhe = BoxLayout(orientation = "vertical", padding = 8, spacing = 8)
        l1 = BoxLayout(size_hint = (0.8, None), height = "30sp")
        l2 = BoxLayout(size_hint = (0.8, None), height = "30sp")

        lb1 = Label(text = txt_test3)
        lb2 = Label(text = "Результат:")
        lb3 = Label(text = "Результата після відпочинку:")
        self.btn = Button(text = "Завершити", size_hint = (0.3, 0.2), pos_hint = {"center_x": 0.5})
        self.in_result1 = TextInput(text = "0", multiline = False)
        self.in_result2 = TextInput(text = "0", multiline = False)
        self.btn.on_press = self.next

        l1.add_widget(lb2)
        l1.add_widget(self.in_result1)
        l2.add_widget(lb3)
        l2.add_widget(self.in_result2)

        outhe.add_widget(lb1)
        outhe.add_widget(l1)
        outhe.add_widget(l2)
        outhe.add_widget(self.btn)

        self.add_widget(outhe)

    def next(self):
        self.manager.current = "result"

class CheckSist(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        outhe = BoxLayout(orientation = "vertical", padding = 8, spacing = 8)

        lb1 = Label(text = txt_sits)
        self.btn = Button(text = "Продовжити", size_hint = (0.3, 0.2), pos_hint = {"center_x": 0.5})
        self.btn.on_press = self.next

        outhe.add_widget(lb1)
        outhe.add_widget(self.btn)

        self.add_widget(outhe)

    def next(self):
        self.manager.current = "pulse2"

class PulseScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        outhe = BoxLayout(orientation = "vertical", padding = 8, spacing = 8)
        l1 = BoxLayout(size_hint = (0.8, None), height = "30sp")

        instr = Label(text = txt_test1)
        lb1_res = Label(text = "Введіть результат")
        self.in_result = TextInput(text = "0", multiline = False)
        self.btn = Button(text = "Продовжити", size_hint = (0.3, 0.2), pos_hint = {"center_x": 0.5})
        self.btn.on_press = self.next

        l1.add_widget(lb1_res)
        l1.add_widget(self.in_result)

        outhe.add_widget(instr)
        outhe.add_widget(l1)
        outhe.add_widget(self.btn)

        self.add_widget(outhe)

    def next(self):
        self.manager.current = "sist"

class InstrScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        outhe = BoxLayout(orientation = "vertical", padding = 8, spacing = 8)
        l1 = BoxLayout(size_hint = (0.8, None), height = "30sp")
        l2 = BoxLayout(size_hint = (0.8, None), height = "30sp")

        instr = Label(text = txt_instruction)
        lb1 = Label(text = "Введіть ім'я:")
        lb2 = Label(text = "Введіть вік:")
        self.in_name = TextInput(multiline = False)
        self.in_age = TextInput(multiline = False)
        self.btn = Button(text = "Start", size_hint = (0.3, 0.2), pos_hint = {"center_x": 0.5})
        self.btn.on_press = self.next

        l1.add_widget(lb1)
        l1.add_widget(self.in_name)

        l2.add_widget(lb2)
        l2.add_widget(self.in_age)

        outhe.add_widget(instr)
        outhe.add_widget(l1)
        outhe.add_widget(l2)
        outhe.add_widget(self.btn)

        self.add_widget(outhe)

    def next(self):
        self.manager.current = "pulse1"

class HeartCheck(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstrScr(name = "instr"))
        sm.add_widget(PulseScr(name = "pulse1"))
        sm.add_widget(CheckSist(name = "sist"))
        sm.add_widget(PulseScr2(name = "pulse2"))
        sm.add_widget(Result(name = "result"))
        return sm

app = HeartCheck()
app.run()