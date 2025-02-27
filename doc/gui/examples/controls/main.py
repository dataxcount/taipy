import taipy as tp
from taipy.gui import Gui
from pages.pages_grp1.page1.page1 import page1_md
from pages.pages_grp1.page2.page2 import page2_md
from pages.root import root

pages = {
    '/':root,
    'pages_grp1/page1':page1_md,
    'pages_grp1/page2':page2_md,
}

lov_navbar = [("/pages_grp1/page1", "Example 1"),("/pages_grp1/page2", "Example 2")]

if __name__ == '__main__':
    app = Gui(pages=pages)
    tp.Orchestrator().run()
    app.run(title="Examples", use_reloader=True, port=5555)
    