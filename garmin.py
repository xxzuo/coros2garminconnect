from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright, account: dict, path: str) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://www.baidu.com/
    page.goto("https://www.baidu.com/")

    # Go to https://connect.garmin.cn/
    page.goto("https://connect.garmin.cn/")

    # Click text=登录
    page.locator("text=登录").click()
    page.wait_for_url("https://connect.garmin.cn/signin")

    # Click input[name="username"]
    page.frame_locator("#gauth-widget-frame-gauth-widget").locator("input[name=\"username\"]").click()

    # Fill input[name="username"]
    page.frame_locator("#gauth-widget-frame-gauth-widget").locator("input[name=\"username\"]").fill(account["username"])

    # Click input[name="password"]
    page.frame_locator("#gauth-widget-frame-gauth-widget").locator("input[name=\"password\"]").click()

    # Fill input[name="password"]
    page.frame_locator("#gauth-widget-frame-gauth-widget").locator("input[name=\"password\"]").fill(account["password"])

    # Click button:has-text("登录")
    page.frame_locator("#gauth-widget-frame-gauth-widget").locator("button:has-text(\"登录\")").click()

    page.wait_for_url("https://connect.garmin.cn/modern/")

    # Click [aria-label="上传或导入活动"]
    page.locator("[aria-label=\"上传或导入活动\"]").click()

    # Click text=导入数据
    page.locator("text=导入数据").click()
    page.wait_for_url("https://connect.garmin.cn/modern/import-data")

    # Click text=浏览
    page.locator("text=浏览").click()

    with page.expect_file_chooser() as fc_info:
        page.click("upload")
    file_chooser = fc_info.value
    file_chooser.set_files(path)
    # Click button:has-text("导入数据")
    page.locator("button:has-text(\"导入数据\")").click()

    # Click text=查看详情
    page.locator("text=查看详情").click()

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


def upload_data_to_garmin(garmin_username: str, garmin_password: str, local_file_path: str):
    garmin_account = {"username": garmin_username, "password": garmin_password}
    with sync_playwright() as playwright:
        run(playwright, garmin_account, local_file_path)
