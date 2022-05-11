from django.urls import reverse
from menu import Menu, MenuItem

Menu.add_item("main", MenuItem("Accueil",
                               reverse("home")))

Menu.add_item("main", MenuItem("A propos de",
                               reverse("about")))
