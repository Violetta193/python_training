from model.kontakt import Kontakt


def test_modification_kontakt(app):
    if app.kontakt.count() == 0:
        app.kontakt.create(Kontakt())
    app.kontakt.open_page_kontakts()
    app.kontakt.modification(
        kontakt=Kontakt(first_name="new_name",
                        mid_name="new_midname",
                        last_name="new_lastname",
                        nick_name="new_nickname",
                        title="new_title",
                        company_name="Pigas",
                        address="Pavlova street",
                        home_number="9-343-3434-343",
                        e_mail="kkdfjkfd@mail.ru"))
    app.return_to_home_page()
# Hello world!