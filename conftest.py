import pytest
from selenium import webdriver

from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem


software_names = [SoftwareName.CHROME.value]
operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]

user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)

# get list of user agents.
user_agents = user_agent_rotator.get_user_agents()



@pytest.fixture()
def driver(request):
    options = webdriver.ChromeOptions()

    # get random user agent string
    # add user agent because Amazon and BestBuy both has headless protection
    user_agent = user_agent_rotator.get_random_user_agent()
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument("--start-maximized")

    options.add_argument('--no-sandbox')
    # in order to turn off/on headless mode please comment/uncomment a line below
    options.add_argument('headless')
    options.add_argument('disable-infobars')
    options.add_argument('window-size=1920x1080')
    options.add_argument('--verbose')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    wd = webdriver.Chrome(options=options)
    wd.implicitly_wait(5)
    request.addfinalizer(wd.quit)
    return wd
