from kivymd.app import MDApp
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.modalview import ModalView
from kivy.lang.builder import Builder
from kivy.clock import Clock
from kivy.animation import Animation

Builder.load_string("""
<BusyDialog>:
    on_pre_open: self.animate_busy(busy_label)
    on_open: root._is_modal_open = True
    on_dismiss: root._is_modal_open = False
    id: busy_dialog
    auto_dismiss: False
    orientation: 'vertical'
    size_hint: (0.2, 0.2)
    pos_hint: {'top': 0.85, 'right': 0.21}
    background_normal: ''
    background_color: (0, 0, 0, 0)
    Label:
        id: busy_label
        dots: 0
        size_hint: (1, 1)
        _text: ""
        text: "[b]" + self._text + str("."*int(self.dots)) + "[/b]"
        pos_hint: {'top': 0.8, 'right': 0.5}
        color: (0.08,0.08,0.08,1)
        markup: True
        canvas.before:
            Color:
                rgba: (1,1,1,1)
            Rectangle:
                pos: self.pos
                size: self.size
            Color:
                rgba: (1,0,0,.3)
            Rectangle:
                pos: self.center[0] - (self.width/2 * self.dots/3), self.y
                size: self.width * self.dots/3, self.height
        

<RootLay>:
    MDRaisedButton:
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        text: 'Busy'
        on_release: root.busy_dialog.open_busy()
""")

class BusyDialog(ModalView):
    check = True
    cnt = 0
    def open_busy(self):
        app = App.get_running_app()
        app.root.busy_dialog.open()

    def run_busy(self, busy):
        Clock.schedule_once(self.animate_busy(busy),9)

    def animate_busy(self, busy, *args):
        #animate text busy. -> busy.. -> busy...
        sec = 1.0
        busy._text = "Busy"
        anim = Animation(dots=3, duration=sec * 3) + Animation(dots=3, duration=sec / 2) + Animation(dots=0, duration=sec * 3)
        anim.repeat = True
        anim.bind(on_progress=self.progression)
        anim.start(busy)

    def progression(self, *args):
        if args[2] == 1.0:
            self.cnt += 1
        if self.cnt == 3 and self.check:
            args[1].text = "[b]Finished[/b]"
            Animation.cancel_all(args[1], 'dots')
            App.get_running_app().root.busy_dialog.dismiss()

class RootLay(FloatLayout):
    busy_dialog = None
    _is_modal_open = False
    def __init__(self, **kwargs):
        super(RootLay, self).__init__(**kwargs)
        Clock.schedule_once(self.setup_menu)

    def setup_menu(self, dt):
        self.busy_dialog = BusyDialog()

class Example(MDApp):
    def build(self):
        return RootLay()

Example().run()