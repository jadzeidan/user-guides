---
layout: default
title: Mobile app pairing
nav_order: 1
parent: Advanced features
grand_parent: BitBox01
---
# {{page.grand_parent}}: {{page.title}}
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}


![alt text]({% link assets/images/BitBox01_pairing/pair1.png %})

There are two levels of pairing available:

## Level 1: Normal pairing
- Lets you verify addresses on your smartphone
- Requires you to confirm transactions on your smartphone

Use a mobile phone as a large screen for securely verifying transactions and receiving addresses created by the BitBox. This avoids man-in-the-middle attacks on computers that have been fully compromised (i.e. rooted). Optionally in addition, enable the mobile phone as a second-factor authorisation (2FA) device using the desktop app's 'Options' tab.
Technically, a private and encrypted communication channel between the mobile phone and the BitBox is created using a hashed Elliptic Curve Diffie–Hellman (ECDH) key exchange in combination with off-channel information from a blink code, using the BitBox's LED. All you need to do is count a few blinks and enter them in the mobile phone. See how below.


### 1. Get the mobile app
{: .no_toc }
Choose your platform to download our free mobile app.

- [iOS](https://itunes.apple.com/us/app/digital-bitbox-2fa/id1079896740)

- [Android](https://play.google.com/store/apps/details?id=com.digitalbitbox.tfa)

- [APK Download](https://github.com/digitalbitbox/2FA-app/releases)
    - Checksum: sha256sum - dbbc41907269605b2e1ec0af79b77af9c034e255f3f8d7b43fe3f11251f6df81

- [Source Code](https://github.com/digitalbitbox/2FA-app)



### 2. Pair the mobile app with your BitBox02
{: .no_toc }
Click "Pair Mobile App" in the BitBoxApp

![alt text]({% link assets/images/BitBox01_pairing/pair1.png %})

Confirm
![alt text]({% link assets/images/BitBox01_pairing/pair2.png  %})
In the mobile app click the "SCAN" button then scan the QR code shown in the BitBox desktop app.
![alt text]({% link assets/images/BitBox01_pairing/pair3.png  %})
Then wait a few seconds until a connection is established and click "begin" in the mobile app.
![alt text]({% link assets/images/BitBox01_pairing/pair4.png  %})
Your BitBox01 will then blink, asking you to perform a long-touch on the LED in order to confirm that you want to pair.

After that you will see the following screen on your mobile app. Please click "BLINK".
Your BitBox01 will then blink between 1-4 times, please count and press the correct number in the mobile app.
Please repeat that until you can click "FINISH"

![alt text]({% link assets/images/BitBox01_pairing/pair5.png  %})

You should then see a confirmation in the BitBoxApp.
![alt text]({% link assets/images/BitBox01_pairing/pair7.png  %})
In the "Manage Device" settings you should then see "Status" paired
![alt text]({% link assets/images/BitBox01_pairing/pair8.png  %})





### Verifying addresses and transactions
{: .no_toc }
Information received by the BitBox01 automatically displays in the mobile app when connected to the internet.
Otherwise, get the information by scanning QR codes presented by the desktop app.

![alt text]({% link assets/images/BitBox01_pairing/ios_receiving.png  %}){:height="250" width="250"}
![alt text]({% link assets/images/BitBox01_pairing/ios_sending_01.png  %}){:height="250" width="250"}



## Level 2: Full second-factor authorisation (2FA)
![alt text]({% link assets/images/BitBox01_pairing/ios_sending_01_lock.png  %}){:height="250" width="250"}

When full 2FA is enabled, possession of the mobile phone is required in order to spend coins. Full 2FA is enabled using the 'Settings' tab in the desktop app. Under the hood, an encrypted single-use PIN is sent to the mobile app, decrypted there, and returned to the BitBox when pressing the Accept button.

>**Warning!** Be sure that you have a valid microSD card backup and know your recovery password before enabling 2FA. [Click here to see how to check if you have a valid backup.]({%link bitbox01/basics/managing-backups.md %}#verifying-a-backup) Once enabled, the microSD slot, necessary for backups, and mobile app pairing is disabled. These are re-enabled only after resetting your BitBox01. To then restore your wallet you will need the **microSD card backup and your recovery password!**
