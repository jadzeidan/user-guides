
## Download the BitBox App
In order to set up your {{include.product}} and create your first wallet you need to download the BitBox App for your computer.
Stay tuned for our mobile app! To be notified when it is available you can subscribe to our newsletter here.

[Download](https://shiftcrypto.ch/start/){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }


---

## Launch the BitBox app

Once the download is finished, please unpack the app (doube-click on it) and pull it into your application folder.

Then double-click it to launch it.

You should then see a screen that asks you to plug in your {{include.product}}.

![alt text]({{site.baseurl}}/assets/images/BitBoxApp/BitBox_App_waiting.png  "BitBox App")


---

## Insert microSD card & plug in your {{include.product}}
Before you plug in your {{include.product}}, please already **insert the microSD card** which will be needed in a later step.

{% if include.product == "BitBox02" %}
When done, please plug the {{include.product}} into your computer. Depending on the available ports you might need to use the USB-C to USB-A adapter that came with your {{include.product}}.
{% elsif include.product == "BitBox01" %}
When done, please plug the {{include.product}} into your computer.
{% endif %}
---

## Follow the in-App setup-wizard

Once the {{include.product}} is plugged in, the setup-wizard should start which will guide you through the process of setting up your {{include.product}}, creating and backing up your wallet.

{% if include.product == "BitBox02" %}

### Step 1: Choose display orientation
Most laptops have ports on both sides and as we cannot know from which side you will plug your {{include.product}} you will first need to select your display orientation.

To do that just touch the {{include.product}} on the side that is closer to you.

IMAGE

### Step 2: Confirm pairing code
All information that is exchanged between your computer and the {{include.product}} is encrypted. In order to make sure that there is no man-in-the-middle attack we need to ask you to confirm that the code on your screen and the code on your {{include.product}} are identical.

Please take the time to check all characters.
![alt text]({{site.baseurl}}/assets/images/BitBox02_wizard/step2.png  "BitBox App")

If both codes match, please confirm on your {{include.product}}, then click "Confirm & Continue" in the BitBox App.
### Step 3: Choose if you want to create a new wallet or restore an existing wallet

Now you are asked to choose if you want to create a new wallet or restores an existing wallet.

![alt text]({{site.baseurl}}/assets/images/BitBox02_wizard/step3.png  "BitBox App")

If this is the first time you create a wallet choose "Create Wallet".

If you already used a {{include.product}} before and you want to restore your wallet from your backup file choose "Restore Backup". (Link to restore wallet)

If you used a different hardware wallet before and you want to restore from the mnemonic seed phrase created by that other wallet, choose "Restore from BIP-39 mnemonic". (link to import bip39)

### Step 4: Create a wallet
First you need to give your wallet a name. This name can be anything, choose a name that you will recognise in the future when you might need to restore from your backup.

If you cannot click the "Name Device & Continue" button make sure that you have your microSD card plugged into the {{include.product}} correctly.
![alt text]({{site.baseurl}}/assets/images/BitBox02_wizard/step4b.png  "BitBox App")

Please then confirm the wallet name on your {{include.product}}.
![alt text]({{site.baseurl}}/assets/images/BitBox02_wizard/step4c.png  "BitBox App")

### Step 5: Set your {{include.product}} device password
Next you need to set a device password for your {{include.product}} which you will need to input every time you want to use your {{include.product}}. Please make sure that you remember this password and that it is not easy to guess.

The setup wizard will show you a video of how to use the touch buttons on your BitBox02 to set and input your password.
![alt text]({{site.baseurl}}/assets/images/BitBox02_wizard/step5.png  "BitBox App")

### Step 6: Create your wallet backup
After the device password is set, the {{include.product}} will create a backup of your wallet and safe it on the microSD card. To start that process click "Create Backup".

Your {{include.product}} will then ask you to confirm today's date as that is needed for the backup file.

> The backup file on your microSD card is not password protected, unless you use the advanced passphrase feature (link). That means should someone find your microSD card they can steal your funds. Therefore you should **make sure that you store it in a secure location.**

![alt text]({{site.baseurl}}/assets/images/BitBox02_wizard/step6.png  "BitBox App")

If you want, you can create multiple backups on multiple microSD cards. To do so follow this guide(link).

You can at any point check that you still have a valid wallet. To do so follow this guide (link).

{% elsif include.product == "BitBox01" %}
### Step 1: Choose if you want to create a new wallet or restore an existing wallet
Now you are asked to choose if you want to create a new wallet or restores an existing wallet.

If this is the first time you create a wallet choose "Create Wallet".

If you already used a {{include.product}} before and you want to restore your wallet from your backup file choose "Restore a wallet from a backup". (Link to restore wallet)
![alt text]({{site.baseurl}}/assets/images/BitBox01_setup/bb01_setup1.png  )

### Step 2: Understand the {{include.product}} passwords
The {{include.product}} makes use of two passwords:
* a **device password**, that you need whenever you want to use your {{include.product}}. This password can be changed later.
* a **recovery password** that protects your backup. This password can **NOT** be changed later.

**Important:** If you lose your {{include.product}} you will need your backup microSD card **AND** the recovery password in order to restore your wallet. **Just the backup microSD card is not enough.**

**Therefore please ensure that you keep your recovery password and backup microSD card safe.**
![alt text]({{site.baseurl}}/assets/images/BitBox01_setup/bb01_setup2.png  )

### Step 3: Start the setup process
Read the information and click "Continue"
![alt text]({{site.baseurl}}/assets/images/BitBox01_setup/bb01_setup3.png  )

### Step 4: Set device password
Now please set and confirm your device password. This password is needed whenever you want to use your {{include.product}}. It password can be changed later.

Click "Set device password"
![alt text]({{site.baseurl}}/assets/images/BitBox01_setup/bb01_setup4.png  )

### Step 5: Create wallet and microSD card backup
Next your wallet will be created. For that your microSD card needs to be plugged in, so that the backup file can be saved on it.

If your have not yet plugged in a microSD card, please do so now and click "Set recovery password now".
![alt text]({{site.baseurl}}/assets/images/BitBox01_setup/bb01_setup5.png  )

### Step 6: Set recovery password
In this step you will set the recovery password that protects your backup microSD card.

This password can **NOT** be changed later.

**Important:** If you lose your {{include.product}} you will need your backup microSD card **AND** the recovery password in order to restore your wallet. **Just the backup microSD card is not enough.**

Please also give your wallet a name that you can remember.
![alt text]({{site.baseurl}}/assets/images/BitBox01_setup/bb01_setup6.png  )

{% endif %}



### Step 7: Start stacking sats
Great! Your {{include.product}} is ready to use. Please make sure that you store your backup on your microSD card in a **secure location.**
{% if include.product == "BitBox02" %}
![alt text]({{site.baseurl}}/assets/images/BitBox02_wizard/step7.png  "BitBox App")
{% elsif include.product == "BitBox01" %}
![alt text]({{site.baseurl}}/assets/images/BitBox01_setup/bb01_setup7.png  )
{% endif %}
