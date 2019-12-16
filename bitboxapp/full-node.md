---
layout: default
title: Full node support
nav_order: 4
has_children: false
parent: BitBoxApp
---

# {{page.parent}}: {{page.title}}
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

This functionality allows you to connect your full node to the BitBoxApp.

## Connecting to your full node without Tor
On your regular computer, configure the BitBoxApp to use your RaspiBolt:

* In the sidebar, select Settings > Connect your own full node
* In the field “Enter the endpoint” enter the hostname or ip address and the port, e.g. raspibolt.local:50002
* Click on “Download remote certificate”
* Click “Check”, you should be prompted with the message “Successfully establised a connection”
* Click “Add” to add your server to the list on the top
* Remove the Shift servers to only connect to your own server

## Connecting to your full node via Tor
If you have Tor installed on your computer, you can access your RaspiBolt remotely over Tor.

* In the sidebar, select Settings > Enable tor proxy
* Enable it and confirm the proxy address (usually the default 127.0.0.1:9050)
* When adding your RaspiBolt full node as described above, use your Tor address (e.g. gwdllz5g7vky2q4gr45zGuvopjzf33czreca3a3exosftx72ekppkuqd.onion:50002)
