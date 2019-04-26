from rasa_nlu.converters import load_data
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer

import os, sys
parent = os.path.dirname(os.path.realpath(__file__))
sys.path.append('../MITIE/mitielib')

def train():
    training_data = load_data('../mom/data/nlu.json')
    trainer = Trainer(RasaNLUConfig("../mom/nlu_model_config.json"))
    trainer.train(training_data)
    model_directory = trainer.persist('../models')  # Returns the directory the model is stored in
    return model_directory


def predict(model_directory):
    from rasa_nlu.model import Metadata, Interpreter
    # where `model_directory points to the folder the model is persisted in
    interpreter = Interpreter.load(model_directory, RasaNLUConfig("../mom/nlu_model_config.json"))
    print (interpreter.parse("salad"))

# model_directory = train()
# print (model_directory)

model_directory = train()
# predict("../models/default/model_20171117-181635")