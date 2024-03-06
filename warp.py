import ipaddress, platform, subprocess, os, datetime, base64, json

warp_cidr = [
        '162.159.192.0/24',
        '162.159.193.0/24',
        '162.159.195.0/24',
        '162.159.204.0/24',
        '188.114.96.0/24',
        '188.114.97.0/24',
        '188.114.98.0/24',
        '188.114.99.0/24'
    ]

script_directory = os.path.dirname(__file__)
ip_txt_path = os.path.join(script_directory, 'ip.txt')
result_path = os.path.join(script_directory, 'result.csv')

def create_ips():
    c = 0
    total_ips = sum(len(list(ipaddress.IPv4Network(cidr))) for cidr in warp_cidr)

    with open(ip_txt_path, 'w') as file:
        for cidr in warp_cidr:
            ip_addresses = list(ipaddress.IPv4Network(cidr))
            for addr in ip_addresses:
                c += 1
                file.write(str(addr))
                if c != total_ips:
                    file.write('\n')

if os.path.exists(ip_txt_path):
    print("ip.txt exist.")
else:
    print('Creating ip.txt File.')
    create_ips()
    print('ip.txt File Created Successfully!')

def arch_suffix():
    machine = platform.machine().lower()
    if machine.startswith('i386') or machine.startswith('i686'):
        return '386'
    elif machine.startswith(('x86_64', 'amd64')):
        return 'amd64'
    elif machine.startswith(('armv8', 'arm64', 'aarch64')):
        return 'arm64'
    elif machine.startswith('s390x'):
        return 's390x'
    else:
        raise ValueError("Unsupported CPU architecture")

arch = arch_suffix()

print("Fetch warp program...")
url = f"https://gitlab.com/Misaka-blog/warp-script/-/raw/main/files/warp-yxip/warp-linux-{arch}"

subprocess.run(["wget", url, "-O", "warp"])
os.chmod("warp", 0o755)
command = "./warp >/dev/null 2>&1"
print("Scanning ips...")
process = subprocess.Popen(command, shell=True)
# Wait for the process to finish
process.wait()

# Check if there's any error
if process.returncode != 0:
    print("Error: Warp execution failed.")
else:
    print("Warp executed successfully.")

def warp_ip():
    counter = 0
    config_prefixes = ""
    creation_time = os.path.getctime(result_path)
    formatted_time = datetime.datetime.fromtimestamp(creation_time).strftime("%Y-%m-%d %H:%M:%S")
    with open(result_path, 'r') as csv_file:
        next(csv_file)
        for ips in csv_file:
            counter += 1
            if counter == 11:
                break
            else:
                ip = ips.split(',')[0]
                config_prefix = f'warp://{ip}?ifp=10-20&ifps=40-100&ifpd=10-20#Warp-{counter}\n'
                config_prefixes += config_prefix
    return config_prefixes, formatted_time

title = "//profile-title: base64:" + base64.b64encode('CHEF_WG ✌️'.encode('utf-8')).decode('utf-8') + "\n"
update_interval = "//profile-update-interval: 1\n"
sub_info = "//subscription-userinfo: upload=0; download=0; total=10737418240000000; expire=2546249531\n"
profile_web = "//profile-web-page-url: https://github.com/ByteMysticRogue\n"
last_modified = "//last update on: " + warp_ip()[1] + "\n"
configs = warp_ip()[0]
with open('warp.txt', 'w') as op:
    op.write(title + update_interval + sub_info + profile_web  + last_modified + configs)