# -*- coding: utf-8 -*-

from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_day():
    day = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
           '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
    return "".join([random.choice(day)])


def random_month():
    month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
             'November', 'December']
    return "".join([random.choice(month)])


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", photo="", title="", company="", address="",
                    home_telephone="", mobile_telephone="", work_telephone="", fax_telephone="", email="", email2="",
                    email3="", homepage="", bday="", bmonth="-", byear="", aday="", amonth="-", ayear="", address2="",
                    secondary_phone="", notes="")] + [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 20),
            lastname=random_string("lastname", 20), nickname=random_string("nickname", 20),
            photo="C:\\Users\\Haytay\\PycharmProjects\\python_training\\Test.png",
            title=random_string("title", 30), company=random_string("company", 30), address=random_string("address", 40),
            home_telephone=random_string("", 11), mobile_telephone=random_string("", 11),
            work_telephone=random_string("", 11), fax_telephone=random_string("", 11),
            email=random_string("email", 30), email2=random_string("email2", 30), email3=random_string("email3", 30),
            homepage=random_string("homepage", 40), bday=random_day(), bmonth=random_month(),
            byear=random_string("", 4), aday=random_day(), amonth=random_month(),
            ayear=random_string("", 4), address2=random_string("address2", 40),
            secondary_phone=random_string("", 11), notes=random_string("notes", 50))
    for i in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts)+1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


