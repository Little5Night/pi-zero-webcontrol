#!/bin/bash
echo "Installiere Hostapd & Dnsmasq..."
sudo apt-get update
sudo apt-get install -y hostapd dnsmasq
# Beispiel-Konfigs, bitte anpassen für deine Netzwerkumgebung
echo "interface wlan0
    static ip_address=192.168.4.1/24
    nohook wpa_supplicant" | sudo tee /etc/dhcpcd.conf
echo "interface=wlan0
dhcp-range=192.168.4.2,192.168.4.20,255.255.255.0,24h" | sudo tee /etc/dnsmasq.conf
echo "country_code=DE
interface=wlan0
ssid=Cortana
hw_mode=g
channel=7
wmm_enabled=0
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_passphrase=ChangeMe
wpa_key_mgmt=WPA-PSK
rsn_pairwise=CCMP" | sudo tee /etc/hostapd/hostapd.conf
sudo systemctl unmask hostapd
sudo systemctl enable hostapd
sudo systemctl enable dnsmasq
sudo systemctl restart dhcpcd
sudo systemctl restart hostapd
sudo systemctl restart dnsmasq
echo "Hotspot mit SSID 'Cortana' und Passwort 'ChangeMe' aktiv!"
