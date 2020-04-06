---
layout: default
title: MyEtherWallet troubleshooting
nav_order: 1
has_children: false
parent: Troubleshooting
grand_parent: BitBox02
---

# {{page.grand_parent}}: {{page.title}}
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

If you are having issues using MyEtherWallet with the BitBox02,please take a look at the list below to find your specific issue and respective fix.

#### Issue: Unlock BitBox02

- Unlock BitBox02 by entering your password on the device

#### Issue: Unexpected error

- Disconnect and reconnect the BitBox02 and try again.

#### Issue: Action aborted by user.

- You cancelled a process on the BitBox02. Try again.

#### Issue: Your BitBox02 is not initialized

- The BitBox02 is not set up yet. Download and install the [BitBoxApp](https://shiftcrypto.ch/start/) to setup your BitBox02.

#### Issue: Please upgrade to the newest firmware using Shift Cryptosecurity's BitBoxApp

- Your BitBox02 firmware is out of date. Open the BitBoxApp to update the BitBox02

#### Issue: MyEtherWallet does not yet support this version of the firmware.

- MyEtherWallet may need to update. Try to hard refresh by clicking ctrl-F5 when on the MyEtherWallet page. If this does not work, it is possible you need to wait for MyEtherWallet to release an update.

#### Issue: Trying to connect from a non-whitelisted origin.

- Attention! You may be on a phishing site. Please check if the URL is correct. The URL for MyEtherWallet should be myetherwallet.com.

#### Issue: BitBoxBridge not found

- To use MyEtherWallet, you need to download and install the [BitBoxBridge](https://shiftcrypto.ch/start/)

- If BitBoxBridge is already installed, make sure service is running:

**Windows**

- In search bar type **services**
- Find **bitbox-bridge**
- Check it’s status.

If status is empty, right click on bitbox-bridge and click Start

To make sure the BitBoxBridge starts on boot, right click bitbox-bridge -> properties then select in startup type automatic

**macOS**

-	Open Activity Monitor and look for the service **bitbox-bridge**. 

If it is not listed there, then the service is not running.

You can also see if the service is running using the Terminal:

- Open Terminal
- Insert command: 
`sudo launchctl list | grep shift`

If there is a number in the PID column, it is running. 

To restart the BitBoxBridge, do the following:

-	Launchd  something something something dark side something something something complete
-	Open the Terminal
-	Insert the following commands:
`sudo launchctl stop ch.shiftcrypto.bitboxbridge`
`sudo launchctl start ch.shiftcrypto.bitboxbridge`


Log files are in /opt/shiftcrypto/bitbox-bridge/logs

Linux:

`$ sudo systemctl stop bitbox-bridge`
`$ sudo systemctl start bitbox-bridge`
`$ systemctl status bitbox-bridge`

Example:

bitbox-bridge.service - Shiftcrypto BitBoxBridge
   Loaded: loaded (/usr/lib/systemd/system/bitbox-bridge.service; enabled; vendor preset: enabled)
   Active: active (running) since Fri 2020-02-07 22:58:31 CET; 24s ago
 Main PID: 4556 (bitbox-bridge)
	Tasks: 6 (limit: 4915)
   Memory: 4.4M
   CGroup: /system.slice/bitbox-bridge.service
       	└─4556 /opt/bitbox-bridge/bin/bitbox-bridge

#### Issue: Expected exactly one BitBox02. No or more than one BitBox02 detected.

Please make sure you only have one BitBox02 plugged in at a time.

#### Issue: Pairing rejected on device, please try again

Reconnect the BitBox02 and accept the pairing code by clicking the “check mark” on the BitBox02 when prompted.

#### Issue: Your BitBox02 is busy. Please close all other wallets and try again.

-	Close the BitBoxApp
-	Close any other wallets you may have open using the BitBox02. Such as Electrum.

#### Issue: Device attestation failed

-	Reconnect BitBox02 and try again
-	If you keep getting the warning. Please contact support@shiftcrypto.ch 

#### Issue: Unsupported BitBox device

MyEtherWallet only supports the BitBox02 Multi edition or the BitBox02. If you are using a BitBox02 Bitcoin-only edition, it is not compatible with MyEtherWallet because it does not support Ethereum.

#### Issue: Plug in BitBox02 and choose screen orientation by tapping one of the sides.

-	Make sure BitBox02 is inserted into USB and powered.
-	Choose orientation of BitBox02 by tapping one of the sides of the device. USB connection is only established after you choose the screen orientation.

If you are still experiencing issues, please contact support@shiftcrypto.ch