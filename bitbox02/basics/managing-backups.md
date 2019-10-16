---
layout: default
title: Managing backups
nav_order: 5
has_children: false
parent: Basic features
grand_parent: BitBox02
---

# {{page.grand_parent}}: {{page.title}}
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---
Please make sure you have the microSD card that contains your backup inserted into your BitBox02.
## Listing the backup files
In order to check which backup files are on your microSD card, click "Manage Backups"
![alt text]({% link assets/images/BitBox02_backups/backups1.png %})
You will then see a list of all backup files found on the currently inserted microSD card.

Normally that is just one file:
![alt text]({% link assets/images/BitBox02_backups/backups2.png %})
## Verifying a backup
In order to verify, that one of the backup files on the currently inserted microSD card is a backup of the wallet you are currently using on your BitBox02 (and not a backup of some other, older wallet which you might not be using anymore) click "Check Backup".

You should then see a pop-up like this:

![alt text]({% link assets/images/BitBox02_backups/backups3.png %})

That pop-up tells you that there is a backup for the currently used wallet, i.e. in this case there is a backup for the wallet called "Tutorial-2" which is the wallet I'm currently using.

You are then asked to confirm that the ID shown in the BitBoxApp matches the ID shown on your BitBox02.
If that is the case please confirm on your BitBox02 and then click "OK" in the BitBoxApp.

## Creating a new backup
If your backup was destroyed or you would just like to create another backup to store in a different location you can easily do that. All you need is a fresh microSD card which the new backup will be stored on.

### Plug in the new microSD card and click "Manage Backups"
![alt text]({% link assets/images/BitBox02_backups/backups1.png %})

### Click "Create Backup"
![alt text]({% link assets/images/BitBox02_backups/backups4.png %})

### Follow instructions on your BitBox02
Next you should see a pop-up telling you to follow the instructions on your BitBox02 screen.

![alt text]({% link assets/images/BitBox02_backups/backups5.png %})

<!--On your BitBox02 you will first need to confirm that you understand that **by default backup files are not password protected, i.e. if someone finds your backup they can steal your coins**.-->

Then you will be asked to input your device password to confirm the backup creation.

Once confirmed, you backup will be created and saved to the microSD card.

If you would like to manually check that there now is a backup file on the microSD card, please click "Back" once, then "Manage Backups" again and then [verify your backup.]({% link bitbox02/basics/managing-backups.md %}#verifying-a-backup)
