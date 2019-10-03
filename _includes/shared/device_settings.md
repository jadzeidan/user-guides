{% if include.product == "BitBox02" %}
![alt text]({{site.baseurl}}/assets/images/BitBox02_device/device_settings1.png )
{% elsif include.product == "BitBox01" %}
![alt text]({{site.baseurl}}/assets/images/BitBox01_random/bb01_device_settings1.png )
{% endif %}

## Secrets section
At the top of the device settings you can find the "secrets" section. This section is all about making sure your funds are secure.

It let's you:
{% if include.product == "BitBox02" %}
* [manage and verify your backups.]({{site.baseurl}}/bitbox02/Basic-features/managing_backups/ ).
* [view your BIP39 seed to back it up on paper or metal.]({{site.baseurl}}/bitbox02/Advanced-features/view_bip39//)
* [reset your {{include.product}}.]({{site.baseurl}}/bitbox02/Advanced-features/reset/)
{% elsif include.product == "BitBox01" %}
* [manage and verify your backups.]({{site.baseurl}}/404).
* [change your device password]({{site.baseurl}}/404)
* [create a hidden wallet]({{site.baseurl}}/404)
* [reset your {{include.product}}.]({{site.baseurl}}/404)

## Pairing section
The pairing section let's you pair your {{include.product}} with your smartphone via our mobile app. That allows you to require a second factor for your transactions and let's you verify the generated receive address on your Smartphone.

To set up Two-Factor-Authentication follow this guide (coming soon)

{% endif %}


## Firmware section
The firmware section shows you which firmware version you are running on your {{include.product}} and if you're up to date. Rest assured, we will notify you in the app, on twitter, via our blog and our email newsletter when a new update becomes available.

## Hardware section
{% if include.product == "BitBox02" %}
This section let's you change your wallet name and use the built in true-random-number-generator (TRNG) to generate a 256-bit random number.
{% elsif include.product == "BitBox01" %}
This section let's you use the built in true-random-number-generator (TRNG) to generate a 256-bit random number and test that the LED works by clicking "Blink".
{% endif %}


{% if include.product == "BitBox02" %}
## Expert section
The "expert" section allows you to enable the passphrase option. To learn more about that follow [this guide.]({{site.baseurl}}/bitbox02/Advanced-features/passphrase/)
{% endif %}