
import pandas as pd
from time import sleep
# initialise odd_fetcher
from test_POM.pages.bet_placer import BetPlacer
from test_POM.pages.odd_fetcher import OddFetcher

bet365_odds = OddFetcher()
# initialise bet placer
bet365_placer = BetPlacer("username", "password")
# We should now have two chrome windows open, one for fetching odds and tracking markets
# Another which sits idle, logged in, waiting to navigate and place a bet when its requested
upcomming_races, track_races = None, None
i = 0
while True:
  # every 100 iterations, refetch the new upcomming races
  if i % 100 == 0:
    # get the upcomming races
    upcomming_races : pd.DataFrame = bet365_odds._get_upcomming_markets()
    # get the upcomming 10 races to track
    track_races = upcomming_races.head(10)
    # fetch the odds for the upcomming races (this should be quick as possible!)
    # urls will be constant until 'track_races' is updated
    # so the odd_fetcher should be efficient and maintain tabs for urls as they're needed
    odds = bet365_odds.fetch_odds(list(track_races.url))
    # example strategy
    for race_url in odds:
      for runner_name, fixed_odd in odds[race_url].items():
        if runner_name == 'Example Runner' and fixed_odd == 2.50:
          # bet 1 dollar as an example
          bet365_placer.place_bet(race_url, runner_name, fixed_odd, 1)
          # sleep before going again
          sleep(2)

