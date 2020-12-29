'''
JSON file structure:

{
    "gtk-theme": {
        "code": "123456789",
        "source": "xfce-look",
        "filename": "Hello World-tar.gz"
    },
    "icon-theme" {
        "code": "123456789",
        "source": "gnome-look",
        "filename": "candy-tar.gz"
    },
    "cinnamon-shell-theme": {
        "code": "123456789",
        "source": "cinnamon-look",
        "filename": "Hello World-tar.gz"
    },
    "gnome-shell-theme": {
        "code": "123456789",
        "source": "gnome-look",
        "filename": "Hello World-tar.gz"
    },
    "cursor-theme": {
        "code": "123456789",
        "source": "xfce-look",
        "filename": "Hello World-tar.gz",
    }
}
'''

import json

def load_theme_from_string(string)
    ...

def load_theme_from_file(filename):
    with open(filename) as f:
        json_content = f.read()

    return load_theme_from_file()