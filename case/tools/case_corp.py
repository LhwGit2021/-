import pytest
from jsonpath import jsonpath
from WeWork.api.api_corp import QY_interface


# def getId():
#     inter = QY_interface()
#     r = inter.tag_select()
#     id = jsonpath(r.json(), "$..[?(@.name=='无与伦比')]")[0]['id']
#     return id

def get_Id():
    inter = QY_interface()
    r = inter.tag_select()
    id = jsonpath(r.json(), "$..[?(@.name=='🐍')]")[0]['id']
    return id


class TestCorpTag:

    def setup(self):
        self.inter = QY_interface()

    def test_01select(self):
        r = self.inter.tag_select()
        print(r)
        assert r.json()["errcode"] == 0

    def test_demo(self):
        pass

    #
    #
    # def test_02add(self):
    #     data = {
    #         "group_id": "et3OWZBwAAh8z8yGjJ34cs9IifhxffKQ",
    #         "group_name": "客户等级"
    #     }
    #     r = self.inter.tag_add("无与伦比", **data)
    #
    # @pytest.mark.parametrize('id,name,check', [
    #     [getId(), "蛤蟆", 0],
    #     [getId(), "老鼠", 0],
    #     [getId(), "蝎子", 0],
    #     [getId(), "蜘蛛", 0],
    #     [getId(), "🐍", 0],
    # ], ids=["01", "02", "03", "04", "05"])
    # def test_03update(self, id, name, check):
    #     r = self.inter.tag_update(id, name)
    #     assert r.json()["errcode"] == check

    def test_04delete(self):
        data = {
            "tag_id": [
                get_Id()
            ]
        }
        r = self.inter.tag_delete(**data)
        assert r.json()["errcode"] == 0
