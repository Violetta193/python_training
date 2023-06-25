import time


def test_delete_kontakt(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.kontakt.delete()
    time.sleep(1)
    app.return_to_home_page()
    app.session.logout()