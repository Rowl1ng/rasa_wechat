import sys
from rasa_core.channels.console import ConsoleInputChannel
sys.path.append('../MITIE/mitielib')
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.interpreter import NaturalLanguageInterpreter
from rasa_nlu.model import Metadata, Interpreter
from rasa_nlu.config import RasaNLUConfig
from rasa_core.policies import Policy
from rasa_core.actions.action import ACTION_LISTEN_NAME
from rasa_core import utils
import numpy as np
nlu_model_path = '../models/default/model_20171118-162138'

class SimplePolicy(Policy):
    def predict_action_probabilities(self, tracker, domain):
        # type: (DialogueStateTracker, Domain) -> List[float]

        responses = {
            "greet": 3,
            "goodbye": 4,
        }

        if tracker.latest_action_name == ACTION_LISTEN_NAME:
            key = tracker.latest_message.intent["name"]
            action = responses[key] if key in responses else 2
            return utils.one_hot(action, domain.num_actions)
        else:
            return np.zeros(domain.num_actions)

class HelloInterpreter(NaturalLanguageInterpreter):
    def parse(self, message):
        interpreter = Interpreter.load(nlu_model_path, RasaNLUConfig("../mom/nlu_model_config.json"))
        intent = interpreter.parse(message)
        return intent

def complex():
    agent = Agent.load("../models/policy/mom", interpreter=HelloInterpreter())
    return agent
def simple():
    from rasa_core.tracker_store import InMemoryTrackerStore
    from rasa_core.domain import TemplateDomain
    default_domain = TemplateDomain.load("../mom/domain.yml")
    agent = Agent(default_domain,
                  policies=[SimplePolicy()],
                  interpreter=HelloInterpreter(),
                  tracker_store=InMemoryTrackerStore(default_domain)
                  )
    return agent

agent = complex()
# agent = simple()
agent.handle_channel(ConsoleInputChannel())
# ans = agent.handle_message("你好")
# print(" ".join(ans))
