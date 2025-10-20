from pydantic import BaseModel

class Stock(BaseModel):
    c: float   # Current price
    d: float   # Change
    dp: float  # Percent change
    h: float   # High price of the day
    l: float   # Low price of the day
    o: float   # Open price of the day
    pc: float  # Previous close price
