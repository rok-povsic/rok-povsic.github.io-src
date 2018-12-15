Title: How to fix mouse offset bug in VMWare Workstation under Windows 8.1 host
Date: 2016-02-12 18:44
Category: vmware
Tags: vmware, bug
Authors: Rok Povšič

There’s a bug in mouse behavior that happened to me in VMWare Workstation under Windows 8.1 host with Ubuntu 14.04 as client. When hovering mouse over something and/or selecting something by dragging, the mouse moved it’s position by some offset. 

<!-- PELICAN_END_SUMMARY -->

See the GIF below.

<!-- PELICAN_END_SUMMARY -->

![VMWare bug]({filename}/images/vmware_bug.gif)

**How to fix it?**

- Locate VMWare Workstation, right click and open Properties.
- Under Compatibility check Disable display scaling on high DPI settings.
- Restart VMWare Workstation.

The mouse should now behave normally.