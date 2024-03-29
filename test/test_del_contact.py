from model.contact import Contact
import random
import allure

def test_delete_first_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Lisa", middlename="Sea", lastname="Isa", nickname="Hay", photo="C:\\Users\\Haytay\\PycharmProjects\\python_training\\Test.png", title="tit", company="comp", address="adr", home_telephone="898", mobile_telephone="893423422", work_telephone="898", fax_telephone="898", email="a@asd.ru", email2="saew@imnr.ru", email3="aw@inw.ru", homepage="aa", bday="1", bmonth="May", byear="2000", aday="3", amonth="May", ayear="2003", address2="1qwe", secondary_phone="89233", notes="1as2"))
    with allure.step('Given a non-empty contact list'):
        old_contacts = db.get_contact_list()
    with allure.step('Given a random contact from the list'):
        contact = random.choice(old_contacts)
    with allure.step('When I delete a contact %s from the list' % contact):
        app.contact.delete_contact_by_id(contact.id)
    with allure.step('Then the new list is equal to the old list without the deleted contact'):
        new_contacts = db.get_contact_list()
        assert len(old_contacts) - 1 == app.contact.count()
        old_contacts.remove(contact)
        assert old_contacts == new_contacts
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

