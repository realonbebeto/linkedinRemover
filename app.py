
import random
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver


# Profile j0behg1h.linkedin
options = Options()
# options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('start-maximized')
options.add_argument(
    '--user-data-dir={}'.format('/home/main/snap/chromium/common/chromium'))
options.add_argument('--profile-directory={}'.format('Profile 2'))
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.get("https://www.linkedin.com/search/results/people/?keywords=copywriter&network=%5B%22F%22%5D&origin=FACETED_SEARCH&sid=(QZ")
time.sleep(1)
curr_win = driver.current_window_handle
print(curr_win)


def random_int(start, end):
    return random.randint(start, end)


def tab_switcher(curr_win):
    all_win = driver.window_handles
    for win in all_win:
        if win != curr_win:
            driver.switch_to.window(win)
            break

    time.sleep(0.9)


entities = driver.find_elements(By.CLASS_NAME, 'entity-result__item')

# [0].find_elements(By.CSS_SELECTOR, 'div.linked-area.flex-1.cursor-pointer')[0].click()

# time.sleep(1)
# tab_switcher(curr_win)
# pixel_scroll = random_int(300, 700)
# driver.execute_script(
#     f"window.scrollBy({{top: {pixel_scroll}, left: {0}, behavior: 'smooth'}})")

# driver.find_elements(By.CSS_SELECTOR, 'div.pv-top-card-v2-ctas')[0].find_elements(
#     By.CSS_SELECTOR, 'button.artdeco-dropdown__trigger.artdeco-dropdown__trigger--placement-bottom.ember-view.pvs-profile-actions__action.artdeco-button.artdeco-button--secondary.artdeco-button--muted.artdeco-button--2')[0].click()
# time.sleep(5)
# driver.execute_script(
#     f"window.scrollBy({{top: {random_int(1, 15)}, left: {0}, behavior: 'smooth'}})")
# pixel_scroll = random_int(200, 300)

# driver.execute_script(
#     f"window.scrollBy({{top: {pixel_scroll}, left: {0}, behavior: 'smooth'}})")

# more_buttons = driver.find_elements(
#     By.CSS_SELECTOR, 'div.artdeco-dropdown__content-inner')[1].find_elements(By.XPATH, "//ul/li/div[contains(@role, 'button')]")


for entity in entities:
    # Click to open new window
    entity.find_elements(
        By.CSS_SELECTOR, 'div.linked-area.flex-1.cursor-pointer')[0].click()

    # Swithch to new window
    tab_switcher(curr_win)

    # Dramatic Pause
    time.sleep(random_int(5, 11))

    pixel_scroll = random_int(500, 700)

    # Random Down Scroll
    driver.execute_script(
        f"window.scrollBy({{top: {pixel_scroll}, left: {0}, behavior: 'smooth'}})")

    # Dramatic Pause
    time.sleep(random_int(1, 7))

    # Random Up Scroll
    driver.execute_script(
        f"window.scrollBy({{top: {-pixel_scroll+random_int(0, 30)}, left: {0}, behavior: 'smooth'}})")

    # Find the More button and Click it
    driver.find_element(By.CSS_SELECTOR, 'div.pv-top-card-v2-ctas').find_element(
        By.CSS_SELECTOR, 'button.artdeco-dropdown__trigger.artdeco-dropdown__trigger--placement-bottom.ember-view.pvs-profile-actions__action.artdeco-button.artdeco-button--secondary.artdeco-button--muted.artdeco-button--2').click()
    # Dramatic Pause
    time.sleep(random_int(2, 31))

    pixel_scroll = random_int(200, 300)

    driver.execute_script(
        f"window.scrollBy({{top: {pixel_scroll}, left: {0}, behavior: 'smooth'}})")

    # Dramatic Pause
    time.sleep(random_int(2, 31))

    more_buttons = driver.find_elements(By.CSS_SELECTOR, 'div.artdeco-dropdown__content-inner')[
        1].find_elements(By.XPATH, "//ul/li/div[contains(@role, 'button')]")

    print(more_buttons[14].text)
    print(more_buttons[15].text)

    # Dramatic Pause
    time.sleep(random_int(1, 2))
    driver.close()

time.sleep(random_int())
# print(type(entities))
# print(entities)

# y = driver.find_elements(
#     By.XPATH, '//button[@class="artdeco-dropdown__trigger artdeco-dropdown__trigger--placement-bottom ember-view pvs-profile-actions__action artdeco-button artdeco-button--secondary artdeco-button--muted"]')
# print(y)
# time.sleep(5)
# print(driver.title)
driver.close()
