{% if include.product == "BitBox02" %}

## Watch send tutorial video or continue reading
{: .no_toc }

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src='https://www.youtube.com/embed//HrwQ6hGpMyo' frameborder='0' allowfullscreen></iframe></div>
{% endif %}
## Click the send button
![alt text]({% link assets/images/BitBox02_send/send1.png %})

## Paste in the address you want to send to
Or click the QR-code symbol to use your device camera to scan a QR-code.
![alt text]({% link assets/images/BitBox02_send/send3.png %})

## Enter the amount you want to send
You can either type in the amount in cryptocurrency or in fiat.
![alt text]({% link assets/images/BitBox02_send/send4.png %})

## Choose the fee
The higher the fee, the quicker your transaction will be confirmed in the blockchain. A low fee should be sufficient in most cases.
![alt text]({% link assets/images/BitBox02_send/send5.png %})

## Click "Sign and Send"
![alt text]({% link assets/images/BitBox02_send/send6.png %})

{% if include.product == "BitBox02" %}
## Verify the transaction details on your {{include.product}}
It is crucial that you make sure the transaction details are correct. **There is no reverse button in Bitcoin.**

Please double check all transaction details on your {{include.product}}.

**Trust your {{include.product}}, not your potentially malware infected computer.**

If what you see on your  {{include.product}} is correct, then confirm the transaction on your  {{include.product}}.
![alt text]({% link assets/images/BitBox02_send/send7.png %})

If you confirmed the transaction on your  {{include.product}} you should see this screen shortly after:
![alt text]({% link assets/images/BitBox02_send/send8.png  %})

{% elsif include.product == "BitBox01" %}
## Confirm the transaction on your {{include.product}}
**Attention:** We recommend that you use our Smartphone app as a second-factor authenticator for your transactions, so that you can verify the transaction details on a second display.

Please confirm or deny the transaction on your {{include.product}} as explained in the pop-up.
![alt text]({% link assets/images/BitBox01_random/bb01_send1.png %})
{% endif %}
