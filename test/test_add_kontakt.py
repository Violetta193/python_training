# -*- coding: utf-8 -*-
from model.kontakt import Kontakt
import time


def test_kontakts(app):
    app.open_home_page()
    old_kontakts = app.kontakt.get_kontakts_list()
    kontakt = Kontakt(first_name="anna",
                      mid_name="Maria",
                      last_name="Kalom",
                      nick_name="fire",
                      title="text",
                      company_name="Pigas",
                      address="Pavlova street",
                      home_number="9-343-3434-343",
                      e_mail="kkdfjkfd@mail.ru")
    app.kontakt.create(kontakt)
    app.open_home_page()
    new_kontakts = app.kontakt.get_kontakts_list()
    assert len(old_kontakts) + 1 == len(new_kontakts)
    old_kontakts.append(kontakt)
    assert sorted(new_kontakts, key=Kontakt.id_or_max) == sorted(old_kontakts, key=Kontakt.id_or_max)
    app.return_to_home_page()

def test_empty_kontakts(app):
    app.open_home_page()
    old_kontakts = app.kontakt.get_kontakts_list()
    kontakt = Kontakt(first_name="",
                mid_name="",
                last_name="",
                nick_name="",
                title="",
                company_name="",
                address="",
                home_number="",
                e_mail="")
    app.kontakt.create(kontakt)
    app.open_home_page()
    new_kontakts = app.kontakt.get_kontakts_list()
    assert len(old_kontakts) + 1 == len(new_kontakts)
    old_kontakts.append(kontakt)

    assert sorted(new_kontakts, key=Kontakt.id_or_max) == sorted(old_kontakts, key=Kontakt.id_or_max)

    app.return_to_home_page()
