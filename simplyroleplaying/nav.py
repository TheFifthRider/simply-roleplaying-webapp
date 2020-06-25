from flask_nav import Nav
from flask_bootstrap.nav import BootstrapRenderer

nav = Nav()


class CustomRenderer(BootstrapRenderer):
    def visit_Navbar(self, node):
        nav_tag = super(CustomRenderer, self).visit_Navbar(node)
        nav_tag['class'] = 'navbar navbar-srp'
        return nav_tag
