#!/bin/bash

# Stop kalau ada error
set -e

# 1. Buat virtual environment
echo "📦 Membuat virtual environment..."
python3 -m venv venv

# 2. Aktifkan venv
echo "🔑 Aktivasi virtual environment..."
source venv/bin/activate

# 3. Upgrade pip
echo "⬆️ Upgrade pip..."
pip install --upgrade pip

# 4. Install dependencies
echo "📥 Install dependencies..."
pip install pytest pytest-html selenium webdriver-manager

# 5. Jalankan test + HTML report
echo "🚀 Menjalankan test..."
pytest -v --html=reports/login-report.html --self-contained-html
