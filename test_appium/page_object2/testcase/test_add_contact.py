import pytest
import yaml
from test_appium.page_object2.page.app import App


class TestAddContact():
    def setup(self):
        self.main = App().start().main()

    @pytest.mark.parametrize('name,gender,phone', yaml.safe_load(open("../data/contact.yml", encoding='utf8')))
    def test_add_contact(self, name, gender, phone):
        self.main.goto_addresslist().click_addmember().click_addmanully(). \
            input_name(name).set_gender(gender).input_phone(phone).click_save().veriy_toast(). \
            click_back()
