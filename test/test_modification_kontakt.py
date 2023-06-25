

def test_modification_kontakt(app):
        app.open_home_page()
        app.session.login(username="admin", password="secret")
        app.kontakt.modification()
        app.return_to_home_page()
        app.session.logout()