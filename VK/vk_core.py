import vk_api
import os


class Vk:
    def __init__(self):
        """Авторизация ВКонтакте, инициализация сессии и инструментов"""
        vk_session = vk_api.VkApi(os.environ['VK_LOGIN'], os.environ['VK_PASSWORD'], app_id=5559651)
        try:
            vk_session.authorization()
        except vk_api.AuthorizationError as error_msg:
            print(error_msg)
        self.vk_session = vk_session
        self.tools = vk_api.VkTools(vk_session)

    def method(self, method_name, params):
        """Интерфейс обращения к методам ВКонтакте"""
        try:
            return self.vk_session.method(method_name, params)
        except:
            print("None request")
            return None

    def get_all(self, method_name, params):
        """Позволяет осуществлять в 25 раз больше запросов (идеально для выкачиваня стены)"""
        try:
            return self.tools.get_all(method_name, 100, params)
        except Exception as msg:
            print(msg)
            return None
