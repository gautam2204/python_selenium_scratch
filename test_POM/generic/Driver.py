from selenium import webdriver


class DriverManager:
    _driver = None

    @classmethod
    def get_driver(cls):
        if cls._driver is None:
            proxies = {
                'https': 'https://144.48.38.39:8443'
            }
            options = webdriver.ChromeOptions()
            # options.set_capability("proxy", value=proxies)
            cls._driver = webdriver.Chrome(options=options)
            return cls._driver
        return cls._driver

