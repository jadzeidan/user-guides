---
layout: default
title: Backup center (BitBox01 aka. Digital BitBox)
nav_order: 2
has_children: false
parent: BitBox01
---
# {{page.title}}
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

**Caution:** This page is not required to use your Bitbox01 and is provided for instructional purposes.
## To recover real funds
A standalone version of this page can be downloaded from <a href="https://github.com/digitalbitbox/html_backup">Github</a> and run offline. See the README on Github for instructions.

> **If you want to recover real funds, please download the page from Github and run offline!**


## For educational purposes (i.e. no real funds on backup)
Learn how to recover from a backup or create your own wallet using the client-side JavaScript below.

(compatible with firmware versions 2.0+)

{% include backup.html %}

## Instructions
* To recover your Bitcoin wallet without a BitBox01, enter the wallet backup text and password in the above boxes, click 'generate' and import the recovery key into the Electrum software wallet.
* To recover Ethereum without a BitBox01, enter the wallet backup text and password in the above boxes, click 'generate' and enter an Ethereum private key into MyEtherWallet.
The order of private keys corresponds to the order of public addresses when 'viewing' a wallet in MyEtherWallet.
* To load your own wallet into a BitBox01, put the PDF file
on the micro SD card inside a folder named 'digitalbitbox' in the root directory.
Then, insert the SD card into the BitBox01, and load your wallet using the desktop app.
**High quality randomness is crucial!**
Otherwise, a thief may be able to guess your key and take your coins.

## Derivation
### Information
* A wallet is generated from the backup text and password using a modified BIP39 procedure.
In particular, PBKDF2 strengthening is done twice (22,528 total rounds) for stronger protection.
* Standard wallet addresses are generated following the BIP32 and BIP44 specifications.
* The BIP32 extended master private key is m.
* BIP 44 specifies the following standard:
    * m / purpose' / coin_type' / account' / change / address_index

### Purpose field
* Purpose is set as follows:
    * Legcay (P2SH) = 44'
    * Segwit (P2PSH) = 49'
    *  Native Segwit (P2WPKH) = 84'

### Coin_type field
* Coin_type is set in accordance to [SLIP-44](https://github.com/satoshilabs/slips/blob/master/slip-0044.md):
    * Bitcoin = 0
    * Bitcoin Tesnets = 1
    * Litecoin = 2
    * Ethereum = 60

### Account field
* BitBox App currently only supports a single account, therefore wallets created via the BitBox App will use 0 for the account field.
* Wallets created via Electrum can have a different account field number.

### Change field
* 0 for normal receive addresses
* 1 for internally generated change addresses

### Address field
* Addresses are numbered from index 0 in sequentially increasing manner.

## Other schemes / Information
* Electrum recovery keys are generated with m/44'/0'/0'.
* For a multi-signature wallet, the base BIP32 key path is m/100'/45'/0'.
* The tool generates Ethereum keys m/44'/60'/0'/0/0 through m/44'/60'/0'/0/19.
<!--
| master private key | purpose'  | coin' | account' | change | address |
|:-------------------|:----------|:------|:---------|:-------|:--------|
| m                  |  44'      | 0     | 0        | 0      | 0       |-->
