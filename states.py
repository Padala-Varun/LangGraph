#So now we are creating a graph
#and the first thing you create is a state

import os
#State Creation

#1) using typed Dict (Most comman approach)

from typing import TypedDict

class State(TypedDict):
    topic : str
    summary : str
    score : int

#2) using pydantic approach
# it is good at data validation and type checking at runtime

# pyrefly: ignore [missing-import]
from pydantic import BaseModel, field_validator

class State(BaseModel):
    topic : str
    summary : str=""
    score : int 


    @field_validator("score")
    @classmethod
    def score_positive(cls,v):
        if v<0:
            raise ValueError("Score must be positive")

# 3) using python data classes
# standard python dataclass but it is used very rarely
       
from dataclasses import dataclass , field

@dataclass
class State:
    topic : str=""
    summary : str=""
    messages : list=field(default_factory=list)

# 4) using langgraph message state

# pyrefly: ignore [missing-import]
from langgraph.graph import MessageState

class State(MessageState):
    user_name:str
    language:str