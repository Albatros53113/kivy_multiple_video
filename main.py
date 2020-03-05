from kivy.app import App
from os.path import dirname, join
from kivy.properties import NumericProperty, OptionProperty
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition


class Auswahlscreen(Screen):
    pass


class Abspielscreen(Screen):
    pass


class Hintergrund(ScreenManager):

    duration = NumericProperty(-1)
    position = NumericProperty(0)
    state = OptionProperty('stop', options=('play', 'pause', 'stop'))

    def __init__(self, **kwargs):
        super(Hintergrund, self).__init__(**kwargs)
        self.ids['_videofenster'].bind(texture=self._play_started,
                                       duration=self.setter('duration'),
                                       position=self.setter('position'),
                                       state=self._set_state)
        self.transition = NoTransition()
        self.current = '_auswahlscreen'
        self.curdir = dirname(__file__)
        self.letztesVideo = 0

    def start_movie(self, nummer):
        filename = join(self.curdir, 'film' + str(nummer) + '.mp4')
        # print(filename)
        self.ids['_videofenster'].source = filename
        self.ids['_videofenster'].state = 'play'
        if nummer == self.letztesVideo:
            self._play_started(None, None)
        self.letztesVideo = nummer

    def stop_movie(self):
        self.ids['_videofenster'].state = 'stop'

    def _play_started(self, instance, value):
        self.current = '_abspielscreen'

    def on_duration(self, instance, value):
        pass

    def on_position(self, instance, value):
        pass

    def _set_state(self, instance, value):
        self.state = value
        if self.state == 'stop':
            self.ids['_videofenster'].seek(0)
            self.current = '_auswahlscreen'

    def clear_video(self):
        curdir = dirname(__file__)
        filename = join(curdir, 'film1.mp4')
        self.ids['_videofenster'].source = filename
        self.ids['_videofenster'].state = 'play'


class VideoplayApp(App):

    def build(self):
        # self.sprachen = Sprachen()
        self.hauptfenster = Hintergrund()
        return self.hauptfenster

    def on_stop(self):
        pass


if __name__ == '__main__':
    from kivy.core.window import Window
    Window.size = 1920, 1080
    Window.fullscreen = True
    Window.top = 840
    Window.left = 1080
    VideoplayApp().run()
