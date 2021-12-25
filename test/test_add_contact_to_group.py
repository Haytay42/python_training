import random
import re

from model.contact import Contact


def test_add_some_contact_to_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Lisa", middlename="Sea", lastname="Isa", nickname="Hay",
                                   photo="C:\\Users\\Haytay\\PycharmProjects\\python_training\\Test.png", title="tit",
                                   company="comp", address="adr", home_telephone="898", mobile_telephone="893423422",
                                   work_telephone="898", fax_telephone="898", email="a@asd.ru", email2="saew@imnr.ru",
                                   email3="aw@inw.ru", homepage="aa", bday="1", bmonth="May", byear="2000", aday="3",
                                   amonth="May", ayear="2003", address2="1qwe", secondary_phone="89233", notes="1as2"))
    old_contacts = db.get_contact_list()
    index = random.randrange(len(old_contacts))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.contact.add_contact_to_group(index, group.name)
    contact_from_ui = sorted(app.contact.get_contacts_in_group(group_name=group.name), key=Contact.id_or_max)
    num = group.id
    contact_from_db = db.get_contacts_in_group(num)
    for i in range(len(contact_from_ui)):
        assert contact_from_ui[i].id == clear(contact_from_db[i].id)

def clear(s):
    return re.sub("[() ,]", "", s)

