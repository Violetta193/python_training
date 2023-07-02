import time


def test_delete_kontakt(app):
    app.open_home_page()
    app.kontakt.delete()
    time.sleep(1)
    app.return_to_home_page()