````
███████ ██ ███    ██  ██████        ██████   ██████  ██   ██     ████████ ███████ ███    ███ ██████  ██       █████  ████████ ███████ ███████ 
██      ██ ████   ██ ██             ██   ██ ██    ██  ██ ██         ██    ██      ████  ████ ██   ██ ██      ██   ██    ██    ██      ██      
███████ ██ ██ ██  ██ ██   ███ █████ ██████  ██    ██   ███          ██    █████   ██ ████ ██ ██████  ██      ███████    ██    █████   ███████ 
     ██ ██ ██  ██ ██ ██    ██       ██   ██ ██    ██  ██ ██         ██    ██      ██  ██  ██ ██      ██      ██   ██    ██    ██           ██ 
███████ ██ ██   ████  ██████        ██████   ██████  ██   ██        ██    ███████ ██      ██ ██      ███████ ██   ██    ██    ███████ ███████
````
# Configs

This repository contains various configuration settings for both Client-side and Server-Side:

- <span style="font-size: larger;"> Inbound-Outbound sample
- <span style="font-size: larger;"> ShadowTLS-v3
- <span style="font-size: larger;"> TrojanGFW-tls
- <span style="font-size: larger;"> TrojanGFW-tls-gRPC
- <span style="font-size: larger;"> TUIC v5
- <span style="font-size: larger;"> vless-reality-gRPC
- <span style="font-size: larger;"> vless-reality-HTTP
- <span style="font-size: larger;"> vless-reality-TCP
- <span style="font-size: larger;"> vmess-TCP-tls-HTTP Camouflage 
- <span style="font-size: larger;"> vmess-tls-gRPC
- <span style="font-size: larger;"> vmess-tls-WebSocket (ws)

# [Sing-Box Installation](https://sing-box.sagernet.org/installation/package-manager/)

### <img width="20" height="20" src="icons/ubuntu.svg"/> Ubuntu/ <img width="20" height="20" src="icons/debian.svg"/> Debian
````
bash <(curl -fsSL https://sing-box.app/deb-install.sh)
````
### <img width="20" height="20" src="icons/redhat.svg"/> Redhat/RPM
````
bash <(curl -fsSL https://sing-box.app/rpm-install.sh)
````
### <img width="20" height="20" src="icons/arch.svg"/> Archlinux/PKG
````
bash <(curl -fsSL https://sing-box.app/arch-install.sh)
````

### Config PATH
````
cd /etc/sing-box
````
### Edit Config File
````
nano /etc/sing-box/config.json
````
# Sing-Box Operation
| Operation   | Command                               |
|-------------|---------------------------------------|
| Enable      | `sudo systemctl enable sing-box`      |
| Disable     | `sudo systemctl disable sing-box`     |
| Start       | `sudo systemctl start sing-box`       |
| Stop        | `sudo systemctl stop sing-box`        |
| Kill        | `sudo systemctl kill sing-box`        |
| Restart     | `sudo systemctl restart sing-box`     |
| Logs        | `sudo journalctl -u sing-box --output cat -e` |
| New Logs    | `sudo journalctl -u sing-box --output cat -f` |

# Sing-Box Commands

To verify whether the configuration file is correctly set up:
- If you are in the /etc/sing-box folder:
````
sing-box check
````
- If you are in a different location:
````
sing-box check -c <PATH_TO_CONFIG_FILE>
````

To run Sing-Box:

As a service:
````
systemctl start sing-box.service
````
Standalone:
````
sing-box run -c <PATH_TO_CONFIG_FILE>
````