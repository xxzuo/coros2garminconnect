from playwright.sync_api import Playwright, sync_playwright, expect
import time


def run(playwright: Playwright, account: dict, path: str) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://t.coros.com/
    page.goto("https://t.coros.com/")

    # Go to https://t.coros.com/login
    page.goto("https://t.coros.com/login")

    # Click [placeholder="请输入邮箱账号"]
    page.locator("[placeholder=\"请输入邮箱账号\"]").click()

    # Fill [placeholder="请输入邮箱账号"]
    page.locator("[placeholder=\"请输入邮箱账号\"]").fill(account["username"])

    # Click [placeholder="请输入6-20个字符的密码"]
    page.locator("[placeholder=\"请输入6-20个字符的密码\"]").click()

    # Fill [placeholder="请输入6-20个字符的密码"]
    page.locator("[placeholder=\"请输入6-20个字符的密码\"]").fill(account["password"])

    # Click text=邮箱ID 密码 记住密码 忘记密码？ 我已阅读并同意COROS的隐私政策 登录 >> i >> nth=4
    page.locator("text=邮箱ID 密码 记住密码 忘记密码？ 我已阅读并同意COROS的隐私政策 登录 >> i").nth(4).click()

    # Click text=登录
    page.locator("text=登录").click()
    time.sleep(4)
    # Go to https://trainingcn.coros.com/admin/views/dash-board
    page.goto("https://trainingcn.coros.com/admin/views/dash-board")

    # Click text=活动列表
    page.locator("text=活动列表").click()
    page.wait_for_url("https://trainingcn.coros.com/admin/views/activities")

    # 最新一条记录数据
    with page.expect_popup() as popup_info:
        page.click("xpath=//tr[@class='table-tr data-row hover-effect'][1]/td[2]//a[1]")
    page1 = popup_info.value
    page1.wait_for_load_state('networkidle')
    time.sleep(5)
    with page1.expect_download() as download_info:
        page1.click("xpath=//i[@title='导出']")
    download = download_info.value
    download.save_as(path)
    # Close page
    page1.close()

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


def download_coros_data(coros_username: str, coros_password: str, save_path: str):
    coros_account = {"username": coros_username, "password": coros_password}
    with sync_playwright() as playwright:
        run(playwright, coros_account, save_path)
