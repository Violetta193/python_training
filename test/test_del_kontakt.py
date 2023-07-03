import time
from model.kontakt import Kontakt

def test_delete_kontakt(app):
    if app.kontakt.count() == 0:
        app.kontakt.create(Kontakt())
    app.kontakt.open_page_kontakts()
    old_kontakts = app.kontakt.get_kontakts_list()
    app.kontakt.delete_first_kontakt()
    time.sleep(1)
    new_kontakts = app.kontakt.get_kontakts_list()
    assert len(old_kontakts) + 1 == len(new_kontakts)
    old_kontakts[0:1] = []
    assert old_kontakts == new_kontakts
    app.return_to_home_page()