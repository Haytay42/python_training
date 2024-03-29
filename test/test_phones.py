import re
import allure
from model.contact import Contact


def test_phones_on_home_page(app, db):
    with allure.step('Given a non-empty contact list from db'):
        old_contacts = db.get_contact_list()
    with allure.step('When i get contact information lists from home page and edit page'):
        contact_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
        contact_from_edit_page = sorted(db.get_contact_list(), key=Contact.id_or_max)
    with allure.step('Then the phones in list from home page are equal to the phones in list from edit page'):
        for i in range(len(old_contacts)):
            assert contact_from_home_page[i].all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page[i])

def test_phones_on_contact_view_page (app):
    with allure.step('When i get contact information lists from view page and edit page'):
        contact_from_view_page = app.contact.get_contact_from_view_page(0)
        contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    with allure.step('Then the phones in list from view page are equal to the phones in list from edit page'):
        assert contact_from_view_page.home_telephone == contact_from_edit_page.home_telephone
        assert contact_from_view_page.mobile_telephone == contact_from_edit_page.mobile_telephone
        assert contact_from_view_page.work_telephone == contact_from_edit_page.work_telephone
        assert contact_from_view_page.secondary_phone == contact_from_edit_page.secondary_phone

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_telephone, contact.mobile_telephone, contact.work_telephone, contact.secondary_phone]))))