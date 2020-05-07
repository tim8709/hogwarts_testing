from web.selenium.page.index import Index


class TestAddMember:
    def setup(self):
        self.index = Index(reuse=True)

    def test_add_member(self):
        # 跳转添加成员页面
        add_member = self.index.goto_add_member()
        # 添加成员
        add_member.add_member()
        # 测试是否添加
        # assert add_member.get_first() == "姓名"
        assert "姓名" in add_member.get_member_names()
