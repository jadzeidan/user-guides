json = {
  "guide": {
    "accountDescription": {
      "text": "This is your account overview. It shows incoming and outgoing transactions. The balance is displayed for each account separately. Consult the guide in settings to learn more about the different account types.",
      "title": "What is displayed here?"
    },
    "accountFiat": {
      "text": "Yes, you can click on any ticker to rotate through several fiat currencies. You can also change the list of currencies in the settings.",
      "title": "Can I display other conversion rates?"
    },
    "accountIncomingBalance": {
      "text": "Incoming sums up the amounts that are being transferred to you but have not yet been confirmed by the network.",
      "title": "What does incoming mean?"
    },
    "accountInfo": {
      "xpub": {
        "text": "An extended public key is a root key from which all receiving addresses of an account are derived.\nIt is provided here for advanced use and interoperability with watch-only wallets, such as Electrum or Sentinel.",
        "title": "What is an extended public key?"
      }
    },
    "accountLegacyConvert": {
      "text": "Go to the Bitcoin account, select receive and copy the address. Go back to your legacy account, click send, paste the copied address and tick send all. Then sign and send to move all your coins in a single transaction.",
      "title": "How can I move my coins out of the Legacy account?"
    },
    "accountRates": {
      "link": {
        "text": "www.cryptocompare.com",
        "url": "https://www.cryptocompare.com"
      },
      "text": "The exchange rates are updated every minute from CryptoCompare.",
      "title": "Which rates are used?"
    },
    "accountReload": {
      "text": "All transaction information is updated automatically.",
      "title": "How can I reload the transaction history?"
    },
    "accountSendDisabled": {
      "text": "The ‘Send’ button is activated when your balance is more than zero.",
      "title": "Why can't I send any {{unit}}?"
    },
    "accountTransactionAttributesBTC": {
      "text": "Virtual size: Used to determine network fee. You have successfully saved on fees if it is smaller than the size of the transaction.\nSize: Actual transaction size in bytes when serialized according to the underlying blockchain.\nWeight: Introduced with Segwit, it is a new metric to evaluate transaction and block sizes. Each segregated witness byte counts as one, everything else as four weight units. Instead of one megabyte in actual size, the block size limit is now four million weight units.",
      "title": "Bitcoin-related transaction details"
    },
    "accountTransactionAttributesGeneric": {
      "text": "Confirmations: When your transaction is first broadcast it will be unconfirmed. You will need to wait for it to be included in to a block by a miner, after which it will have 1 confirmation. Each block broadcast on the network thereafter will add another confirmation to your transaction. Generally merchants and other network actors will only accept transactions with between 3-6 confirmations before considering the transaction as settled. \nTransaction ID: A unique identification number that can be used to lookup a transaction in a block explorer.\nFee: Miners are paid a transaction fee as an incentive to include transactions in the blocks they mine. To learn more, click on the send button.",
      "title": "What is the information shown in the transaction details?"
    },
    "accountTransactionConfirmation": {
      "text": "This is a transaction that has been broadcasted to the network and is waiting to be confirmed.",
      "title": "What is a pending transaction?"
    },
    "accountTransactionLabel": {
      "text": "It is the address where you received the coins or sent the coins to. An address encodes how (and thus by whom) the coins can be spent.",
      "title": "Which address is displayed for each transaction?"
    },
    "accountTransactionTime": {
      "text": "The time the transaction has been confirmed on the blockchain.",
      "title": "What time is displayed?"
    },
    "appendix": {
      "href": "https://shiftcrypto.ch/contact",
      "link": "Contact us!",
      "text": "Another question?"
    },
    "backups": {
      "check": {
        "text": "'Check Backup' allows you to verify that you have a working backup corresponding to your current wallet. It can also be used to verify that you still have the correct recovery password. You can check your main recovery password or your hidden recovery password.",
        "title": "What is 'Check Backup'?"
      },
      "encrypt": {
        "text": "No but your recovery password is required to derive the wallet from the stored seed.",
        "title": "Can I encrypt the backup?"
      },
      "howOften": {
        "text": "The backup is automatically generated when a new wallet is created. You only have to make a new backup if your micro SD card is lost or damaged, or if you want to use multiple micro SD cards as backups.\nYou do not need to create new backups after transaction activity. All your transaction data can be recreated by your single backup that was automatically generated for you.",
        "title": "How often do I have to make a backup?"
      },
      "whatIsABackup": {
        "text": "It is a copy of the seed on an micro SD card. The seed together with your recovery password generates your wallet.",
        "title": "What is a backup?"
      }
    },
    "backupsBB02": {
      "check": {
        "text": "'Check Backup' allows you to verify that you have a working backup corresponding to your current wallet.",
        "title": "What is 'Check Backup'?"
      },
      "encrypt": {
        "text": "No. Please keep the micro SD card safe, as it contains the unencrypted seed to recover your wallet.",
        "title": "Can I encrypt the backup?"
      },
      "whatIsABackup": {
        "text": "It is a copy of the seed on an micro SD card.",
        "title": "What is a backup?"
      }
    },
    "bitbox": {
      "2FA": {
        "text": "When 2FA is enabled, all transactions have to be approved on the paired mobile phone in order to spend coins. Under the hood, an encrypted single-use number is sent to the mobile app, decrypted there, and returned to the BitBox when pressing the Accept button. This communication with the device is done via the channel between the mobile phone and this desktop app established during pairing.\n\nBe sure to backup your wallet and pair the mobile app before enabling 2FA. Once enabled, the micro SD slot and mobile app pairing are disabled. They can be re-enabled by resetting the BitBox, which erases the device.",
        "title": "How does Two Factor Authorization (2FA) work?"
      },
      "disable2FA": {
        "text": "In order to disable 2FA, you need to reset your BitBox and then restore the wallet from its backup. Make sure that you still have the micro SD card with the backup and that you still remember the recovery password. Then press 'Reset Device'. Set a new device password and choose 'Or Restore a Backup'. Select the backup you have made from the wallet, click 'Restore' and enter the recovery password you used when creating the wallet.",
        "title": "How can I disable Two Factor Authorization (2FA)?"
      },
      "ejectBitbox": {
        "text": "You can unplug the BitBox at any time without having to eject it first.",
        "title": "How can I eject the BitBox?"
      },
      "ejectSD": {
        "text": "You can remove the micro SD card from the BitBox at any time as long as you are not in the process of creating or restoring a backup.",
        "title": "How can I eject the micro SD card?"
      },
      "hiddenWallet": {
        "text": "It is a second wallet on the same device protected by a different device password and recovery password, which you can use for plausible deniability. The same backup seed is used for both your normal and hidden wallet, so no additional backup is required.",
        "title": "What is a hidden wallet?"
      },
      "legacyHiddenWallet": {
        "text": "First click the button below (available if the BitBox is unlocked with the main device password and 2FA is disabled), then replug your Bitbox and unlock it with your hidden device password.",
        "title": "How do I access the legacy hidden wallet?"
      },
      "pairing": {
        "text": "After having downloaded our mobile app for either iOS or Android, you scan the displayed QR code, which sets up a secure channel between the mobile app and this application. Once scanned, follow the instructions in the mobile app.",
        "title": "How to securely pair with your phone"
      }
    },
    "receive": {
      "address": {
        "text": "Give it to others to send you some coins.\n(Try to independently verify the address, for example with a phone call.)",
        "title": "What do I do with an address?"
      },
      "addressChange": {
        "text": "As soon as an address is used in a transaction a new address is added to the list to replace it. There will always be 20 unused addresses available in the list.",
        "title": "When do the addresses change?"
      },
      "howVerify": {
        "text": "Click on the BitBox icon in the sidebar on the left and see the Pairing section. The guide will update and you can continue following the instructions from there.",
        "title": "How can I verify an address securely?"
      },
      "whyMany": {
        "text": "For privacy and security reasons, you should never hand out the same address twice. Click on 'Next' to get a new address for a different purpose. You can generate up to 20 addresses at a time. All addresses are derived from your single backup seed. (Think of addresses like invoice numbers.)",
        "title": "Why are there many addresses?"
      },
      "whyVerify": {
        "text": "One of the reasons for buying a hardware wallet like the BitBox is that you should not trust your computer due to its big attack surface. Consequently, you should not trust your computer to generate and display authentic addresses. The button to verify the address securely makes the BitBox send the address to a paired mobile phone, from which you can also scan and verify the QR code.",
        "title": "Why should I verify the address securely?"
      }
    },
    "send": {
      "fee": {
        "text": "The fee is based on the transaction data size and not its amount. The fee targets are calculated by Bitcoin Core's fee estimation algorithm for each network priority you chose. They are shown if they have a different value from the target below.\nEconomy: 24 blocks (around 4 hours for Bitcoin, 1 hour for Litecoin)\nLow: 12 blocks (around 2 hours for Bitcoin, 30 minutes for Litecoin)\nNormal: 6 blocks (around 1 hour for Bitcoin, 15 minutes for Litecoin)\nHigh: 2 blocks (around 20 minutes for Bitcoin, 5 minutes for Litecoin)\n(A block takes on average ten minutes for Bitcoin (2.5 minutes in Litecoin) to mine and the network load may vary considerably in the above periods.)",
        "title": "How is the fee determined?"
      },
      "priority": {
        "text": "The higher fee you are willing to pay, the faster your transaction is typically confirmed by the network.",
        "title": "What is the network priority?"
      },
      "revert": {
        "text": "Once a transaction is signed and sent (i.e. broadcasted to the network), it can no longer be reverted. Verify the transactions (including the fee) properly before signing!\nIf you know the recipient and he or she is willing to send the same amount (minus the transaction fees) back to you, you can send them a new receiving address.",
        "title": "Can I revert a transaction?"
      },
      "whyFee": {
        "text": "Transactions are competing to be confirmed by a miner. Miners choose transactions to be included in the blockchain based on their fee.\nMiners vote on the history of transactions. Since there is no trusted third party to enforce one vote per person (which is the whole point of blockchains), miners vote on transactions by sacrificing a costly resource like computing power. As a reward for their work, they can claim newly created coins and the fee of all the transactions they included.",
        "title": "Why is there a network fee?"
      }
    },
    "settings-electrum": {
      "what": {
        "text": "It is possible to power your wallet with your own full nodes instead of using Shift servers.",
        "title": "What is this?"
      }
    },
    "settings": {
      "btc-p2pkh": {
        "text": "This uses an old transaction format, which has been superseded by the Segwit address and transaction formats. If you used the BitBox with the old desktop app before, this is the account containing your coins currently. To save fees in the future transfer them to the Bitcoin account with a transaction to an address in the Bitcoin or Bitcoin bech32 account.",
        "title": "What is Bitcoin Legacy?"
      },
      "btc-p2sh": {
        "link": {
          "text": "Segregated Witness Benefits",
          "url": "https://bitcoincore.org/en/2016/01/26/segwit-benefits/"
        },
        "text": "This is a backwards compatible segwit account (p2sh-p2wpkh). It uses a new transaction format that saves you network fees. The address format is similar to legacy, and as such can be used with all existing Bitcoin wallets/exchanges/services.",
        "title": "What is the Bitcoin account?"
      },
      "btc-p2wpkh": {
        "link": {
          "text": "Bech32 adoption",
          "url": "https://en.bitcoin.it/wiki/Bech32_adoption"
        },
        "text": "To reap the full benefits of segwit's cheaper network fees, Bitcoin bech32 should be used. It uses a new address format called bech32, but this format is not accepted everywhere yet.",
        "title": "What is Bitcoin bech32?"
      },
      "moreCoins": {
        "text": "We will be integrating more altcoins besides Litecoin in the next few releases. If you are looking for a specific coin, leave us a suggestion at the contact below.",
        "title": "Can you add more coins?"
      },
      "servers": {
        "text": "This app communicates with servers of Shift Cryptosecurity to check for updates, load transactions, and send information to paired mobile apps.\nAdditionally, it retrieves the latest exchange rates from CryptoCompare. (The conversions are calculated locally, no amounts of yours are transmitted.)",
        "title": "Which servers does this app talk to?"
      },
      "whyMultipleAccounts": {
        "text": "Some cryptocurrencies have multiple address and transaction formats. These addresses are separated into extra accounts.",
        "title": "Why are there multiple accounts for the same coin?"
      }
    },
    "title": "Guide",
    "unlock": {
      "forgotDevicePassword": {
        "text": "You have to reset the device and restore the wallet from a backup, using the recovery password.",
        "title": "What do I do if I forgot the device password?"
      },
      "reset": {
        "text": "Enter a wrong device password 15 times. The last few attempts require a long touch on the device.",
        "title": "How do I reset the device?"
      }
    },
    "waiting": {
      "deviceNotRecognized": {
        "text": "The device should blink once when inserted. Make sure that it is inserted the right way around. If you are having trouble, please contact us through the link below.",
        "title": "My BitBox01 is not recognized"
      },
      "getDevice": {
        "link": {
          "text": "Order a BitBox",
          "url": "https://shiftcrypto.ch/shop"
        },
        "text": "You can buy a BitBox in our online shop:",
        "title": "How can I get a device?"
      },
      "internet": {
        "text": "Yes, an internet connection is required to synchronize the wallet, send transactions and retrieve the latest exchange rates.",
        "title": "Does this app require an internet connection?"
      },
      "lostDevice": {
        "link": {
          "text": "Backup Center",
          "url": "https://shiftcrypto.ch/backup"
        },
        "text": "You can recover your accounts on a new BitBox or with our backup center.",
        "title": "I lost my device. Now what?"
      },
      "useWithoutDevice": {
        "text": "Unfortunately, this is not yet possible at the moment.",
        "title": "Can I use the app without a device?"
      },
      "welcome": {
        "text": "Thanks for using this app built by Shift Cryptosecurity in Switzerland. We appreciate any input you have to share. Please give feedback using the link at the bottom.",
        "title": "Welcome to the BitBoxApp!"
      }
    }
  }
}

def extract_values(obj, key):
    """Pull all values of specified key from nested JSON."""
    arr = {}

    def extract(obj, arr, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    print("yes")
                    extract(v, arr, key)
                elif k in key:
                    if k == "text":

                    string = k + ": "+ v
                    arr.append(string)
        #elif isinstance(obj, list):
            #for item in obj:
                #extract(item, arr, key)
        return arr

    results = extract(obj, arr, key)
    return results

results = extract_values(json, ["text", "title"])
#print(results)
