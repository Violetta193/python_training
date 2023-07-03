from model.kontakt import Kontakt


def test_modification_kontakt(app):
    if app.kontakt.count() == 0:
        app.kontakt.create(Kontakt())
    app.kontakt.open_page_kontakts()
    old_kontakts = app.kontakt.get_kontakts_list()
    kontakt = Kontakt(first_name="new_name",
                        mid_name="new_midname",
                        last_name="new_lastname",
                        nick_name="new_nickname",
                        title="new_title",
                        company_name="Pigas",
                        address="Pavlova street",
                        home_number="9-343-3434-343",
                        e_mail="kkdfjkfd@mail.ru")
    kontakt.id = old_kontakts[0].id
    app.kontakt.modification(kontakt)
    new_kontakts = app.kontakt.get_kontakts_list()
    assert len(old_kontakts) == len(new_kontakts)
    old_kontakts[0] = kontakt
    assert sorted(new_kontakts, key=Kontakt.id_or_max) == sorted(old_kontakts, key=Kontakt.id_or_max)
    app.return_to_home_page()
