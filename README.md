# 🍯 Honeygain LuckyPot Auto (Raspberry Pi & Linux)
Automate the opening of the Honeygain LuckyPot via a lightweight Python script using only the official API. Works without a browser and is compatible with Raspberry Pi, Linux servers, and VPS.

---------------------------------------

## 🚀 Description
This script automatically opens the Honeygain LuckyPot every 15 minutes via cron. Logs are integrated into luckypot.log. No browser or Selenium required.

---------------------------------------

## 🔧 Configuration
After cloning the repository, configure your Honeygain credentials:

cp secrets.py.template secrets.py
nano secrets.py

--------------------------------------

## ✏️ Edit and replace with your information:

EMAIL = "your_email@example.com"
PASSWORD = "your_password"

--------------------------------------

## ⚙️ Automation
Once the secrets.py file is configured, run:

bash install_luckypot_auto.sh

--------------------------------------

## ❌ Uninstall
bash remove_luckypot_cron.sh

--------------------------------------

## ✅ Prerequisites
Python 3

Python modules: requests, python-dotenv
