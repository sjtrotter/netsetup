# netsetup
`netsetup` aims to be a frontend for multiple lower level programs that deal with networking. Things like hostnames, NTP, DNS servers, DHCP vs manual configuration, IP address, MAC address, netmask, gateway, firewall rules .. (this list may not be all-inclusive). Once more fully feature-complete, I'll change this to a list of items instead.

![screenshot?]()

## Installation

Previous: Nothing extra required other than a current Python3 installation with standard libraries installed. Utilizes sys, argparse, ipaddress, and random modules.

Now: Standby. I'll rewrite this section as needed. It may turn out we need some non-standard modules.

## Usage example

Usage examples will be coming after development.

## Development setup

I like using VSCode, but YMMV. The most important thing is to make sure you are on the latest development branch when contributing.

- Clone the repository (upper-right Code button, or): `git clone https://github.com/sjtrotter/netsetup.git`
- Checkout the latest version: `git checkout X.Y.Z`
- Set origin: `git push --set-upstream origin X.Y.Z`
- Pull latest updates: `git pull`

## Release History

* 0.0.0
    * Working on README, LICENSE, and deciding on best commandline argument parser for python.

## Meta

Stephen Trotter – stephen.j.trotter@gmail.com

Distributed under the GNU GPLv3 license. See ``LICENSE`` for more information.

[https://github.com/sjtrotter/netsetup](https://github.com/sjtrotter/)

## Contributing

1. Fork it (<https://github.com/sjtrotter/netsetup/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->
[wiki]: https://github.com/sjtrotter/netsetup/wiki
