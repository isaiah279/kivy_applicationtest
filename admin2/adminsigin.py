from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (450, 500)


class Tutorials(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Orange"
        self.config.primary_color = "Green"
        login_page = Builder.load_file('adminsigin.kv')

        return login_page

    def verify(self, email, password):

        if email == "isaiah@gmail.com" and password == 1234:
            print("Admin Logged in successfully")
        else:
            print("not logged in")


if __name__ == "__main__":
    Tutorials().run()
