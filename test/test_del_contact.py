from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Lisa", middlename="Sea", lastname="Isa", nickname="Hay", photo="C:\\Users\\Haytay\\PycharmProjects\\python_training\\Test.png", title="tit", company="comp", address="adr", home_telephone="898", mobile_telephone="893423422", work_telephone="898", fax_telephone="898", email="a@asd.ru", email2="saew@imnr.ru", email3="aw@inw.ru", homepage="aa", bday="1", bmonth="May", byear="2000", aday="3", amonth="May", ayear="2003", address2="1qwe", phone2="89233", notes="1as2"))
    app.contact.delete_first_contact()