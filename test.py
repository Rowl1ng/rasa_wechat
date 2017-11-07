

from rasa_core.tracker_store import InMemoryTrackerStore

domain = TemplateDomain.load('examples/restaurant_domain.yml')


agent = Agent(
    default_domain,
    policies=[SimplePolicy()],
    interpreter=HelloInterpreter(),
    tracker_store=InMemoryTrackerStore(default_domain)
)
from rasa_core.interpreter import RegexInterpreter
import pprint
pp = pprint.PrettyPrinter(indent=4)
interpreter = RegexInterpreter()
result = interpreter.parse('_greet[name=rasa]')
pp.pprint(result)

