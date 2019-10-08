---
layout: default
title: Managing backups
nav_order: 5
has_children: false
parent: Basic-features
grand_parent: BitBox01
---

# {{page.grand_parent}}: {{page.title}}
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---
Please make sure you have the microSD card with your backup inserted into your BitBox01.
## Listing the backup files
In order to check which backup files are on your microSD card, click "Manage Backups"
![alt text]({% link assets/images/BitBox01_random/bb01_device_settings1.png %})
You will then see a list of all backup files that are on the currently inserted microSD card.

Normally that is just one file.
![alt text]({% link assets/images/BitBox01_random/bb01_backup1.png %})

## Verifying a backup
In order to verify a backup select it, then click "Check Backup".

You will then be asked to input the recovery password for that wallet backup file.

![alt text]({% link assets/images/BitBox01_random/bb01_backup2.png %})
- **If the backup file + recovery password generates the same wallet as you are currently using on your BitBox01 it will say: "Backup matches the wallet."**

- **If you input a different recovery password a different wallet will be generated which therefore does not match the wallet you are currently using on your BitBox01 and the app will tell you: "Backup does NOT match the wallet."**

**Info:** There is no such thing as an incorrect recovery password. Your recovery password is combined with your wallet backup file and a wallet is generated from that. If you input a different recovery password (not the one you used when you generated your wallet) it will still generate a valid wallet, however that wallet won't contain your coins. You can think of the recovery password like a "passphrase". For more information [check this guide]({% link bitbox02/Advanced-features/passphrase.md %})


## Creating a new backup
If your backup was destroyed or you would just like to create another backup to store in a different location you can easily do that. All you need is a fresh microSD card which the new backup will be stored on.

### Plug in the new microSD card and click "Manage Backups"
![alt text]({% link assets/images/BitBox01_random/bb01_device_settings1.png %})

You should then see the following:
![alt text]({% link assets/images/BitBox01_random/bb01_no_backups.png %})

### Click "Create" and follow instructions in the App
Next you should see a pop-up asking you to give the wallet backup file a name and input the recovery password of your current wallet.

- If the recovery password **matches**, a new wallet backup file will be saved on the microSD card.

- If the recovery password **does not matches**, a new wallet backup file will still be saved on the microSD card (as the backup file is valid).
