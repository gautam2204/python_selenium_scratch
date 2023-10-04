from test_POM.generic.Driver import DriverManager


class BetPlacer:
    _betPlaceDriver=None
    loginUserName = ""
    loginPass = ""

    def __init__(self, userName:str, password:str):
        super(BetPlacer, self).__init__()
        self.loginUserName = userName
        self.loginPass = password
        self._betPlaceDriver = DriverManager.get_driver()
        self.launch()

    def doLogin(self):
        pass

    def place_bet(self, race_url, runner_name, fixed_odd, param):
        pass

    def launch(self):
        print(self._betPlaceDriver)
        self._betPlaceDriver.execute_script('window.open("https://www.dream11.com/dream11-team-today"),"_blank"')

