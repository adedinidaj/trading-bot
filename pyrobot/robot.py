# This will be interacting mainly with the TD Ameritrade API\
# Where we will send messsages back and forth from the API
# Where we will maintain our sessions
# Creating the other obejects, whether they are trade objects or stockframe objects

# might need to install panda if I don't have it install 
import panda as pd

# Probably need to install this as well
# How we create a new client that will create a new session and then maintain that session as we are interacting with the API
from td.client import TDClient
from td.utils import milliseconds_since_epoch

from datetime import datetime
from datetime import time
from datetime import timezone

from typing import List
from typing import Dict
from typing import Union


class PyRobot ():
# This is a method that is run everytime you create a new instance of that object 
# This will initialise a client
    def __init__(self, client_id: str, redirect_uri: str, credentials_path: str =  None, trading_account: str = None) -> None:
        self.trading_account: str = trading_account
        self.client_id: str = client_id
        self.redirect_uri: str = redirect_uri
        self.credentials_path: str = credentials_path
        self.session: TDClient = self._create_Session()
        self.trades: dict = ()
        self.historical_prices: dict = ()
        self.stock_frame = None

    # This will allow us to create a new session 
    def _create_session(self) -> TDClient:
        td_client = TDClient(
            client_id=self.client_id,
            redirect_uri=self.redirect_uri,
            credentials_path=self.credentials_path
        )
        
        # Login to the session
        td_client.login()
        
        return td_client
    
    
    # Going to define some properties about our Python robot
    
    # The below code is based off of US timezone
    # Might want to know is pre-market open
    @property
    def pre_market_open(self) -> bool:
        
        # Need to make sure to include utc because that's where timezone challenges come from
        # Need to make sure we are in utc time because we can't always assume that the user is going to be in our timezone 
    
        pre_market_start_time = datetime.now().replace(hour=12, minute=00, second=00, tzinfo=timezone.utc).timestamp()
        market_start_time = datetime.now().replace(hour=13, minute=30, second=00, tzinfo=timezone.utc).timestamp()
        right_now = datetime.now().replace(tzinfo=timezone.utc).timestamp()
        
        # Essentially this will just find out if the pre market is open
        # Using this will help me to know when to the tell the robot to start up or when to close down 
        if market_start_time >= right_now >= pre_market_start_time:
            return True
        else: 
            return False
                
    # Might want to know if post-market is open
    @property
    def post_market_open(self) -> bool:

        post_market_end_time = datetime.now().replace(hour=22, minute=30, second=00, tzinfo=timezone.utc).timestamp()
        market_end_time = datetime.now().replace(hour=20, minute=00, second=00, tzinfo=timezone.utc).timestamp()
        right_now = datetime.now().replace(tzinfo=timezone.utc).timestamp()
        
        # Essentially this will just find out if the pre market is open
        # Using this will help me to know when to the tell the robot to start up or when to close down 
        if post_market_end_time >= right_now >= market_end_time:
            return True
        else: 
            return False
    
    # Want to know if regular market, so not pre or post but what it is right now!
    @property
    def regular_market_open(self) -> bool:    

        market_start_time = datetime.now().replace(hour=13, minute=30, second=00, tzinfo=timezone.utc).timestamp()
        market_end_time = datetime.now().replace(hour=20, minute=00, second=00, tzinfo=timezone.utc).timestamp()
        right_now = datetime.now().replace(tzinfo=timezone.utc).timestamp()

        # Is it between the start time and the end time, if it is that means the market is open
        if market_end_time >= right_now >= market_start_time:
            return True
        else: 
            return False

    def create_portfolio(self):
        pass

    # This will create a trade object
    def create_trade(self):
        pass

    def create_stock_frame(self):
        pass

    def grab_current_quotes(self) -> dict:
        pass

    def grab_historical_prices(self) -> List(Dict):
        pass

   

    

