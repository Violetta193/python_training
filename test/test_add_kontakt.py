# -*- coding: utf-8 -*-
from model.kontakt import Kontakt


def test_kontakts(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.kontakt.create(
        Kontakt(first_name="anna",
                mid_name="Maria",
                last_name="Kalom",
                nick_name="fire",
                title="text",
                company_name="Pigas",
                address="Pavlova street",
                home_number="9-343-3434-343",
                e_mail="kkdfjkfd@mail.ru"))
    app.return_to_home_page()
    app.session.logout()


def test_empty_kontakts(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.kontakt.create(
        Kontakt(first_name="",
                mid_name="",
                last_name="",
                nick_name="",
                title="",
                company_name="",
                address="",
                home_number="",
                e_mail="")
    )
    app.return_to_home_page()
    app.session.logout()
