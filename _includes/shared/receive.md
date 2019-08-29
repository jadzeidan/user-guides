
### Bitcoin 101:
{: .no_toc }
{% include glossary/bitcoin_address_reuse_warning.md %}


## Select coin and type

Use the menu on the left to choose the coin (and type) you would like to receive. To activate more coins and types check out this guide.(link to settings page)
![alt text]({{site.baseurl}}/assets/images/BitBox02_receive/receive1.png  )


---

## Click receive

Once you have selected the coin, click the "Receive" button in the upper right corner.
![alt text]({{site.baseurl}}/assets/images/BitBox02_receive/receive1b.png  )


{% if include.product == "BitBox02" %}
## Verify receive address

You will then see the first few characters of a receive address. In order to get the complete address you need to verify it on your {{include.product}} by clicking "Show and verify full address on device".

![alt text]({{site.baseurl}}/assets/images/BitBox02_receive/receive2.png  )

The address will then be shown on your {{include.product}} and the BitBox App at the same time.

Please compare the addresses and confirm on your {{include.product}} if they match.

![alt text]({{site.baseurl}}/assets/images/BitBox02_receive/receive3.png  )
{% endif %}


## Copy or scan address
Now you can scan the QR code of the receive address or copy the receive address by using the copy button on the right of the address.
{% if include.product == "BitBox02" %}
![alt text]({{site.baseurl}}/assets/images/BitBox02_receive/receive4.png  )
{% elsif include.product == "BitBox01" %}
![alt text]({{site.baseurl}}/assets/images/BitBox01_random/bb01_receive1.png  )
{% endif %}

## Receive
You can now use this address to send coins to your {{include.product}}. When you want to make another transaction to your {{include.product}} create a new receive address first, don't re-use addresses.
