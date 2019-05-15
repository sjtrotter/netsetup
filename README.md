# netsetup
Networking setup script, Windows and RHEL independent. Provides a single commandline interface for setting the following:  hostname; MAC address; IP address (manual or dynamic); firewall profile; and allowed/disallowed input and output networks/hosts.

![screenshot?]()

## Installation

Nothing extra required other than a current Python3 installation with standard libraries installed. Utilizes sys, argparse, ipaddress, and random modules.

## Usage example

If you have chmod'd the script to +x:
```
netexpand.py 192.168.1.0/30
192.168.1.1
192.168.1.2
```
Otherwise:
```
python3 netexpand.py 192.168.1.0/30 -r
192.168.1.2
192.168.1.1
```

## Development setup

Same as install, nothing special here. Just need a working Python3 install, with sys and argparse modules.

## Release History

* 0.0.0
    * Working on README, LICENSE, and deciding on best commandline argument parser for python.

## Meta

Stephen Trotter – stephen.j.trotter@gmail.com

Distributed under the GNU GPLv3 license. See ``LICENSE`` for more information.

[https://github.com/sjtrotter/netexpand](https://github.com/sjtrotter/)

## Contributing

1. Fork it (<https://github.com/yourname/yourproject/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->
[wiki]: https://github.com/sjtrotter/netexpand/wiki
