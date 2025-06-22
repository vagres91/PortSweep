import socket
import threading
from datetime import datetime

# Kullanıcıdan hedef IP ve port aralığı al
target = input("🎯 Target IP or Hostname: ").strip()
start_port = int(input("🔢 Start Port: "))
end_port = int(input("🔢 End Port: "))

# Zaman başlat
print(f"\n🚀 Scanning {target} from port {start_port} to {end_port}...\nStarted at {datetime.now()}\n")

# Lock for clean output from threads
print_lock = threading.Lock()

# Port tarama fonksiyonu
def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            with print_lock:
                print(f"[OPEN] Port {port}")
        s.close()
    except:
        pass

# Thread'leri başlat
threads = []
for port in range(start_port, end_port + 1):
    t = threading.Thread(target=scan_port, args=(port,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

# Zaman bitişi
print(f"\n✅ Scan completed at {datetime.now()}")
