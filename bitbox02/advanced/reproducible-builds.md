---
layout: default
title: Reproducible builds
parent: Advanced features
grand_parent: BitBox02
nav_order: 4
---
# {{page.grand_parent}}: {{page.title}}
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}
---

INFO: Site under construction

## Why reproducible builds?
Whilst anyone can inspect the source code of open source software for malicious flaws how can you be certain that the binary built from that public source code is actually on your device?

Reproducible builds, also known as deterministic compilation, is a process of compiling firmware in a way that is reproducible, i.e. results in the exact same binary. By comparing the checksum of the produced binary multiple third parties come to a consensus on a “correct” result and then sign the resulting hash with their GPG key. They thereby assert that the binary they built is identical to the one we built.

## What you can do
For both levels:
-  `git clone https://github.com/digitalbitbox/bitbox02-firmware.git`
- Requirement: GPG

### Level 1: Verify the community assertions
This is less technically involved as you just need GPG. By verifying the community assertions you check that other people independently built the binary and that they confirmed they came to the same result as we did.

To check the community assertions on the command line:
1. Switch to the downloaded `/bitbox02-firmware` folder and go into the `/releases` folder.
2. Go into the release folder you want to verify depending on the firmware version.
- In that folder you find one `assertion.txt` and multiple `assertion-YOURNAME.txt` files.
3. To verify each assertion do: `gpg --verify assertion-YOURNAME.sig assertion.txt`
- If the check was successful it should say "Good signature". (Depending on your trust level you could get a warning that you have not trusted that public key. )

### Level 2: Contribute your own signature
1. In `releases/` run `./build.sh <version tag> <make command>`, e.g. `./build.sh firmware-btc-only/v4.1.0 "make firmware-btc"`.
2. Wait, this could take a few minutes.
3. Then print the checksum:
- On Linux: `sha256sum temp/build/bin/firmware.bin` or `sha256sum temp/build/bin/firmware-btc.bin`
- On Mac: `shasum -a 256 temp/build/bin/firmware.bin` or `shasum -a 256 temp/build/bin/firmware-btc.bin`
4. Open `assertion.txt` of the firmware you just built and compare the checksum you got in step 3 to the checksum specified in `assertion.txt`.
5. If they match sign `assertion.txt` by running: `gpg -o assertion-YOURNAME.sig --detach-sign assertion.txt`
6. Add your GPG pubkey to the `./pubkeys` folder by running: `gpg --export --armor YOUR_PGP_KEY_ID  > ./pubkeys/YOURNAME.asc`.
7. Open a pull request to add your signature to the public repository.
