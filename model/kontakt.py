from sys import maxsize


class Kontakt:
    def __init__(self, first_name="", mid_name="",
                 last_name="", nick_name="",
                 title="", company_name="",
                 address="", home_number="",
                 e_mail="", id=""):
        self.first_name = first_name
        self.mid_name = mid_name
        self.last_name = last_name
        self.nick_name = nick_name
        self.title = title
        self.company_name = company_name
        self.address = address
        self.home_number = home_number
        self.e_mail = e_mail
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.first_name, self.last_name)

    def __eq__(self, other):
        return (self.id is None or other.id is None
                or self.id == other.id) and self.first_name == other.first_name and self.last_name == other.last_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
