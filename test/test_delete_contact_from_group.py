import random
import re
import time

from model.contact import Contact
from model.group import Group
import allure

def test_del_some_contact_from_group(app, db):
    old_groups = db.get_group_list()
    if len(old_groups) == 0:
        app.group.create(Group(name='test'))
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Lisa", middlename="Sea", lastname="Isa", nickname="Hay",
                                   photo="C:\\Users\\Haytay\\PycharmProjects\\python_training\\Test.png", title="tit",
                                   company="comp", address="adr", home_telephone="898", mobile_telephone="893423422",
                                   work_telephone="898", fax_telephone="898", email="a@asd.ru", email2="saew@imnr.ru",
                                   email3="aw@inw.ru", homepage="aa", bday="1", bmonth="May", byear="2000", aday="3",
                                   amonth="May", ayear="2003", address2="1qwe", secondary_phone="89233", notes="1as2"))
    with allure.step('Given a non-empty group list from db'):
        new_groups = db.get_group_list()
    with allure.step('Given a random group from the list'):
        group = random.choice(new_groups)
        old_contacts = db.get_contact_list()
        num = group.id
        index = random.randrange(len(old_contacts))
    with allure.step('Given a random contact that is included in the group %s' % group):
        if len(db.get_contacts_in_group(num)) == 0:
            app.contact.add_contact_to_group(index, group.name)
        old_contacts_in_group = sorted(app.contact.get_contacts_in_group(group_name=group.name), key=Contact.id_or_max)
        contacts_num = random.choice(old_contacts_in_group)
    with allure.step('When I delete a contact %s in the group' % contacts_num):
        app.contact.delete_contact_from_group(group.name, contacts_num.id)
        old_contacts_in_group.remove(contacts_num)
    with allure.step('Then the list from ui is equal to the list from db'):
        new_contacts_in_group = db.get_contacts_in_group(num)
        for i in range(len(old_contacts_in_group)):
            assert old_contacts_in_group[i].id == clear(new_contacts_in_group[i].id)


def clear(s):
    return re.sub("[() ,]", "", s)

