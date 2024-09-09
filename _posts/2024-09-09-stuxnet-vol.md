---
layout: post
title: "Malware Analysis: Stuxnet"
date: 2024-09-09
categories: cybersecurity malware volatility 
---

In this post, we will be going over the Stuxnet virus using Volatility.

## Pre-Start

A reoccurring piece of information that is needed for this investigation is the image profile. This is done by using the imageinfo command.

![Image Info](/assets/img/stuxnet-investigation/image_info.png)

The suggested profile is WinXPSP2x86.

## Part I - Services/Processes

First section is the most basic. Using the `psscan` and `pstree` commands we can find the active running processes on the machine.

![Process Scan](/assets/img/stuxnet-investigation/psscan.png)


In this process tree, the red outlined processes seem to be normal (`winlogon.exe` is the parent of the red `lsass.exe`). The purple outlined processes are the suspicious ones. The `lsass.exe` copies in purple have the parent of the `services.exe`. 
![Process Tree](/assets/img/stuxnet-investigation/pstree.png)

Looking at these processes the only thing that sticks out is the multiple instances of the `lsass.exe`. After some research, `lsass.exe` is the Local Security Authority Subsystem Service. This service is a **core service** and its only parent should be either `winlogon.exe` or in Vista and later, it is created by the `wininit.exe`.$^{[1]}$

>[*The Local Security Authority(LSA) is a protected subsystem that maintains the information about all aspects of local security on a system (collectively known as the local security policy and provides various services for translation between names and identifiers.)*](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-2000-server/cc961760(v=technet.10))


This diagram contains the inner workings of the Local Security Authority Subsystem Service. This could be dated after XP but this is generally how it works.
![LSA](/assets/img/stuxnet-investigation/cc961760.dsbg02(en-us,technet.10).gif)


So we have identified that two suspicious processes through `pstree`. Both are children of PID 668.

1. `lsass.exe` : PID: 868
2. `lsass.exe` : PID: 1928

## Part II - Process Hashes

Most detected viruses are detected through hash matches, using VirusTotal we can check the hash of a given process and figure out if it is malicious.

To dump the processes and take a look into the hashes we can use the `procdump` command.

![Process Dump](/assets/img/stuxnet-investigation/proc_dump.png)

Then we can check the sha256 hashes using `sha256sum`.

![sha256sum](/assets/img/stuxnet-investigation/sha256sum.png)


Now we can take a look at these two processes hashes on VirusTotal and see if they are malicious.

![VirusTotal: 868](/assets/img/stuxnet-investigation/868_virustotal.png)

![VirusTotal: 1928](/assets/img/stuxnet-investigation/1928_virustotal.png)


### References

1 | [*Mark Russinovich: Analyzing the Stuxnet Virus with Sysinternals Tools (Part 1)*](https://learn.microsoft.com/en-us/archive/blogs/mark_russinovich/stuxnet-1089-3)

2 | [*Mark Russinovich: Analyzing the Stuxnet Virus with Sysinternals Tools (Part 2)*](https://learn.microsoft.com/en-us/archive/blogs/mark_russinovich/stuxnet-1089-2)

3 | [*Mark Russinovich: Analyzing the Stuxnet Virus with Sysinternals Tools (Part 3)*](https://learn.microsoft.com/en-us/archive/blogs/mark_russinovich/stuxnet-1089)

4 | [*MNIN Security Blog - Coding, Reversing, Exploiting (Stuxnet's Footprint in Memory with Volatility 2.0)*](https://mnin.blogspot.com/2011/06/examining-stuxnets-footprint-in-memory.html)

5 | [*Local Security Authority Subsystem Service  - Wikipedia*](https://en.wikipedia.org/wiki/Local_Security_Authority_Subsystem_Service#:~:text=Local%20Security%20Authority%20Subsystem%20Service%20(LSASS)%20is%20a%20process%20in,security%20policy%20on%20the%20system.)

