from demoqa import Demoqa


def test_demoqa(setup):
    page = Demoqa(setup, "https://demoqa.com/")
    page.go_to_site()
    url = page.get_current_url()
    assert url == "https://demoqa.com/"
    page.click_elements_button()
    url = page.get_current_url()
    assert url == "https://demoqa.com/elements"
    page.click_check_box_menu_item()
    url = page.get_current_url()
    assert url == "https://demoqa.com/checkbox"
    page.click_toggle_button()
    page.click_toggle_button_download()
    page.click_word_file()
    text = page.success_text().strip()
    assert text == "You have selected :\nwordFile"

