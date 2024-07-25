from langchain_core.pydantic_v1 import BaseModel, Field

class Analysis(BaseModel):
    is_buyer_persona: bool = Field(description="Whether the user matches the buyer persona")
    explanation: str = Field(description="A clear and concise explanation of your decision without referring to yourself in first person")