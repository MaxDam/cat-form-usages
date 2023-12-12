from cat.mad_hatter.decorators import tool, hook, plugin
from pydantic import BaseModel, Field, ValidationError, field_validator
from cat.log import log
from typing import Dict
import random

# Model
class PizzaOrder(BaseModel):
    pizza_type: str | None = None
    address: str | None = None
    phone: str | None = None
    
    @field_validator("pizza_type")
    @classmethod
    def validate_pizza_type(cls, pizza_type: str):
        log.info("VALIDATIONS")

        if pizza_type in [None, ""]:
            return

        pizza_types = list(menu)
        if pizza_type not in pizza_types:
            raise ValueError(f"{pizza_type} is not present in the menù")
        
    @classmethod
    def get_prompt_examples(cls):
        return [
            {
                "sentence": "I want to order a pizza",
                "json": [None, None, None],
                "updatedJson": [None, None, None]
            },
            {
                "sentence": "I live in Via Roma 1",
                "json": ["Margherita", None, None],
                "updatedJson": ["Margherita", "Via Roma 1", None]
            }
        ]
    
    # Prompt prefix
    @classmethod
    def prompt_prefix(cls):
        return """you have to behave like a professional 
        waiter taking orders for a pizzeria, 
        always you have to appear cordial but friendly, 
        you must use informal language with the customer;
        translating everything in {language} language.
        """

    # Action
    @classmethod
    def execute_action(cls, model):
        result = "<h3>PIZZA CHALLENGE - ORDER COMPLETED<h3><br>" 
        result += "<table border=0>"
        result += "<tr>"
        result += "   <td>Pizza Type</td>"
        result += f"  <td>{model.pizza_type}</td>"
        result += "</tr>"
        result += "<tr>"
        result += "   <td>Address</td>"
        result += f"  <td>{model.address}</td>"
        result += "</tr>"
        result += "<tr>"
        result += "   <td>Phone Number</td>"
        result += f"  <td>{model.phone}</td>"
        result += "</tr>"
        result += "</table>"
        result += "<br>"                                                                                                     
        result += "Thanks for your order.. your pizza is on its way!"
        result += "<br><br>"
        result += f"<img style='width:400px' src='https://maxdam.github.io/cat-pizza-challenge/img/order/pizza{random.randint(0, 6)}.jpg'>"
        return result


# Hook set model  
@hook
def cform_set_model(models, cat):
    settings = cat.mad_hatter.get_plugin().load_settings()
    if settings['order_pizza'] is True:
        models.append(PizzaOrder())
    return models

# Order pizza start intent
@tool(return_direct=True)
def start_order_pizza_intent(input, cat):
    '''I would like to order a pizza
    I'll take a pizza'''

    log.critical("INTENT ORDER PIZZA START")
    if "PizzaOrder" in cat.working_memory.keys():
        cform = cat.working_memory["PizzaOrder"]
        return cform.start_conversation()
    
    return "I'm sorry but I can't order a pizza if you don't initialize my form model"

# Order pizza stop intent
@tool()
def stop_order_pizza_intent(input, cat):
    '''I don't want to order pizza anymore, 
    I want to give up on the order, 
    go back to normal conversation'''

    log.critical("INTENT ORDER PIZZA STOP")
    if "PizzaOrder" in cat.working_memory.keys():
        cform = cat.working_memory["PizzaOrder"]
        cform.stop_conversation()    
    return


# Get pizza menu
@tool()
def ask_menu(input, cat):
    '''What is on the menu?
    Which types of pizza do you have?
    Can I see the pizza menu?
    I want a menu'''

    log.critical("INTENT ORDER PIZZA MENU")
    # if the intent is active..
    if "PizzaOrder" in cat.working_memory.keys():
        # return menu
        response = "The available pizzas are the following:"
        for pizza in menu:
            response += f"\n - {pizza}"
        return response

    return input

menu = [
    "Margherita",
    "Romana",
    "Quattro Formaggi",
    "Capricciosa",
    "Bufalina",
    "Diavola"
]
