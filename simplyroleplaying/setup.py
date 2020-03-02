import os

from flask import Flask, render_template, send_from_directory
from flask_bootstrap import Bootstrap
from flask_nav import register_renderer
from flask_nav.elements import Navbar, View, Subgroup
from flask_heroku import Heroku
from flaskext.markdown import Markdown

from .nav import nav
from .nav import CustomRenderer

srp = Flask(__name__)
Bootstrap(srp)
Heroku(srp)
Markdown(srp)
nav.init_app(srp)
register_renderer(srp, 'custom', CustomRenderer)
nav.register_element('navbar', Navbar(
    View('Home', '.index'),
    Subgroup('Character',
             View('Character Creation', '.character_creation'),
             View('Stats', '.stats'),
             View('Skills and Backgrounds', '.skills'),
             View('Tests of Ability', '.tests'),
             View('Growth and Milestones', '.milestones'),
             View('Advantages and Disadvantages', '.advantages_and_disadvantages'),
             ),
    Subgroup('Action',
             View('Action Scenarios', '.action'),
             View('Combat Scenarios', '.combat'),
             View('Racing Scenarios', '.racing'),
             View('Weapons', '.weapons'),
             View('Techniques', '.techniques'),
             View('Armor', '.armor'),
             View('Healing', '.healing'),
             ),
    View('Magic', '.magic'),
    Subgroup('World',
             View('Overview', '.world'),
             View('Races', '.world_races'),
             View('Religions', '.world_religions'),
             ),
))


@srp.route('/static/styles/<path:filename>')
def styles(filename):
    return send_from_directory('static/styles', filename)


@srp.route('/static/logos/<path:filename>')
def logos(filename):
    return send_from_directory('static/logos', filename)


@srp.route('/static/icons/<path:filename>')
def icons(filename):
    return send_from_directory('static/icons', filename)


@srp.route("/")
def index():
    header_text = "Welcome to Simply Roleplaying!"
    page_title = "Home"
    return render_template('index.html', headerText=header_text, pageTitle=page_title)


@srp.route("/character/")
def character_creation():
    return render_markdown('character/creation.md')


@srp.route("/character/stats/")
def stats():
    return render_markdown('character/stats.md')


@srp.route("/character/skills/")
def skills():
    return render_markdown('character/skills.md')


@srp.route("/character/tests/")
def tests():
    return render_markdown('character/tests.md')


@srp.route("/character/milestones/")
def milestones():
    return render_markdown('character/milestones.md')


@srp.route("/character/advantages_and_disadvantages/")
def advantages_and_disadvantages():
    return render_markdown('character/advantages_and_disadvantages.md')


@srp.route("/action/")
def action():
    return render_markdown('action/action.md')


@srp.route("/action/combat/")
def combat():
    return render_markdown('action/combat.md')


@srp.route("/action/racing/")
def racing():
    header_text = "Racing"
    page_title = "Racing"
    return render_template('combat_and_equipment/racing.html', headerText=header_text, pageTitle=page_title)


@srp.route("/action/weapons/")
def weapons():
    header_text = "Weapons"
    page_title = "Weapons"
    return render_template('combat_and_equipment/weapons.html', headerText=header_text, pageTitle=page_title)


@srp.route("/action/techniques/")
def techniques():
    header_text = "Combat Techniques"
    page_title = "Combat Techniques"
    return render_template('combat_and_equipment/techniques.html', headerText=header_text, pageTitle=page_title)


@srp.route("/action/armor/")
def armor():
    return render_markdown('action/armor.md')


@srp.route("/combat/healing/")
def healing():
    header_text = "Healing"
    page_title = "Healing"
    return render_template('combat_and_equipment/healing.html', headerText=header_text, pageTitle=page_title)


@srp.route("/magic/")
def magic():
    header_text = "Simply Magic"
    page_title = "Simply Magic Module"
    return render_template('magic.html', headerText=header_text, pageTitle=page_title)


@srp.route("/world/")
def world_overview():
    return render_markdown('worlds/earth_the_forgotten_times/overview.md')


@srp.route("/world/races/")
def world_races():
    header_text = "The Races of Earth: The Forgotten Times"
    page_title = "Races - Earth: The Forgotten Times"
    return render_template('earth_the_forgotten_times/races.html', headerText=header_text, pageTitle=page_title)


@srp.route("/world/religions/")
def world_religions():
    header_text = "The Religions of Earth: The Forgotten Times"
    page_title = "Religions - Earth: The Forgotten Times"
    return render_template('earth_the_forgotten_times/religions.html', headerText=header_text, pageTitle=page_title)


def render_markdown(path_to_markdown):
    page_title = "page"
    with open(os.path.join(os.path.dirname(__file__), 'markdown/' + path_to_markdown), 'r') as file:
        file_contents = file.read()
        for line in file:
            trimmed_line = line.strip()
            if trimmed_line.startswith("#"):
                page_title = trimmed_line.strip("#").strip()
                break

    return render_template('base.html', pageTitle=page_title, fileContents=file_contents)


if __name__ == "__main__":
    srp.run()
