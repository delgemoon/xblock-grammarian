
#Import dependences

from lettuce.core import Feature
from lettuce.core import Scenario
from lettuce.core import Step
from lettuce.exceptions import LettuceSyntaxError

#validation tools
from nose.tools import assert_equals
from nose.tools import assert_raises


json_object = {
        'feature_name' : '' ,
        'scenario_name' : '' ,
        'step_dict' : [] ,
        } 

def outline_paser(stream):

    feature = Feature.from_string(stream)
    if feature is None:
        print "Feature is not found"
    self.json_object['feature_name'] = feature.sentence

    scenario = Scenario.from_string(stream)
    
    if scenario is None:
        print "Scenario is not found"


    self.json_object['scenario_name'] = scenario.sentence
    #keep going now
    step = []
    for step in scenario.solved_steps 

