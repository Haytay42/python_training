# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_contact(Contact(firstname="Lisa2", middlename="Sea2", lastname="Isa2", nickname="Hay2", photo="C:\\Users\\Haytay\\PycharmProjects\\python_training\\Test1.png", title="tit2", company="comp2", address="adr2", home_telephone="8982", mobile_telephone="8934234222", work_telephone="8982", fax_telephone="8982", email="a@asd.ru2", email2="saew@imnr.ru2", email3="aw@inw.ru2", homepage="aa2", bday="12", bmonth="August", byear="2001", aday="4", amonth="August", ayear="2004", address2="1qwe1", phone2="892331", notes="1as2d"))
    app.session.logout()
