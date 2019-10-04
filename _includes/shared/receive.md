
### Bitcoin 101:
{: .no_toc }
{% include glossary/bitcoin_address_reuse_warning.md %}


## Select coin and type

Use the menu on the left to choose the coin (and type) you would like to receive. To activate more coins and types check out [this guide.]({% link bitbox_app/settings.md %}#bitbox-app-settings)


---

## Click receive

Once you have selected the coin, click the "Receive" button in the upper right corner.
![alt text]({% link assets/images/BitBox02_receive/receive1b.png %})


{% if include.product == "BitBox02" %}
## Verify receive address

You will then see the first few characters of a receive address. In order to get the complete address you need to verify it on your {{include.product}} by clicking "Show and verify full address on device".

![alt text]({% link assets/images/BitBox02_receive/receive2.png %})

The address will then be shown on your {{include.product}} and the BitBox App at the same time.
{% endif %}

## Copy or scan address
You can then scan the QR-code or copy the address.

{% if include.product == "BitBox02" %}
Please confirm that the address you scanned with your other wallet and the address shown on your BitBox02 match.

 **Rule:** Always trust your hardware wallet, not the wallet app.
![alt text]({% link assets/images/BitBox02_receive/receive3.png %})
{% elsif include.product == "BitBox01" %}
![alt text]({% link assets/images/BitBox01_random/bb01_receive1.png %})
{% endif %}

## Receive
You can now use this address to send coins to your {{include.product}}. When you want to make another transaction to your {{include.product}} create a new receive address first, don't re-use addresses.
