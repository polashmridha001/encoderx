#!/usr/bin/env python3
import urllib.parse
import html
import base64
import binascii
import sys
import os

def banner():
    os.system("clear")
    print("""

██████╗  ██████╗ ██╗      █████╗ ███████╗██╗  ██╗    ███╗   ███╗██████╗ ██╗██████╗ ██╗  ██╗ █████╗ 
██╔══██╗██╔═══██╗██║     ██╔══██╗██╔════╝╚██╗██╔╝    ████╗ ████║██╔══██╗██║██╔══██╗╚██╗██╔╝██╔══██╗
██████╔╝██║   ██║██║     ███████║███████╗ ╚███╔╝     ██╔████╔██║██████╔╝██║██║  ██║ ╚███╔╝ ███████║
██╔═══╝ ██║   ██║██║     ██╔══██║╚════██║ ██╔██╗     ██║╚██╔╝██║██╔═══╝ ██║██║  ██║ ██╔██╗ ██╔══██║
██║     ╚██████╔╝███████╗██║  ██║███████║██╔╝ ██╗    ██║ ╚═╝ ██║██║     ██║██████╔╝██╔╝ ██╗██║  ██║
╚═╝      ╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    ╚═╝     ╚═╝╚═╝     ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
                                   By POLASH MRIDHA 🔥 | DEVIL MODE 😈
    """)

def url_encode(data):
    return urllib.parse.quote(data)

def html_encode(data):
    return html.escape(data)

def base64_encode(data):
    return base64.b64encode(data.encode()).decode()

def hex_encode(data):
    return binascii.hexlify(data.encode()).decode()

def unicode_encode(data):
    return ''.join(['\\u{:04x}'.format(ord(c)) for c in data])

def main():
    banner()
    data = input("🔹 Enter the character or string to encode: 👉 ")
    print("\n📤 Encoding Result:\n")
    print(f"🔸 URL Encode     : {url_encode(data)}")
    print(f"🔸 HTML Encode    : {html_encode(data)}")
    print(f"🔸 Base64 Encode  : {base64_encode(data)}")
    print(f"🔸 Hex Encode     : {hex_encode(data)}")
    print(f"🔸 Unicode Encode : {unicode_encode(data)}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[❌] Ctrl+C detected. Exit.")
        sys.exit()
