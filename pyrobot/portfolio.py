from typing import List
from typing import Dict
from typing import Union
from typing import Optional

class Portfolio():

    # This argument is optional, however if it is passed through, it should be a string
    def __init__(self, account_number: Optional[str]):
        
        self.positions = {}
        self.positions_count = 0
        self.market_value = 0.0
        self.profit_loss = 0.0

        # This will help to calculate risk tolerance for a particular portfolio
        self.risk_tolerance = 0.0
        self.account_number = account_number

    # asset_type will provide some type of overview of how positions are allocated across different asset types.
    # THis section of code will make it easier for the user to see where it's easier for them to get a high level picture of what they have added so far
    # This assuming that the user wants to add one position at a time
    def add_position(self, symbol: str, asset_type: str, purchase_date: Optional[str], quantity: int = 0, purchase_price: float = 0.0) -> dict:
        
        self.positions[symbol] = {}
        self.positions[symbol]['symbol'] = symbol
        self.positions[symbol]['quantity'] = quantity
        self.positions[symbol]['purchase_price'] = purchase_price
        self.positions[symbol]['purchase_date'] = purchase_date
        self.positions[symbol]['asset_type'] = asset_type

        return self.positions

    # Assuming that the user wants to add multiple positions at once
    def add_positions(self, positions: List[dict]) -> dict:

        if isinstance(positions, list):

            for position in positions:

                self.add_position(
                    symbol = position['symbol'],
                    asset_type = position['asset_type'],
                    purchase_date = position.get['purchase_date', None],
                    purchase_price = position.get('purchase_price', 0.0),
                    quantity = position.get('quantity', 0)
                )

                return self.positions
        
        else:
            raise TypeError("Postions must be a list of dictionaries")

    # This assume that the user wants to remove a position
    def remove_position(self, symbol: str) -> Tuple[bool, str]:

        if symbol in self.positions:
            del self.positions[symbol]
            return (True, "{Symbol} was successfully removed!".format(symbol=symbol))
        else:
            return (True, "{Symbol} did not exist in the portfolio!".format(symbol=symbol))

    # Putting in a few placeholders

    #
    def in_portfolio(self, symbol: str) -> bool:

        if symbol in self.positions:
            return True
        else:
            return False
    
    # Asking to see if something is profitable 
    def is_profitable(self, symbol: str, current_price: float) -> bool:

        # Grab the purchase price 
        purchase_price = self.positions[symbol]['purchase_price']

        if (purchase_price <= current_price):
            return True
        elif (purchase_price > current_price):
            return False

    # This will show my distribution across asset classes
    def total_allocation(self):
        pass

    # Will be some kind of risk metric 
    def risk_exposure(self):
        pass

    def total_market_value(self):
        pass