
import pytest



@pytest.mark.skip("temporaty")
def test_one(driver_init, name):
    print(name)
    elem = driver_init.find_element_by_css_selector('a[title="Women"]')
    elem.click()
    #print(driver_init.page_source)
    assert "Women - My Store" in driver_init.title

def test_two(name,H,request):
    if name:
        print('!!!!!!!!!! name :',name)

    if H:
        print('!!!!!! request -H',request.config.getoption("-H"))
        assert 0
    assert 1


