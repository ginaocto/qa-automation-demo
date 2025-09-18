{\rtf1\ansi\ansicpg1252\cocoartf2706
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import pytest\
from selenium import webdriver\
from selenium.webdriver.chrome.service import Service\
from webdriver_manager.chrome import ChromeDriverManager\
from selenium.webdriver.chrome.options import Options\
import os\
\
@pytest.fixture\
def driver(request):\
    options = Options()\
    options.add_argument("--headless")  # hapus baris ini kalau mau lihat browser terbuka\
    options.add_argument("--no-sandbox")\
    options.add_argument("--disable-dev-shm-usage")\
\
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)\
    driver.implicitly_wait(5)\
\
    yield driver\
\
    # screenshot akhir setiap test\
    test_name = request.node.name\
    reports_dir = "reports/screenshots"\
    os.makedirs(reports_dir, exist_ok=True)\
    driver.save_screenshot(f"\{reports_dir\}/\{test_name\}.png")\
    driver.quit()\
\
\
# Screenshot tambahan kalau test gagal\
@pytest.hookimpl(hookwrapper=True)\
def pytest_runtest_makereport(item, call):\
    outcome = yield\
    rep = outcome.get_result()\
    if rep.when == "call" and rep.failed:\
        driver = item.funcargs.get("driver", None)\
        if driver:\
            reports_dir = "reports/screenshots"\
            os.makedirs(reports_dir, exist_ok=True)\
            driver.save_screenshot(f"\{reports_dir\}/\{item.name\}_FAILED.png")\
}