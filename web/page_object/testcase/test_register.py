from web.page_object.page.main import Main


class TestRegister():
    def setup(self):
        self.main = Main()

    def test_register(self):
        assert self.main.goto_login().goto_register().register()
