from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="group1", header="test", footer="test2"))
    app.group.modify_first_group(Group(name="test"))


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="group1", header="test", footer="test2"))
    app.group.modify_first_group(Group(header="header1"))
