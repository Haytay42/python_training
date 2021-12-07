import re
from random import randrange


def test_check_random_contact_information(app):
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact_information_from_home_page = app.contact.get_contact_list()[index]
    contact_information_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_information_from_home_page.firstname == contact_information_from_edit_page.firstname
    assert contact_information_from_home_page.lastname == contact_information_from_edit_page.lastname
    assert contact_information_from_home_page.address == contact_information_from_edit_page.address
    assert contact_information_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_information_from_edit_page)
    assert contact_information_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(
        contact_information_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_telephone, contact.mobile_telephone, contact.work_telephone, contact.secondary_phone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))
