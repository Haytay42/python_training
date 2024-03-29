# -*- coding: utf-8 -*-
import random
from model.contact import Contact
import allure

def test_modify_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Lisa", middlename="Sea", lastname="Isa", nickname="Hay", photo="C:\\Users\\Haytay\\PycharmProjects\\python_training\\Test.png", title="tit", company="comp", address="adr", home_telephone="898", mobile_telephone="893423422", work_telephone="898", fax_telephone="898", email="a@asd.ru", email2="saew@imnr.ru", email3="aw@inw.ru", homepage="aa", bday="1", bmonth="May", byear="2000", aday="3", amonth="May", ayear="2003", address2="1qwe", secondary_phone="89233", notes="1as2"))
    with allure.step('Given a non-empty contact list'):
        old_contacts = db.get_contact_list()
    with allure.step('Given a random contact from the list'):
        contact_to_mod = random.choice(old_contacts)
        elem_index = app.contact.get_elem_index(app.contact.get_contact_list(), contact_to_mod.id)
        contact = Contact(firstname="Lisa2", middlename="Sea2", lastname="Isa2", nickname="Hay2", photo="C:\\Users\\Haytay\\PycharmProjects\\python_training\\Test1.png", title="tit2", company="comp2", address="adr2", home_telephone="8982", mobile_telephone="8934234222", work_telephone="8982", fax_telephone="8982", email="a@asd.ru2", email2="saew@imnr.ru2", email3="aw@inw.ru2", homepage="aa2", bday="12", bmonth="August", byear="2001", aday="4", amonth="August", ayear="2004", address2="1qwe1", secondary_phone="892331", notes="1as2d")
        contact.id = contact_to_mod.id
    with allure.step('When I modify a contact %s in the list' % contact):
        app.contact.modify_contact_by_element_index(elem_index, contact)
    with allure.step('Then the new list is equal to the old list with the modify contact'):
        assert len(old_contacts) == app.contact.count()
        new_contacts = db.get_contact_list()
        old_contacts.remove(contact_to_mod)
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

