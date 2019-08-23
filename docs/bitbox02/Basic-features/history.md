---
layout: default
title: Transaction history
nav_order: 3
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

## Transaction types
There are four different types of transactions that can show up in your transaction history.

### Pending incoming transaction
An incoming transaction will at first be pending. That means it is not confirmed in the Bitcoin blockchain yet. You can see that the transaction in the screenshot is pending in two spots.

1. It says "Pending transaction" on the right of the green "In" symbol
2. Below the wallet balance, which is still zero as only confirmed transactions are counted, it says "Incoming +0.002 BTC"

![alt text]({{site.baseurl}}/assets/images/BitBox_history/pending_incoming.png  "BitBox02 box")


### Confirmed incoming transaction
Once a formerly pending transaction has the first confirmation (i.e. it was included in a block) it is shown as a confirmed transaction and the transaction amount is added to your wallet balance.
![alt text]({{site.baseurl}}/assets/images/BitBox_history/confirmed_incoming.png  "BitBox02 box")


### Unconfirmed outgoing transaction
An outgoing transaction will at first be pending. That means it is not confirmed in the Bitcoin blockchain yet. You can see that the transaction in the screenshot is pending in two spots.

1. It says "Pending transaction" on the right of the green "In" symbol
2. Below the wallet balance, which is still zero as only confirmed transactions are counted, it says "Outgoing +0.002 BTC"

IMAGE


### Confirmed outgoing transaction
Once a formerly pending transaction has the first confirmation (i.e. it was included in a block) it is shown as a confirmed transaction and the transaction amount is deducted from your wallet balance.

IMAGE

## Transaction details
If you want to see further details about a transaction you can click on the downward arrow on the left of the green/red transaction type.

Clicking that will drop down and show you the following transaction details:
* Number of confirmations
* Virtual transaction size
* Transaction size
* Transaction weight
* Transaction ID with link to block explorer

![alt text]({{site.baseurl}}/assets/images/BitBox_history/transaction_details.png  "BitBox02 box")
