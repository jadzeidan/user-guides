---
layout: default
title: BitBox01 - Backup center
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
## To recover real funds:
A standalone version of this page can be downloaded from <a href="https://github.com/digitalbitbox/html_backup">Github</a> and run offline. See the README on Github for instructions.

> **If you want to recover real funds, please download the page from Github and run offline!**


## For educational purposes (i.e. no real funds on backup)
Learn how to recover from a backup or create your own wallet using the client-side JavaScript below.

(compatible with firmware versions 2.0+)

{% include backup.html %}

## Instructions
* To <b>recover your Bitcoin wallet without a Digital Bitbox</b>,
enter the wallet backup text and password in the above boxes, click 'generate',
and import the recovery key into the Electrum software wallet.
* To <b>recover Ethereum without a Digital Bitbox</b>,
enter the wallet backup text and password in the above boxes, click 'generate',
and enter an Ethereum private key into MyEtherWallet.
The order of private keys corresponds to the order of public addresses when 'viewing' a wallet in MyEtherWallet.
* The backup is saved as a PDF file on the micro SD card for convenience.
Plug the micro SD card into a trusted printer if you wish to also make a <b>paper backup</b>.
* To <b>load your own wallet</b> into a Digital Bitbox, put the PDF file
on the micro SD card inside a folder named 'digitalbitbox' in the root directory.
Then, insert the SD card into the Digital Bitbox, and load your wallet using the desktop app.
<b>High quality randomness is crucial!</b>
Otherwise, a thief may be able to guess your key and take your coins.

## Derivation
* A wallet is generated from the backup text and password using a modified BIP39 procedure.
In particular, PBKDF2 strengthening is done twice (22,528 total rounds) for stronger protection.
* Standard wallet addresses are generated following the BIP32 and BIP44 specifications.
The BIP32 extended master private key is m.
* Electrum recovery keys are generated with m/44'/0'/0'.
* For a multi-signature wallet, the base BIP32 key path is m/100'/45'/0'.
* For Ethereum, the base BIP32 key path is m/44'/60'/0'/0</i>. The tool generates Ethereum keys m/44'/60'/0'/0/0 through m/44'/60'/0'/0/19.
