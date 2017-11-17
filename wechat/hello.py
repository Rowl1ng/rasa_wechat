# hello.py
# -*- coding: utf-8 -*-

from sanic import Sanic, Blueprint
from sanic.views import HTTPMethodView
from sanic.response import text
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
import sys
sys.path.append('../MITIE/mitielib')
# from momo.helper import get_momo_answer  # 导入获取机器人回答获取函数

nlu_model_path = '../models/nlu/model_20171109-164837'
agent = Agent.load("../models/policy/mom", interpreter=RasaNLUInterpreter(nlu_model_path))


blueprint = Blueprint('index', url_prefix='/')


class ChatBot(HTTPMethodView):
    # 聊天机器人 http 请求处理逻辑
    async def get(self, request):
        ask = request.args.get('ask')
        # 先获取url 参数值 如果没有值，返回 '你说啥'
        if ask:
            answer = get_momo_answer(ask)
            return text(answer)
        return text('你说啥?')


blueprint.add_route(ChatBot.as_view(), '/momo')
# helper.py


def get_momo_answer(content):
    # 获取机器人返回结果函数
    response = agent.handle_message(content.text)
    if isinstance(response, str):
        return response
    return response.text