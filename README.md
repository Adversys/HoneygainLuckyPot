# 🍯 Honeygain LuckyPot Auto (Raspberry Pi & Linux)
Automate the opening of the Honeygain LuckyPot via a lightweight Python script using only the official API. Works without a browser and is compatible with Raspberry Pi, Linux servers, and VPS.

---------------------------------------

## 🚀 Description
This script automatically opens the Honeygain LuckyPot every 15 minutes via cron. Logs are integrated into luckypot.log. No browser or Selenium required.

---------------------------------------

## 🔧 Configuration
After cloning the repository, configure your Honeygain credentials:

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

--------------------------------------

# 🛠 HoneygainLuckyPot Test & Verification Commands

## Manually run the script and check the log
python3 luckypot.py
cat luckypot.log

## Check if the cron is installed correctly
crontab -l

## Check the live log file
tail -f luckypot.log

## Check that the secrets.py file is installed and correct
cat secrets.py

## Check that the cron is running every 15 minutes
grep "luckypot.py" <(crontab -l)

## Check folder permissions
ls -lh /home/Adversys/HoneygainLuckyPot

## Force an immediate opening of the LuckyPot
python3 luckypot.py

## Check if the required modules are installed (should return without errors)
python3 -c "import requests, dotenv"
