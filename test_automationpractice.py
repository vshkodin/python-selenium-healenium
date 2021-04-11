import pytest


def test_one(init_run, driver_init):
    if init_run:
        driver_init.click('a[title="Women"]')
        #print(driver_init.page_source())
        assert "Women - My Store" in driver_init.title()
        driver_init.get("http://automationpractice.com/index.php")
        print("RECORD HTML THREE DUE RUN")
        print("IF TITLE OF THE PAGE DIFF CREATE NEW FILE")
    assert 1
