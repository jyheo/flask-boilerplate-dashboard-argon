from dashapp import app1
from dashapp import app2
import gettext

def register_dashapps(server, lang):
    t = gettext.translation('messages', 'app/translations', languages=[lang])
    app1.register_dash(server, t.gettext)
    app2.register_dash(server, t.gettext)
