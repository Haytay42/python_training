# -*- coding: utf-8 -*-
import random
from model.group import Group
import allure

def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='test'))
    with allure.step('Given a non-empty group list'):
        old_groups = db.get_group_list()
    with allure.step('Given a random group from the list'):
        group_to_mod = random.choice(old_groups)
        elem_index = app.group.get_element_index(old_groups, group_to_mod.id)
        group = Group(name="New group")
    with allure.step('When I modify a group %s in the list' % group):
        app.group.modify_group_by_id(group_to_mod.id, group)
    with allure.step('Then the new list is equal to the old list with the modify group'):
        assert len(old_groups) == app.group.count()
        new_groups = db.get_group_list()
        old_groups[elem_index] = group
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
            assert sorted(app.group.get_group_list(), key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_modify_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(header='test'))
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(header="New header"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)

