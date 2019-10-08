---
layout: default
title: Verify release
nav_order: 5
has_children: false
parent: BitBox App
---

# {{page.parent}}: {{page.title}}
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

In order to verify the downloaded BitBox App please do the following:

## Get benma's public key
<small>Info: Benma is the lead developer of the BitBox App.</small>

Run in your command line:

```
curl https://keybase.io/benma/pgp_keys.asc?fingerprint=2260e48288882c76afaa319d67a2b160f74db275 | gpg --import
```

## Download the BitBox App and .asc file
Download both from [Github](https://github.com/digitalbitbox/bitbox-wallet-app/releases)

**Do not install the BitBox App yet.**

If you have already downloaded the BitBox App from our website then just download the .asc file that corresponds to your operating system.

## Place BitBox App and .asc file in separate folder
Create a new folder and move both, the uninstalled/unzipped BitBox App file and the .asc file into that folder.

## Verify signatures
On your command line navigate into the newly created folder and run the following command:

`gpg --verify BitBox-4.13.1-macOS.zip.asc`

(Depending on when you do this update the command to use the corresponding .asc file you just dowloaded).

### You should then see the following:

```
gpg --verify BitBox-4.13.1-macOS.zip.asc
gpg: assuming signed data in 'BitBox-4.13.1-macOS.zip'
gpg: Signature made <DATE AND TIME>
gpg:                using RSA key 2D8876810AB092E451DCA894804538928C37EAE8
gpg: Good signature from "Marko Bencun <marko@shiftcrypto.ch>" [ultimate]
gpg:                 aka "Marko Bencun <mbencun+pgp@gmail.com>" [ultimate]

```
(The [ultimate] could say [unknown] or something else depending on your trust level.)
