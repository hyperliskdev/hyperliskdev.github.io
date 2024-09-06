---
layout: post
title: "Malware Analysis: Stuxnet"
date: 2024-09-05
categories: cybersecurity malware volatility 
---

In this post, we will be going over the stuxnet virus using Volatility.

## Pre-Start

A reoccurring piece of information that is needed for this investigation is the image profile. This is done by using the imageinfo command.

![Image Info](/assets/img/stuxnet-investigation/image_info.png)

The suggested profile is WinXPSP2x86.

## Part I - Services/Processes

First section is the most basic. Using the `psscan` and `pstree` commands we can find the active running processes on the machine.

![Process Scan](/assets/img/stuxnet-investigation/psscan.png)

![Process Tree](/assets/img/stuxnet-investigation/pstree.png)

Looking at these processes the only thing that sticks out is the multiple instances of the `lsass.exe`. After some research, `lsass.exe` is the Local Security Authority Subsystem Service. This service is a **core service** and provides all the process functionality

[*The Local Security Authority(LSA) is a protected subsystem that maintains the information about all aspects of local security on a system (collectively known as the local security policy and provides various services for translation between names and identifiers.)*](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-2000-server/cc961760(v=technet.10))



![LSA](/assets/img/stuxnet-investigation/cc961760.dsbg02(en-us,technet.10).gif)

