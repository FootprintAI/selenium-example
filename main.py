import argparse

from examples.instagram import login as do_instagram_login;
from examples.goodinfo import query as do_goodinfo_find;
from examples.pyconf import do as do_query_pyorg;
from examples.browser import navigation as do_browser_history;
from examples.browser import get_cookies as get_browser_cookies;
from examples.exceptions import exception_handling as browser_exceprtion_handing;

def make_driver():
    from drivers.webdriver import WebDriver
    return WebDriver()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--action', dest='action', type=str, default='')

    args = parser.parse_args()
    webdriver = make_driver()

    if args.action == 'instagram_login':
        do_instagram_login(webdriver, "<your-username>", "<your-password>")
    elif args.action == 'goodinfo_find':
        do_goodinfo_find(webdriver, "2330")
    elif args.action == 'pyorg_find':
        do_query_pyorg(webdriver, "pycon")
    elif args.action == 'browser_cookies':
        get_browser_cookies(webdriver)
    elif args.action == 'exceptions':
        browser_exceprtion_handing(webdriver)
    else:
        do_browser_history(webdriver)


    webdriver.quit()

