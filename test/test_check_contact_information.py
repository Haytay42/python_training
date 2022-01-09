import re
import allure
from model.contact import Contact


def test_check_contact_information(app, db):
    with allure.step('Given a non-empty contact list from db'):
        old_contacts = db.get_contact_list()
    with allure.step('When i get contact information lists from home page and edit page'):
        contact_information_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
        contact_information_from_edit_page = sorted(db.get_contact_list(), key=Contact.id_or_max)
    with allure.step('Then the list from home page is equal to the list from edit page'):
        assert contact_information_from_home_page == contact_information_from_edit_page
        for i in range(len(old_contacts)):
            assert contact_information_from_home_page[i].firstname == contact_information_from_edit_page[i].firstname
            assert contact_information_from_home_page[i].lastname == contact_information_from_edit_page[i].lastname
            assert contact_information_from_home_page[i].address == contact_information_from_edit_page[i].address
            assert contact_information_from_home_page[i].all_phones_from_home_page == merge_phones_like_on_home_page(contact_information_from_edit_page[i])
            assert contact_information_from_home_page[i].all_emails_from_home_page == merge_emails_like_on_home_page(
                contact_information_from_edit_page[i])


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_telephone, contact.mobile_telephone, contact.work_telephone, contact.secondary_phone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   [contact.email, contact.email2, contact.email3])))
