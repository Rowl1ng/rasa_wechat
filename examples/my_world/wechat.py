from wxpy import *
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
# from wxpy import get_wechat_logger

# 之前训练好的NLU模型
nlu_model_path = '/home/luoling/rasa_nlu_chi/models/rasa_nlu_test/model_20171013-153447'
agent = Agent.load("../babi/models/policy/current", interpreter=RasaNLUInterpreter(nlu_model_path))

# 初始化机器人，扫码登陆
bot = Bot(console_qr=True, cache_path=True)


# bot.self.add()
# bot.self.accept()
# bot.self.send('哈咯~')
# bot.file_helper.send('哈咯~')
# logger = get_wechat_logger()

# 自动接受新的好友请求
@bot.register(msg_types=FRIENDS)
def auto_accept_friends(msg):
    # 接受好友请求
    new_friend = msg.card.accept()
    # 向新的好友发送消息
    new_friend.send('哈哈，我自动接受了你的好友请求')

# 回复 my_friend 的消息 (优先匹配后注册的函数!)
@bot.register(my_friend)
def reply_my_friend(msg):
    return 'received: {} ({})'.format(msg.text, msg.type)

@bot.register(bot.self, except_self=False)
def reply_self(msg):
    # agent = Agent.load("models/policy/current",
    #                    interpreter=RasaNLUInterpreter(nlu_model_path))
    ans = agent.handle_message(msg.text)
    # print (ans)
    # msg.reply(ans)
    return ans
    # return 'received: {} ({})'.format(msg.text, msg.type)

# 进入 Python 命令行、让程序保持运行
embed()