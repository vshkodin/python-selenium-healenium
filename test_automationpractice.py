import pytest



def test_one(init_run,driver_init):

    if init_run:
        print("RECORD HTML THREE DUE RUN")
        print("IF TITLE OF THE PAGE DIFF CREATE NEW FILE")
    assert 1


    #elem = driver_init.find_element_by_css_selector('a[title="Women"]')
    #elem.click()
    #print(driver_init.page_source)
    #assert "Women - My Store" in driver_init.title