# PageObject:
# 两大核心：
#     1. 面向接口编程： 测试用例
#     2. 面向HTML编程：对页面操作细节
# 六大原则：
#     1. 用公共方法（功能点）代表一个页面（类）应当提供的服务（业务层面的，不是操作细节）
#     2. 不要对外暴露，内部的操作细节（_转成私有）
#     3. 不要再内部操作流程中添加断言
#     4. 一个方法返回的是应该另外一个PO
#     5. 不需要把所有的控件都写出来
#     6. 正确和异常的case分开 return.self 或者return 详情页

# api_object:
# 封装减少冗余代码，同时在后期维护中，若接口发生变化，只需要调整接口封装的代码，提高测试用例的可维护性、可读性。
#     1. 将变与不变进行拆分，变的是测试数据，不变的是api
#     2. 创建api层将接口进行单独封装，方便组合业务流程和接口测试
#     3. 将接口公用的部分抽象出来 比如token , send发送请求 ，将方法写入base_api.py文件，管理api的文件取继承BaseApi
#     4. 封装api的时候，依据接口文档将接口需要校验的参数进行参数化 好处：灵活的组装业务，进行业务流程测试，接口测试
from WeWork.api.base import BaseApi


class QY_interface(BaseApi):

    url = 'https://qyapi.weixin.qq.com/'

    # def tag_id(self,num1,num2):
    #     data = {
    #         "method": "post",
    #         "url": self.url + 'cgi-bin/externalcontact/get_corp_tag_list',
    #         "params": {"access_token": self.wework}
    #     }
    #     return self.send_request(data).json()["tag_group"][num1]["tag"][num2]["id"]

    def tag_select(self):
        data = {
            "method": "post",
            "url": self.url + 'cgi-bin/externalcontact/get_corp_tag_list',
            "params": {"access_token": self.wework}
        }
        return self.send_request(data)

    def tag_add(self, name, **kwargs):
        data = {
            "method": "post",
            "url": self.url + 'cgi-bin/externalcontact/add_corp_tag',
            "params": {"access_token": self.wework},
            "json": {
                "tag": [{
                    "name": name
                }],
                **kwargs
            }
        }
        return self.send_request(data)

    def tag_update(self, id, name, **kwargs):
        data = {
            "method": "post",
            "url": self.url + 'cgi-bin/externalcontact/edit_corp_tag',
            "params": {"access_token": self.wework},
            "json": {
                "id": id,
                "name": name,
                **kwargs
            }
        }
        return self.send_request(data)

    def tag_delete(self, **kwargs):
        data = {
            "method": "post",
            "url": self.url + 'cgi-bin/externalcontact/del_corp_tag',
            "params": {"access_token": self.wework},
            "json": {**kwargs}
        }
        return self.send_request(data)


if __name__ == '__main__':
    a = QY_interface()
    # a.tag_select()
    # a.tag_add()
    # a.tag_update('et3OWZBwAAX6Ptk7edPj3vyrwmrM_yuQ','武汉城管')
    # a.tag_delete('et3OWZBwAAX6Ptk7edPj3vyrwmrM_yuQ')
