link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_items(browser):
    browser.implicitly_wait(5)
    browser.get(link)
    assert browser.find_element_by_css_selector("button.btn-add-to-basket").is_displayed() == True, "Кнопка не найдена"