import nmap
scanner = nmap.PortScanner()

target = input("Enter IP: ")
print(f"\nScanning {target}...\n")
scanner.scan(target, '1-1000', '-Pn')

for host in scanner.all_hosts():
    print(f"Host: {host} -> {scanner[host].state()}")
    try:
        for proto in scanner[host].all_protocols():
            lport = scanner[host][proto].keys()
            for port in sorted(lport):
                state = scanner[host][proto][port]['state']
                print(f"Port {port} : {state} -> Find Open!")
    except:
        print("No Port open in this range")

print("\nSearch Done")