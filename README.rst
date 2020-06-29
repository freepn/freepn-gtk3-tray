============================================
 freepn-gtk3-tray - fpnd control/status GUI
============================================

freepn-gtk3-tray is a daemon control and status application for `fpnd`_ on
Linux.

And by "application" we mean a simple appindicator-based GUI which is
basically just an icon with a menu. It loads in the indicator area or the
system tray (whatever is available in your desktop environment). The icon's
menu allows you to start and stop the daemon, as well as get daemon status
and query the Ubuntu geoip location server.

Functionally this app does (almost) nothing without having the above `fpnd`_
package installed, although it does not currently require it as a package
dependency.

It also depends on PyGobject, a GTK+3 desktop environment, and the associated
gobject introspection libraries.  The minimal package deps are currently used
in the freepn-gtk3-tray ebuild and deb packages linked in the fpnd readme.

Lastly, the fpnd packages will install the polkit (or sudo) rules required
for the daemon controller commands in the the GUI app.


.. _fpnd: https://github.com/freepn/fpnd

