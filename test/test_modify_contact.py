# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Lisa", middlename="Sea", lastname="Isa", nickname="Hay", photo="C:\\Users\\Haytay\\PycharmProjects\\python_training\\Test.png", title="tit", company="comp", address="adr", home_telephone="898", mobile_telephone="893423422", work_telephone="898", fax_telephone="898", email="a@asd.ru", email2="saew@imnr.ru", email3="aw@inw.ru", homepage="aa", bday="1", bmonth="May", byear="2000", aday="3", amonth="May", ayear="2003", address2="1qwe", phone2="89233", notes="1as2"))
    app.contact.modify_contact(Contact(firstname="Lisa2", middlename="Sea2", lastname="Isa2", nickname="Hay2", photo="C:\\Users\\Haytay\\PycharmProjects\\python_training\\Test1.png", title="tit2", company="comp2", address="adr2", home_telephone="8982", mobile_telephone="8934234222", work_telephone="8982", fax_telephone="8982", email="a@asd.ru2", email2="saew@imnr.ru2", email3="aw@inw.ru2", homepage="aa2", bday="12", bmonth="August", byear="2001", aday="4", amonth="August", ayear="2004", address2="1qwe1", phone2="892331", notes="1as2d"))
