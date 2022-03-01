import threading
from kivymd.uix.datatables import MDDataTable
from kivy.uix.anchorlayout import AnchorLayout
from kivy.metrics import dp
import kivy
import json
import requests
# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.icon_definitions import md_icons
from kivymd.uix.snackbar import Snackbar
# Floatlayout allows us to place the elements
# relatively based on the current window
# size and height especially in mobiles
from kivy.uix.floatlayout import FloatLayout


class Tab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''


class Home(MDFloatLayout, MDTabsBase):
    pass


class Location(MDFloatLayout, MDTabsBase):
    pass


class Database(MDFloatLayout, MDTabsBase):
    pass


class Register(MDFloatLayout, MDTabsBase):
    def registered(self, register):
        print("yess")


class RootLayout(MDFloatLayout):
    stop = threading.Event()


class Example(MDApp):
    def on_stop(self):
        self.root.stop()


class comments(MDFloatLayout, MDTabsBase):
    pass


class MainMDApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "My Material Application"
        self.auth_key = "lj6Vvz1LRVOjS4u5bG25GNGL6uap2WJF9NRlPbpk"
        super().__init__(**kwargs)
    def on_start(self):
        self.root.ids.database.text = "Moa updaredddddddddddddddddd"
    def build(self):
        self.theme_cls.theme_style = "Light"
        return Builder.load_file('admindash.kv')

    def databaseHealthRecorde(self, database):

        url = "https://isaifirst-434b9-default-rtdb.firebaseio.com/.json"
        database = requests.get(url=url + '?auth=' + self.auth_key)
        #for data in database.json():
        print(database.json())
        self.rows = database

    def registered(self, register):
        print("am working well")

    def emergencies(self, emergency):
        print("am working weel")

    def findLocation(self, location):
        self.url = "https://isaifirst-434b9-default-rtdb.firebaseio.com/.json"
        if len(location) == 2:
            err = Snackbar(text="NO Blank Space Allowed")
            err.open()
        else:
            if len(location) >= 3:
                err = Snackbar(text="Sucess")

                JSON = {"userLocation": f"{location}"}
                re = requests.patch(url=self.url, json=JSON)


class Example(MDApp):
    def on_stop(self):
        self.root.stop.set()

    def on_start(self):
        self.root.start.second_thread()


MainMDApp().run()
