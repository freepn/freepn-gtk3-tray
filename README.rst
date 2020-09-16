============================================
 freepn-gtk3-tray - fpnd control/status GUI
============================================

freepn-gtk3-tray is a daemon control and status application for `fpnd`_ on
Linux.

.. image:: https://img.shields.io/github/license/freepn/freepn-gtk3-tray
    :target: https://github.com/freepn/freepn-gtk3-tray/blob/master/LICENSE

.. image:: https://img.shields.io/github/v/tag/freepn/freepn-gtk3-tray?color=green&include_prereleases&label=latest%20release
    :target: https://github.com/freepn/freepn-gtk3-tray/releases
    :alt: GitHub tag (latest SemVer, including pre-release)

.. image:: https://travis-ci.org/freepn/freepn-gtk3-tray.svg?branch=master
    :target: https://travis-ci.org/freepn/freepn-gtk3-tray

.. image:: https://img.shields.io/codeclimate/maintainability/freepn/freepn-gtk3-tray
    :target: https://codeclimate.com/github/freepn/freepn-gtk3-tray


And by "application" we mean a simple appindicator-based GUI which is
basically just an icon with a menu. It loads in the indicator area or the
system tray (whatever is available in your desktop environment). The icon's
menu allows you to start and stop the daemon, as well as get daemon status
and query the Ubuntu geoip location server.  The tray icon appearence will
update to show the current state of the network daemon.

Functionally this app does (almost) nothing without having the above fpnd_
package installed, however, the latest freepn-gtk3-tray packages now depend
on the appropriate fpnd_ packages (for both Ubuntu and Gentoo).

This app also depends on PyGobject, a GTK+3 desktop environment, and the associated
gobject introspection libraries.  The minimal package deps are currently used
in the freepn-gtk3-tray ebuild and deb packages linked in the fpnd readme.

Lastly, the fpnd packages will install the polkit rules required for the
daemon controller commands used in the the GUI app.


Pre-install
-----------

See the Quick Start section of the fpnd_ readme file and install the PPA_
for Ubuntu or the `python-overlay`_ for Gentoo, then make sure your local
user is a member of the ``fpnd`` group.


.. _PPA: https://launchpad.net/~nerdboy/+archive/ubuntu/embedded
.. _python-overlay: https://github.com/freepn/python-overlay


Install
-------

Following the PPA or overlay install, use the appropriate package manager to
install the packages for your distro:

* Gentoo - ``sudo emerge freepn-gtk3-tray``
* Ubuntu - ``sudo apt-get install freepn-gtk3-indicator``

Usage
-----

Select FreePN Tray Control from the Applications View or the Internet menu in
your desktop of choice, eg, Gnome, Unity, Xfce, etc.  You can also add it to
your session startup or run it from an X terminal to get some debug output::

  $ freepn-gtk3-indicator


.. _fpnd: https://github.com/freepn/fpnd

