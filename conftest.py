import pytest

from selenium import webdriver
import chromedriver_binary  # Adds chromedriver binary to path


def pytest_addoption(parser):
    parser.addoption("--name", action="store", default=False)
    parser.addoption("-H",action="store_true", default=False)




def pytest_sessionfinish(session, exitstatus):
    # print("session---->>>>>", session)
    # print("session---->>>>>", type(session))
    # print("session---->>>>>", dir(session))
    # print("session---->>>>>", session.Failed)
    # for i in inspect.getmembers(session):
    #     # to remove private and protected
    #     # functions
    #     if not i[0].startswith('_'):
    #         # To remove other methods that
    #         # doesnot start with a underscore
    #         if not inspect.ismethod(i[1]):
    #             print(i)
    print('\n')
    print()
    if session.testsfailed:

        print("\n"*5)
        print(' |-------------------------------------|',"\n",
              '|                                     |',"\n",
              '|                                     |',"\n",
              f'|            !{session.testsfailed}!   Test Failures      |',"\n",
              '|                                     |',"\n",
              '|                ||                   |',"\n",
              '|                ||                   |',"\n",
              '|                ||                   |',"\n",
              r'|               \  /                  |',"\n",
              r'|                \/                   |',"\n",
              r'|                                     |',"\n",
              '|                                     |', "\n",
              '|_____________________________________|' )



@pytest.fixture()
def driver_init():
    driver = webdriver.Chrome()
    driver.get("http://automationpractice.com/index.php")
    driver.implicitly_wait(15)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def name(request):
    return request.config.getoption("--name")
@pytest.fixture()
def H(request):
    return request.config.getoption("-H")