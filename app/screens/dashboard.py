from kivy.uix.screenmanager import Screen
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.fitimage import FitImage

from app.database.product_db import PRODUCTS


class DashboardScreen(Screen):

    def on_enter(self):
        self.load_products()

    def load_products(self):
        grid = self.ids.product_grid
        grid.clear_widgets()

        for product in PRODUCTS:
            card = MDCard(
                orientation="vertical",
                size_hint_y=None,
                height="260dp",
                padding="10dp",
                radius=[20],
            )

            layout = MDBoxLayout(orientation="vertical", spacing="5dp")

            img = FitImage(source=product["image"])

            name = MDLabel(
                text=product["name"],
                halign="center",
                bold=True,
            )

            price = MDLabel(
                text=f"${product['price']}",
                halign="center",
            )

            btn = MDRaisedButton(
                text="Add to Cart",
                pos_hint={"center_x": 0.5},
            )

            layout.add_widget(img)
            layout.add_widget(name)
            layout.add_widget(price)
            layout.add_widget(btn)

            card.add_widget(layout)
            grid.add_widget(card)