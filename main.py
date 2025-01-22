import kivy
kivy.require('1.0.7')

from kivy.animation import Animation
from kivy.app import App
from kivy.uix.button import Button

import quicklz

class TestApp(App):

    def build(self):
        self.button = Button(text='hello QuickLZ!',
                        on_press=self.quicklz)
        return self.button

    def quicklz(self, instance):
        print("🍉🍉🍉" + " quicklz: ".join(dir(quicklz)))

        compressed = quicklz.compress(b'hello QuickLZ!')
        decompressed = quicklz.decompress(compressed)
        
        decompressedDesc = decompressed.decode("utf-8")
        print("🍉🍉🍉 decompressed: " + decompressedDesc)
        instance.text = "compressed and decompressed: " + decompressedDesc

if __name__ == '__main__':
    TestApp().run()

