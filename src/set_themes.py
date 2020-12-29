"""
Module for setting themes.

Supported desktops:
    Gnome (Pantheon)

TODO: Add more desktop environment
Goals:
    Cinnamon
    XFCE
    Kde
    LXDE
"""

from os import system

class InvalidDesktopEnvironmentError(Exception):
    ...

# Gtk Themes
class Gtk:
    GNOME = "gsettings set org.gnome.desktop.interface gtk-theme '{}'"

# Cursors
class Cursor:
    # There isn't support for cursor themes yet.
    ...

# Icon Theme
class Icon:
    GNOME = "gsettings set org.gnome.desktop.interface icon-theme '{}'"

# Window
class Window:
    GNOME = "gsettings set org.gnome.desktop.wm.preferences theme '{}'"


def set_theme(desktop, theme, name):
    """
    Usage:

        Desktop: Desktop environment name.
        theme: One of set_themes.Gtk, set_themes.Icon, set_themes.Window, set_themes.Cursor
        name: Theme name
    """

    if theme == Cursor:
        raise NotImplementedError

    if desktop in [
        "GNOME",
        "gnome",
        "UBUNTU",
        "ubuntu",
        "Ubuntu",
        "Gnome-xorg",
        "gnome-xorg",
        "PANTHEON",
        "pantheon",
        "Pantheon",
        "DEEPIN",
        "Deepin",
        "deepin",
    ]:
        system(getattr(theme, "GNOME").format(name))
    
    else:
        raise InvalidDesktopEnvironmentError(f"{desktop} desktop environment is not supported.")
