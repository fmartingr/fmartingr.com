---
title: Using ssh_config Match to connect to a host using multiple IP or Hostnames
date: 2022-08-12
publishdate: 2022-08-12
type: blog
---

My main computer is a MacBook Pro from 2017, but I have some servers laying around and one other laptop connected at home
with ArchLinux installed that I use mainly for development. I connect to it remotely either directly using a
SSH/Mosh + Tmux + Emacs/Vim combination, or using the pretty convenient VSCode Remote Extensions when I'm not feeling
much of a _hacker_.

<!--more-->

Thing is, I may access this computer either from my home network directly if I'm at home or via a SDN if I am not (at the office,
coffeeshop, visiting family, etc).

My approach was to setup the hosts directly on my `~/.ssh/ssh_config` as you would with different machines:

``` bash
# .ssh/config
Host laptop.lan
    HostName 192.168.1.2 # Internal network IP

Host laptop.sdn
    Hostname 10.0.0.2 # SDN IP
```

That way, I would connect to each one of them depending on the situation. Using tmux and ssh is not that much of a problem
since I could just detach from home, go away, then connect via SDN an everything would be there (though I had to remember
which alias to use instead of just `ssh laptop`). For VSCode is not that convenient since I would need to close the connection,
made a new one to the new host and so on. Surely we could made this simpler, right?

In my home network, my main router is also my DNS server (with Ad Blocking, rules and all kind of fancy things), and that
server resolves my local domain (`*.lan`) to LAN IP Addresses, so I can start with a simple config as I had previously:

``` bash
# .ssh/config
Host laptop
    HostName laptop.lan
```

Now, what happens if I'm not at home? I could solve this in several ways:
- I could `ping` my router, but that could collide with other networks out there.
- I could check if my Wifi BSSID is one of the APs at home, but I could also connect via Ethernet.
- I could check if I can resolve the `laptop.lan` address, though this requires network access, but in the end is the one I ended
  up using.

``` bash
$ dig +short laptop.lan
192.168.1.2 # At home

$ dig +short laptop.lan
# Empty result when away from home
```

Now, here comes the [`Match`](https://man7.org/linux/man-pages/man5/ssh_config.5.html) magic:

``` bash
# .ssh/config
Host laptop
    HostName laptop.lan

Match originalhost laptop exec "[[ $(/usr/bin/dig +short laptop.lan) == '' ]]"
    HostName laptop.sdn
```

Using `Match` we can replace properties for a defined host using matches. In this ad-hoc example what I did is:

- `Match originalhost laptop`: The connection host need to match `laptop`
- `exec "[[ $(/usr/bin/dig +short laptop.lan) == '' ]]"`: Execute `dig` and try to resolve my LAN's laptop domain name.
  This needs to be a successful command for it to match, in this case we compare `dig`s output to an empty string to evaluate
  if we can resolve the `laptop.lan` domain name (check the `[[ ]]`).
- `HostName laptop.sdn` If both rules match, replace the `HostName` property with the laptop's SDN domain name.

This is a pretty easy way to just `ssh laptop` wherever I am. I didn't knew about this particular
keyword until today, and it's pretty powerful!

Documentation: [ssh_config(5) manpage](https://man7.org/linux/man-pages/man5/ssh_config.5.html)
