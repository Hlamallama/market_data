from pydantic import BaseModel, Field

class Stock(BaseModel):
    current_price: float = Field(alias="c")   # Current price
    change: float = Field(alias="d")   # Change
    percentage_change: float = Field(alias="dp")  # Percent change
    high_price: float = Field(alias="h")   # High price of the day
    low_price: float = Field(alias="l")    # Low price of the day
    open_price: float = Field(alias="o")   # Open price of the day
    previous_close_price: float = Field(alias="pc")  # Previous close price

    class Config:
        validate_by_name = True

    def __str__(self):
        return (
            f"Current Price: {self.current_price}\n"
            f"Change: {self.change} ({self.percentage_change}%)\n"
            f"High: {self.high_price}\n"
            f"Low: {self.low_price}\n"
            f"Open: {self.open_price}\n"
            f"Previous Close Price: {self.previous_close_price}\n"
            + "-"*30
        )
