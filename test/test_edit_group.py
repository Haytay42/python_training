# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="group_name1", header="group_header1", footer="group_footer1"))
    app.session.logout()

