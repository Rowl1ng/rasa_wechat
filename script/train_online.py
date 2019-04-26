from rasa_core.agent import Agent

import sys
from rasa_core.channels.console import ConsoleInputChannel
sys.path.append('../MITIE/mitielib')
from rasa_core.domain import TemplateDomain
import logging
import numpy as np
from rasa_core.policies import Policy
from rasa_core.actions.action import ACTION_LISTEN_NAME
from rasa_core import utils
from rasa_core.interpreter import NaturalLanguageInterpreter
from rasa_nlu.model import Metadata, Interpreter
from rasa_nlu.config import RasaNLUConfig
from rasa_core.tracker_store import InMemoryTrackerStore
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy

nlu_model_path = '../models/default/model_20171118-162138'
logger = logging.getLogger(__name__)

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
        # return {
        #     "text": message,
        #     "intent": {"name": intent, "confidence": 1.0},
        #     "entities": []
        # }
def run_hello_world(max_training_samples=10,serve_forever=True):
    training_data = '../mom/data/stories.md'

    default_domain = TemplateDomain.load("../mom/domain.yml")
    agent = Agent(default_domain,
                  # policies=[SimplePolicy()],
                  policies=[MemoizationPolicy(), KerasPolicy()],
                  interpreter=HelloInterpreter(),
                  tracker_store=InMemoryTrackerStore(default_domain)
                  )
    logger.info("Starting to train policy")
    # agent = Agent(default_domain,
    #               policies=[SimplePolicy()],
    #               interpreter=HelloInterpreter(),
    #               tracker_store=InMemoryTrackerStore(default_domain))

    # if serve_forever:
    #     # Attach the commandline input to the controller to handle all
    #     # incoming messages from that channel
    #     agent.handle_channel(ConsoleInputChannel())

    agent.train_online(training_data,
                       input_channel=ConsoleInputChannel(),
                       epochs=1,
                       max_training_samples=max_training_samples)


    return agent

if __name__ == '__main__':
    logging.basicConfig(level="INFO")
    agent = run_hello_world()
    # ans = agent.handle_message("你好")
    #
    # print(ans)

# from rasa_core.interpreter import RegexInterpreter
# import pprint
# pp = pprint.PrettyPrinter(indent=4)
# interpreter = RegexInterpreter()
# result = interpreter.parse('_greet[name=rasa]')
# pp.pprint(result)

