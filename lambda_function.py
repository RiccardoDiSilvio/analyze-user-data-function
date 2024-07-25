import os
from model import Analysis
from langchain_anthropic import ChatAnthropic

def lambda_handler(event, context): 
    model = ChatAnthropic(model="claude-3-haiku-20240307", temperature=0)
    structured_llm = model.with_structured_output(Analysis)
    return  structured_llm.invoke(f"""
            I'm going to give you a buyer persona and a lot of data from LinkedIn about a user.
            I want you to analyze whether the user matches the buyer persona and why.
            Be very strict in following the buyer persona, and take into account when the person had experience in their roles
            Be detailed but concise in your explanation.
            This is the buyer persona: {event["buyer_persona"]} 
            And this is the user data: {event["user_data"]}
                        """).dict()