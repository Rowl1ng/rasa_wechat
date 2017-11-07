import logging

from rasa_core.policies import Policy
from rasa_core.actions.action import ACTION_LISTEN_NAME
from rasa_core import utils
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.domain import TemplateDomain
from rasa_core.agent import Agent

logger = logging.getLogger(__name__)

nlu_model_path = '/home/luoling/rasa_nlu_chi/models/rasa_nlu_test/model_20171013-153447'

class SimplePolicy(Policy):
    def predict_action_probabilities(self, tracker, domain):
        responses = {
            "greet": 2,
            "goodbye": 3,
            "chat": 4,
        }

        if tracker.latest_domain == ACTION_LISTEN_NAME:
            key = tracker.latest_message.intent("name")
            action = responses[key] if key in responses else 4
            return utils.one_hot(action, domain.num_actions)

def run_my_world(serve_forever=True):
    default_domain = TemplateDomain.load('common_domain.yml')
    agent = Agent.load("models/policy/current",
                       interpreter=RasaNLUInterpreter(nlu_model_path))
    if serve_forever:
        agent.handle_channel(ConsoleInputChannel())
    return agent


if __name__ == '__main__':
    logging.basicConfig(level="DEBUG")
    run_my_world()