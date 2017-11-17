from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
logger = logging.getLogger(__name__)
from rasa_core.agent import Agent
from rasa_core.channels.file import FileInputChannel
from rasa_core.policies.memoization import MemoizationPolicy
from mom_example import MomPolicy

def train_dialogue(domain_file='../mom/domain.yml',
                   model_path='../models/policy/mom',
                   training_data_file="../mom/data/stories.md"):
    agent = Agent(domain_file,
                  policies=[MemoizationPolicy(), MomPolicy()])

    agent.train(
            training_data_file,
            max_history=3,
            epochs=100,
            batch_size=50,
            augmentation_factor=50,
            validation_split=0.2
    )

    agent.persist(model_path)
    return agent

if __name__ == '__main__':
    logging.basicConfig(level="DEBUG")
    train_dialogue()
