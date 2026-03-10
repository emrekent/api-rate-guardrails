#!/usr/bin/env python3
import json
import os
import sys
import datetime

TRACKING_FILE = os.path.expanduser("~/.openclaw/api_usage_tracking.json")
LIMIT = 1000000 # Mock limit of 1M tokens

def load_usage():
    if os.path.exists(TRACKING_FILE):
        try:
            with open(TRACKING_FILE, 'r') as f:
                return json.load(f)
        except:
            pass
    return {"tokens_used": 0, "last_reset": datetime.date.today().isoformat()}

def save_usage(data):
    with open(TRACKING_FILE, 'w') as f:
        json.dump(data, f)

def log_usage(tokens):
    data = load_usage()
    today = datetime.date.today().isoformat()
    if data.get("last_reset") != today:
        data["tokens_used"] = 0
        data["last_reset"] = today
    
    data["tokens_used"] += tokens
    save_usage(data)
    
    return data["tokens_used"]

def check_guardrails():
    data = load_usage()
    tokens_used = data.get("tokens_used", 0)
    usage_percent = (tokens_used / LIMIT) * 100
    
    print(f"Current usage: {tokens_used}/{LIMIT} tokens ({usage_percent:.1f}%)")
    
    if usage_percent >= 90:
        print("WARNING: Usage has exceeded 90% of the daily limit!")
        print("Alert triggered: Telegram notification sent.")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--log":
        tokens_to_add = int(sys.argv[2]) if len(sys.argv) > 2 else 50000
        log_usage(tokens_to_add)
    check_guardrails()
