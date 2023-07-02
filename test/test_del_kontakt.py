import time
from model.kontakt import Kontakt

def test_delete_kontakt(app):
    if app.kontakt.count() == 0:
        app.kontakt.create(Kontakt())
    app.open_home_page()
    app.kontakt.delete_first_kontakt()
    time.sleep(1)
    app.return_to_home_page()