# Pi Zero WebControl

Webbasierte Steuerzentrale für den Raspberry Pi Zero W.
- Steuert Motoren, Lüfter, Servos, LEDs (PWM) über ein modernes Webinterface (Darkmode)
- Anzeige des Status auf Waveshare 1,3-Inch LCD (240x240)
- Alles konfigurierbar im Web (Pins, Geräte, Gruppen, Presets, WLAN)
- Hotspot/Access Point: SSID `Cortana` / PW `ChangeMe` (änderbar)
- Einfach erweiterbar, keine .json-Edits nötig

## Setup
1. Raspberry Pi OS Lite installieren, SSH aktivieren
2. `git clone ...`
3. `cd pi-zero-webcontrol`
4. `bash scripts/setup_hotspot.sh`
5. `bash run.sh`
6. WLAN: `Cortana`, PW: `ChangeMe`, Web: http://192.168.4.1
7. Login: admin / ChangeMe
