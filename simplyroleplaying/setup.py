from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_nav import register_renderer
from flask_nav.elements import Navbar, View, Subgroup
from flask_heroku import Heroku

from .nav import nav
from .nav import CustomRenderer

srp = Flask(__name__)
Bootstrap(srp)
Heroku(srp)
nav.init_app(srp)
register_renderer(srp, 'custom', CustomRenderer)
nav.register_element('navbar', Navbar(
    View('Home', '.index'),
    Subgroup('Character',
        View('Character Creation', '.startingCharacterCreation'),
        View('Stats', '.stats'),
        View('Advantages and Disadvantages', '.advantagesAndDisadvantages'),
        View('Character Growth', '.characterGrowth'),
    ),
    Subgroup('Combat',
        View('Combat Flow', '.combat'),
        View('Weapons', '.weapons'),
        View('Armor', '.armor'),
        View('Healing', '.healing'),
    ),
    View('Magic', '.magic'),
    Subgroup('World',
        View('Money', '.worldMoney'),
        View('Races', '.worldRaces'),
        View('Religions', '.worldReligions'),
    ),
    ))

@srp.route("/")
def index():
    headerText="Welcome to the Simply Roleplaying system!"
    pageTitle="Home"
    return render_template('index.html', headerText=headerText, pageTitle=pageTitle)

@srp.route("/character/creation/")
def startingCharacterCreation():
    headerText="Character Creation"
    pageTitle="Character Creation"
    return render_template('character_creation/starting_creation.html', headerText=headerText, pageTitle=pageTitle)

@srp.route("/character/stats/")
def stats():
    headerText="Stats"
    pageTitle="Stats"
    return render_template('character_creation/determining_stats.html', headerText=headerText, pageTitle=pageTitle)

@srp.route("/character/advantages_and_disadvantages/")
def advantagesAndDisadvantages():
    headerText="Advantages and Disadvantages"
    pageTitle="Advantages and Disadvantages"
    return render_template('character_creation/advantages_and_disadvantages.html', headerText=headerText, pageTitle=pageTitle)

@srp.route("/character/growth/")
def characterGrowth():
    headerText="Character Growth"
    pageTitle="Character Growth"
    return render_template('character_creation/character_growth.html', headerText=headerText, pageTitle=pageTitle)

@srp.route("/combat/")
def combat():
    headerText="Combat Basics"
    pageTitle="Combat Basics"
    return render_template('combat_and_equipment/combat.html', headerText=headerText, pageTitle=pageTitle)

@srp.route("/combat/weapons/")
def weapons():
    headerText="Weapons"
    pageTitle="Weapons"
    return render_template('combat_and_equipment/weapons.html', headerText=headerText, pageTitle=pageTitle)

@srp.route("/combat/armor/")
def armor():
    headerText="Armor"
    pageTitle="Armor"
    return render_template('combat_and_equipment/armor.html', headerText=headerText, pageTitle=pageTitle)

@srp.route("/combat/healing/")
def healing():
    headerText="Healing"
    pageTitle="Healing"
    return render_template('combat_and_equipment/healing.html', headerText=headerText, pageTitle=pageTitle)

@srp.route("/magic/")
def magic():
    headerText="Simply Magic"
    pageTitle="Simply Magic Module"
    return render_template('magic.html', headerText=headerText, pageTitle=pageTitle)

@srp.route("/world/")
def worldOverview():
    headerText="Earth: The Forgotten Times"
    pageTitle="World Overview"
    return render_template('earth_the_forgotten_times/overview.html', headerText=headerText, pageTitle=pageTitle)

@srp.route("/world/money/")
def worldMoney():
    headerText="Money"
    pageTitle="Money"
    return render_template('earth_the_forgotten_times/money.html', headerText=headerText, pageTitle=pageTitle)

@srp.route("/world/races/")
def worldRaces():
    headerText="The Races of Earth: The Forgotten Times"
    pageTitle="Races - Earth: The Forgotten Times"
    return render_template('earth_the_forgotten_times/races.html', headerText=headerText, pageTitle=pageTitle)

@srp.route("/world/religions/")
def worldReligions():
    headerText="The Religions of Earth: The Forgotten Times"
    pageTitle="Religions - Earth: The Forgotten Times"
    return render_template('earth_the_forgotten_times/religions.html', headerText=headerText, pageTitle=pageTitle)

if __name__ == "__main__":
  srp.run()
