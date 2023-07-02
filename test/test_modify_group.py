from model.group import Group

# Этот тест я создавала в процессе одного из ваших уроков
def test_modify_group_name(app):
    if app.group.count() ==0:
        app.group.create(Group(name = "test"))
    app.group.modify_first_group(Group(name = "New group"))


def test_modify_group_header(app):
    if app.group.count() ==0:
        app.group.create(Group(name = "test"))
    app.group.modify_first_group(Group(header = "New header"))