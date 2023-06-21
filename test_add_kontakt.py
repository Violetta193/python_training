# -*- coding: utf-8 -*-
import pytest
from application import Application
from kontakt import Kontakt


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_kontakts(app):
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.init_kontakt_creation(
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
    app.logout()


def test_empty_kontakts(app):
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.init_kontakt_creation(
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
    app.logout()
