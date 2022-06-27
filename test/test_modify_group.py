import random

from model.group import Group


def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='test'))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    new_data = Group(name="Test")
    app.group.modify_group_by_id(group.id, new_data)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)

    if check_ui:
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)