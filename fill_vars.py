import os
from dotenv import load_dotenv, find_dotenv, set_key
load_dotenv(find_dotenv())

# A simple script for fast vars filling into bot
# Credit goes to -> Ayush

print("A simple script for fast vars filling into bot!\nNow Give the vars carefully: \n")
set_key('.env','API_ID', input("API_ID : "))
set_key('.env','API_HASH', input("API_HASH : "))
set_key('.env','BOT_TOKEN', input("BOT_TOKEN : "))
set_key('.env','MONGO_DB_URI', input("MONGO_DB_URI : "))
set_key('.env','OWNER_ID', input("OWNER_ID : "))
set_key('.env','LOG_GROUP_ID', input("LOG_GROUP_ID : "))
set_key('.env','STRING_SESSION', input("STRING_SESSION 1 : "))
set_key('.env','STRING_SESSION2', input("STRING SESSION 2 : "))
set_key('.env','STRING_SESSION3', input("STRING SESSION 3 : "))
set_key('.env','STRING_SESSION4', input("STRING SESSION 4 : "))
set_key('.env','STRING_SESSION5', input("STRING SESSION 5 : "))
set_key('.env','STRING_SESSION6', input("STRING SESSION 6 : "))
set_key('.env','STRING_SESSION7', input("STRING SESSION 7 : "))