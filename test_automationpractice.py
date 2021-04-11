import pytest


def test_automationpractice(init_run, driver_init):
    if init_run:
        driver_init.click('a[title="Women"]')
        assert "Women - My Store" in driver_init.title()
        driver_init.get("/index.php")
        driver_init.get("/index.php?controller=contact")
