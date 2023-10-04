from datetime import datetime

from test_POM.generic.Driver import DriverManager


class OddFetcher:
    _oddfetcherDriver = None

    def __init__(self):
        super(OddFetcher, self).__init__()
        self._oddfetcherDriver = DriverManager.get_driver()
        self.launch()

    def fetch_odds(self, param):
        '''

        :param param: list of races every seconds. races is a list of bet365 urls.
        :return: Return odds as a dictionary: {url: {runner_name_1 : fixed win odds, runner_name_2 : fixed win odds, ...}, ...}
If a runner doesn't have valid fixed win odds (i.e. 'SP' or something else thats not a valid float), simply return "None"


        fetch_odds(races) : This method will be called with a list of races every seconds. races is a list of bet365 urls. I don't want the program
opening a window every time its called, navigating to each of the urls, and returning the odds, this is too slow.
One browser window should be opened and maintained, when this function is called, the browser should open tabs for the urls it doesn't
already have opened.
Otherwise simply scrape the odds from the tab thats already opened.
This is much quicker and means this function should be able to return almost instantly if there are no new urls.
When this function is called, iterate through the urls, if we don't have a tab for it, open one, at the end, if we have a tab open that isn't in
the races list, close it as we don't need it anymore.
Return odds as a dictionary: {url: {runner_name_1 : fixed win odds, runner_name_2 : fixed win odds, ...}, ...}
If a runner doesn't have valid fixed win odds (i.e. 'SP' or something else thats not a valid float), simply return "None"
        '''
        pass

    def _get_upcomming_markets(self):
        '''
        _get_upcomming_markets() :
        This method should go onto "https://www.bet365.com.au/#/AS/B2/" for example (and the equivalents for harness-racing and
        greyhounds) and get links to all races in the next hour.
        This function should return a dataframe with the following columns:
        url to the market
        event_venue (name of the venue the race is running at)
        race_number
        race_type ('greyhound', 'horse-racing', 'harness-racing')
        market_start_time (seconds since epoch in UTC)
        '''
        # pageSource = self._oddfetcherDriver.page_source
        # soup = BeautifulSoup(pageSource, 'html.parser')
        # with open("temp/demo.html",'w+') as file:
        #     file.write(pageSource)
        # Initialize lists to store the extracted data

        """
        For All Races
        """
        xpath_for_races_within_60_mins = "//*[@id='__next']//table/tbody/tr/td/a//child::div[contains(text(), 'm') and number(substring-before(text(), 'm')) < 61]"
        xpath_for_event_venue = "//*[@id='__next']//table/tbody/tr/td/a//child::div[contains(text(), 'm') and number(substring-before(text(), 'm')) < 61 and number(substring-before(text(), 'm'))>0]/parent::node()/parent::node()/parent::node()/td/a"
        '''
        //*[@id='__next']//table/tbody/tr/td/a//child::div[contains(text(), 'm') and number(substring-before(text(), 'm')) < 61 and number(substring-before(text(), 'm'))>0]
        '''
        xpath_for_races_url = "//*[@id='__next']//table/tbody/tr/td/a//child::div[contains(text(), 'm') and number(substring-before(text(), 'm')) < 61 and number(substring-before(text(), 'm'))>0]/parent::a"



        event_venues = []
        race_numbers = []
        race_types = []
        market_start_times = []

        self._oddfetcherDriver.find_elements()

        # Extract data from the webpage based on its structure
        # Modify this part according to the structure of the website you are scraping
        # Example structure: <div class="event">...</div>
        for event in soup.find_all('div', class_='event'):
            event_venue = event.find('span', class_='venue').text
            race_number = event.find('span', class_='race-number').text
            race_type = event.find('span', class_='race-type').text
            start_time_str = event.find('span', class_='start-time').text
            market_start_time = int(datetime.strptime(start_time_str, '%Y-%m-%d %H:%M:%S').timestamp())

            event_venues.append(event_venue)
            race_numbers.append(race_number)
            race_types.append(race_type)
            market_start_times.append(market_start_time)

        # Create a DataFrame from the extracted data
        # from urllib3.util import url
        race_df = pd.DataFrame({  # 'url_to_market': [url] * len(event_venues),
            # 'event_venue': event_venues,
            # 'race_number': race_numbers,
            # 'race_type': race_types,
            # 'market_start_time': market_start_times
            "as": "as"})

        return race_df

    def launch(self):
        print(self._oddfetcherDriver)
        self._oddfetcherDriver.get('https://betm.com.au/racing/today')
