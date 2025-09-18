# 🧪 QA Automation Demo (Pytest + Selenium)

Project ini adalah contoh **QA Automation** menggunakan:
- [Pytest](https://docs.pytest.org/)
- [Selenium](https://www.selenium.dev/)
- [pytest-html](https://pypi.org/project/pytest-html/) → generate HTML report
- [webdriver-manager](https://github.com/SergeyPirogov/webdriver_manager) → auto download driver

# 🚀 Quick Start

# 1) Clone repo
```
git clone https://github.com/USERNAME/qa-automation-demo.git
cd qa-automation-demo
```

# 2) Buat virtual environment & aktifkan
Mac / Linux:
```
python3 -m venv venv
source venv/bin/activate
```

Windows (PowerShell):
```
python -m venv venv
venv\Scripts\activate
```

# 3) Install dependencies
```
pip install --upgrade pip
pip install -r requirements.txt
```
Isi requirements.txt:
```
pytest
selenium
pytest-html
webdriver-manager
```

# 4) Jalankan test
Semua test:
`pytest -v
`
Test spesifik:
`pytest tests/test_login.py::test_login_success -v
`

Buka report:
- macOS: open reports/login-report.html
- Linux: xdg-open reports/login-report.html
- Windows: start reports\login-report.html

<img width="797" height="356" alt="image" src="https://github.com/user-attachments/assets/3c8ae385-8829-4cee-b6e7-8defec1b55a5" />

