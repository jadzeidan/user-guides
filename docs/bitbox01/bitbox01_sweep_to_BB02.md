---
layout: default
title: Sweep funds from BitBox01 to BitBox02
nav_order: 3
has_children: false
parent: BitBox01
---
# {{page.title}}
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---
This guide demonstrates how to sweep all funds from a BitBox02 onto a newly created wallet on a BitBox02 from both standard and hidden wallets. The basic procedure is:
1. Setup your BitBox02
2. Send coins from BitBox01 to BitBox02
3. Use BitBox02
* Optional: Ethereum sweep (wait for feedback)


## Setup your BitBox02
If you have not yet set up your BitBox02, please follow [this guide]({{site.baseurl}}/docs/bitbox02/Getting-started/setup/) to do so.


### Did you use the hidden wallet option on the BitBox01 (aka. Digital BitBox) and you want to continue using it?

**If no:** [Click here to continue]({{site.baseurl}}/docs/bitbox01/bitbox01_sweep_to_BB02/#send-coins-from-bitbox01-to-bitbox02-no-hidden-wallet)

**If yes:**

>**DANGER:** If you forget/lose this passphrase you will forever lose access to the coins stored in that hidden wallet. Proceed with caution.
1. Generate a new passphrase for the hidden wallet to use on your BitBox02 (or re-use the old "hidden-wallet" password if you are sure it is secure) and make sure to back this passphrase up (important!!)
2. Connect your BitBox02, unlock it, go to "Manage Device" in the BitBox App and select "Enable Mnemonic Passphrase".
3. Confirm on your BitBox02 that you want to use a passphrase.
4. [Click here to continue]({{site.baseurl}}/docs/bitbox01/bitbox01_sweep_to_BB02/#send-coins-from-bitbox01-to-bitbox02-with-hidden-wallet)

## Send coins from BitBox01 to BitBox02 (no hidden wallet)
Your BitBox02 should still be plugged in and unlocked.
1. Verify and copy a receive address for each coin you want to sweep (i.e. Bitcoin, Litecoin) and paste it into a text file. Make sure you carefully check that it has been copied correctly.

>The receive address is where your will send your funds to from the BitBox01 to the BitBox02. Note that for Bitcoin, you may have had different style bitcoin addresses in your old wallet that each held funds. These funds can all be sent to the same (default) style receive address you just copied and stored.

2. Once you have the receive addresses ready you can unplug your BitBox02.
3. Then plug in your BitBox01 and unlock it with your BitBox01 device password as usual.
4. Select a currency (e.g. Bitcoin) and click "Send".
5. Paste the respective receive address from your text file into the address field, choose a low test amount (e.g. 2 USD) and select a low fee.
6. Confirm and send your transaction.
7. Reapeat steps 4-6 for all currency and types (e.g. Bitcoin has multiple address types, you can select all of them in the BitBox App settings) that you want to sweep form your BitBox01 to BitBox02.
8. Remember how many test transactions you made.
9. Unplug your BitBox01, plug in your BitBox02, unlock it with your BitBox02 device password.
10. Check that all test transactions arrived on your BitBox02 (you might need to enable more coins/types in the BitBox App settings).

**If that is the case:**

Repeat steps 3-10 with real amounts. You can split it up into multiple transactions if you feel uncomfortable sending all in one transaction. Please confirm that it was received on the BitBox02 after each transaction.

If you can't see all your test transactions after a few minutes:

Contact support: [support@shiftcrypto.ch](mailto:support@shiftcrypto.ch)


## Send coins from BitBox01 to BitBox02 (with hidden wallet)
Confirm: You used one or more hidden-wallets on your BitBox01 and you want to continue doing that by using additional passphrases on your BitBox02
If you didn't use the hidden wallet feature on the BitBox01: Go to <a href="#step2a">Step 2a</a> instead.
If you used the hidden-wallet feature and you want to continue using it on your BitBox02:
Continue below
If you used the hidden-wallet feature but you don't want to continue using it on your BitBox02:
Go to <a href="#step2a">Step 2a</a> instead and repeat it once to sweep the standard wallet from your BitBox01 and then again to sweep the hidden-wallet from your BitBox01

Your BitBox02 should still be plugged in and unlocked.
"Mnemonic Passphrase" should be enabled. To check go to the BitBox App settings. It should say "Disable Mnemonic Passphrase". (Don't click!)
Now we need to do two wallet sweeps. The first for the standard wallet, the second for the hidden wallet.

### Standard wallet sweep:
1. Verify and copy a receive address for each coin you want to sweep (i.e. Bitcoin, Litecoin) and paste it into a text file, note down that this address is from the standard wallet. Make sure you carefully check that it has been copied correctly.

> The receive address is where your will send your funds to from the BitBox01 to the BitBox02. Note that for Bitcoin, you may have had different style bitcoin addresses in your old wallet that each held funds. These funds can all be sent to the same (default) style receive address you just copied and stored.

2. Once you have the receive addresses ready you can unplug your BitBox02.
3. Then plug in your BitBox01 and unlock it with your BitBox01 device password as usual.</p>
4. Select a currency (e.g. Bitcoin) and click "Send".
5. Paste the respective receive address from your text file into the address field, choose a low test amount (e.g. 2 USD) and select a low fee.
6. Confirm and send your transaction.
7. Repeat steps 4-6 for all currency and types (e.g. Bitcoin has multiple address types, you can select all of them in the BitBox App settings) that you want to sweep form your BitBox01 to BitBox02.
8. Remember how many test transactions you made.
9. Unplug your BitBox01, plug in your BitBox02, unlock it with your BitBox02 device password.
10. Check that all test transactions arrived on your BitBox02 (you might need to enable more coins/types in the BitBox App settings).

**If that is the case:**

Repeat steps 3-10 with real amounts. You can split it up into multiple transactions if you feel uncomfortable sending all in one transaction. Please confirm that it was received on the BitBox02 after each transaction.

If you can't see all your test transactions after a few minutes:

Contact support: [support@shiftcrypto.ch](mailto:support@shiftcrypto.ch)


### Hidden-wallet sweep:
          <p>2b.1. Unplug your BitBox02, plug it in again, type in your BitBox02 device password.</p>
          <p>2b.2. Then type in your passphrase for your hidden wallet which you generated in step 1.1. <strong>Attention:</strong> If you forget/lose this password you will lose access to the coins in this wallet. Make sure to backup the passphrase properly.</p>
          <p>2b.3. Verify and copy a receive address for each coin you want to sweep (i.e. Bitcoin, Litecoin) and paste it into a text file, note down that this address is from the hidden wallet. Make sure you carefully check that it has been copied correctly.</p>
          <p>The receive address is where your will send your funds to from the BitBox01 to the BitBox02. Note that for Bitcoin, you may have had different style bitcoin addresses in your old wallet that each held funds. These funds can all be sent to the same (default) style receive address you just copied and stored.</p>
          <p>2b.4. Once you have the receive addresses ready you can unplug your BitBox02.</p>
          <p>2b.5. Then plug in your BitBox01 and unlock it with your BitBox01 device password as usual.</p>
          <p>2b.6. Select a currency (e.g. Bitcoin) and click "Send".</p>
          <p>2b.7. Paste the respective receive address from your text file into the address field, choose a low test amount (e.g. 2 USD) and select a low fee.</p>
          <p>2b.8. Confirm and send your transaction.</p>
          <p>2b.9. Reapeat steps 4-6 for all currency and types (e.g. Bitcoin has multiple address types, you can select all of them in the BitBox App settings) that you want to sweep form your BitBox01 to BitBox02.</p>
          <p>2b.10. Remember how many test transactions you made.</p>
          <p>2b.11. Unplug your BitBox01, plug in your BitBox02, unlock it with your BitBox02 device password.</p>
          <p>2b.12. Check that all test transactions arrived on your BitBox02 (you might need to enable more coins/types in the BitBox App settings).</p>
          <p><strong>If that is the case:</strong></p>
          <ul>
            <li style="text-align:left">Repeat steps 3-10 with real amounts. You can split it up into multiple transactions if you feel uncomfortable sending all in one transaction. Please confirm that it was received on the BitBox02 after each transaction.</li>
          </ul>
          <p><strong>If you can't see all your test transactions after a few minutes: </strong></p>
          <ul>
            <li style="text-align:left">Contact support: <a href="mailto:support@shiftcrypto.ch">support@shiftcrypto.ch</a></li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="leftup leftdown with-space gray-gradient" id="step4">
  <div class="content-width">
    <div class="row center-xs">
      <div class="col-xs-11 col-sm-9 col-md-7">
        <h1 class="title"><span class="gray m-right">4.</span>Use your BitBox02</h1>
        <div class="m-top-xlarge">
          <p>After you have moved all your funds to your new BitBox02 you are good to go. Have fun and always stay safe. Kind regards, Shift Cryptosecurity Team</p>
        </div>
      </div>
    </div>
  </div>
</section>
