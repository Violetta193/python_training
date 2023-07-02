from model.group import Group
# Этот тест я создавала сама в рамках ДЗ
def test_modification_first_group(app):
    if app.group.count() ==0:
        app.group.create(Group(name = "test"))
    app.group.modification_first_group()