from typing import Optional
from pydantic import BaseModel, Field

from cat.mad_hatter.decorators import plugin


class MySettings(BaseModel):
    order_pizza: bool = Field(
        title="order a pizza",
        default=True
    )
    user_registration: bool = Field(
        title="user registration",
        default=False
    )

@plugin
def settings_schema():
    return MySettings.schema()
