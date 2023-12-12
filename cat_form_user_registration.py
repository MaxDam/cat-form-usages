from cat.mad_hatter.decorators import tool, hook, plugin
from pydantic import BaseModel, Field, ValidationError, field_validator
from cat.log import log
from typing import Dict
import random

# Model
class UserRegistration(BaseModel):
    name:    str | None = None
    surname: str | None = None
    company: str | None = None
    email:   str | None = None
    
    @classmethod
    def get_prompt_examples(cls):
        return [
            {
                "sentence": "Hello, I would register me for this service",
                "json": [None, None, None],
                "updatedJson": [None, None, None]
            },
            {
                "sentence": "Hello, my surname is Smith",
                "json": ["John", None, None],
                "updatedJson": ["John", "Smith", None]
            }
        ]
    
    # Action
    @classmethod
    def execute_action(cls, model):
        result = "<h3>You have registered<h3><br>" 
        result += "<table border=0>"
        result += "<tr>"
        result += "   <td>Name</td>"
        result += f"  <td>{model.name}</td>"
        result += "</tr>"
        result += "<tr>"
        result += "   <td>Surname</td>"
        result += f"  <td>{model.surname}</td>"
        result += "</tr>"
        result += "<tr>"
        result += "   <td>Company</td>"
        result += f"  <td>{model.company}</td>"
        result += "</tr>"
        result += "<tr>"
        result += "   <td>Email</td>"
        result += f"  <td>{model.email}</td>"
        result += "</tr>"
        result += "</table>"
        return result


# Hook set model  
@hook
def cform_set_model(models, cat):
    settings = cat.mad_hatter.get_plugin().load_settings()
    if settings['user_registration'] is True:
        models.append(UserRegistration())
    return models

# Start intent
@tool(return_direct=True)
def start_register_intent(input, cat):
    '''I would register me for this service'''

    log.critical("INTENT USER REGISTRATION START")
    if "UserRegistration" in cat.working_memory.keys():
        cform = cat.working_memory["UserRegistration"]
        return cform.start_conversation()
    
    return "I'm sorry but I can't procede to register if you don't initialize my form model"

# Stop intent
@tool()
def stop_register_intent(input, cat):
    '''I don't want to continue this registration'''

    log.critical("INTENT USER REGISTRATION STOP")
    if "UserRegistration" in cat.working_memory.keys():
        cform = cat.working_memory["UserRegistration"]
        cform.stop_conversation()    
    return
    