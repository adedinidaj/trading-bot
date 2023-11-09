Code stored here will include everything that is needed to create a trading bot

Currently building a trading bot from Scratch 
I will add as many comments as I can to each section to make sure there is full understanding!

This will be getting built on bit after bit after bit.

Purpose of each object will be listed here. This will also be the order that each object is being configured

Robot Object
- The purpose of this object is kind of like the entry point into this whole project as a whole.
- This robot object is really going to represent me and I will do certain things like specifying a trades, using indicators, building portfolios.
- This object will form as an entry point into the other objects
- The methods that have been defined in the robot object will return other objects that will be defined later on
- This object will have properties that can help answer common questions when we are trading. E.g., when does the regular market open up?

Portfolio Object 
- Where we are going to mimick a portfolio, and a portfolio is made up of positions.
- Positions represents some type of financial instrument that has some information about some things like assert type, purchase type, purchase date etc.
- It can help us to determine when to execute certain strategies and in a lot of cases when to enter or exit certain positions.
    - Some basic questions may rise up like 'Is this position profitable?', 'Do we own this position?' etc.
    - This object will allow to have some type of easy mechanism for being able to ask those questions as we are running our robot 

Indicators Object 

Stock Frame Object 

Trades Object 

There are things that I will neeed to research on and change but will get to that when it's time.
Those things include:
 1) Finding out the time openings and closings for each session
 2) The current timezone is based off US timezone, so I need to figure out how to change to UK timezone
