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
             View('Character Creation', '.starting_character_creation'),
             View('Stats', '.stats'),
             View('Skills and Backgrounds', '.skills'),
             View('Ability Checks', '.ability_checks'),
             View('Growth and Milestones', '.milestones'),
             View('Advantages and Disadvantages', '.advantages_and_disadvantages'),
             ),
    Subgroup('Combat',
             View('Combat Flow', '.combat'),
             View('Racing', '.racing'),
             View('Weapons', '.weapons'),
             View('Techniques', '.techniques'),
             View('Armor', '.armor'),
             View('Healing', '.healing'),
             ),
    View('Magic', '.magic'),
    Subgroup('World',
             View('Money', '.world_money'),
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


@srp.route("/character/creation/")
def starting_character_creation():
    header_text = "Character Creation"
    page_title = "Character Creation"
    return render_template('character_creation/starting_creation.html', headerText=header_text, pageTitle=page_title)


@srp.route("/character/stats/")
def stats():
    header_text = "Stats"
    page_title = "Stats"
    return render_template('character_creation/stats.html', headerText=header_text, pageTitle=page_title)


@srp.route("/character/skills/")
def skills():
    header_text = "Skills and Backgrounds"
    page_title = "Skills and Backgrounds"
    return render_template('character_creation/skills.html', headerText=header_text, pageTitle=page_title)


@srp.route("/character/ability_checks/")
def skills():
    header_text = "Ability Checks"
    page_title = "Ability Checks"
    return render_template('character_creation/ability_checks.html', headerText=header_text, pageTitle=page_title)


@srp.route("/character/milestones/")
def milestones():
    header_text = "Milestones"
    page_title = "Milestones"
    return render_template('character_creation/skills.html', headerText=header_text, pageTitle=page_title)


@srp.route("/character/advantages_and_disadvantages/")
def advantages_and_disadvantages():
    header_text = "Advantages and Disadvantages"
    page_title = "Advantages and Disadvantages"
    return render_template('character_creation/advantages_and_disadvantages.html', headerText=header_text,
                           pageTitle=page_title)


@srp.route("/combat/")
def combat():
    header_text = "Combat Basics"
    page_title = "Combat Basics"
    return render_template('combat_and_equipment/combat.html', headerText=header_text, pageTitle=page_title)


@srp.route("/racing/")
def racing():
    header_text = "Racing"
    page_title = "Racing"
    return render_template('combat_and_equipment/racing.html', headerText=header_text, pageTitle=page_title)


@srp.route("/combat/weapons/")
def weapons():
    header_text = "Weapons"
    page_title = "Weapons"
    return render_template('combat_and_equipment/weapons.html', headerText=header_text, pageTitle=page_title)


@srp.route("/combat/techniques/")
def techniques():
    header_text = "Combat Techniques"
    page_title = "Combat Techniques"
    return render_template('combat_and_equipment/techniques.html', headerText=header_text, pageTitle=page_title)


@srp.route("/combat/armor/")
def armor():
    header_text = "Armor"
    page_title = "Armor"
    return render_template('combat_and_equipment/armor.html', headerText=header_text, pageTitle=page_title)


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
def worldOverview():
    headerText = "Earth: The Forgotten Times"
    pageTitle = "World Overview"
    return render_template('earth_the_forgotten_times/overview.html', headerText=headerText, pageTitle=pageTitle)


@srp.route("/world/money/")
def world_money():
    header_text = "Money"
    pageTitle = "Money"
    return render_template('earth_the_forgotten_times/money.html', headerText=header_text, pageTitle=pageTitle)


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


if __name__ == "__main__":
    srp.run()
