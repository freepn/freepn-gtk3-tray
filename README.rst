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

Lastly, the fpnd package will install the polkit rules required for the
daemon controller commands used in the the GUI app.


Getting Started
===============

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


User Node State
===============

In addition to the commands used to control fpnd daemon, the tray GUI
displays the current daemon state using both the icon and labels, but
exactly how they are displayed depends on both the desktop environment
and the default theme and icons.  Desktop environments using gnome shell
should display the labels in the status bar next to the icon, but in
other despktops the labels may appear as (mouse-over) tooltips.

Each "state" has a corresponding label and tray icon:

* when ``fpnd`` daemon is stopped: state message is 'NONE'
* when the daemon is started: state is 'WAITING' before moon is queried
* after moon query is successful: state changes to 'STARTING'
* after announce/cfg messages are sent: state is 'WAITING'
* valid reply to cfg message triggers state change to 'CONFIG'
* both networks up and correct (exit) route triggers 'CONNECTED' state

The user node should stay in the 'CONNECTED' state until user shutdown of the
daemon, in which case it returns to the stopped 'NONE' state.  Several events
(mostly external) will cause the user node state to change *temporarily* from
the 'CONNECTED' state to a short sequence of 'WAITING' and 'CONFIG' states, as
well as a possible 'ERROR' state, before returning to the 'CONNECTED' state.


State change events
-------------------

* starting and stopping of the daemon are user-initiated events
* 'CONFIG' events are generated after successful startup
* 'CONFIG' events are also generated if:

  + user node's upstream peer goes offline
  + user node's upstream route goes bad (peer is "wedged")
  + user_node is attached to exit node and network closure is triggered
  + user node is (randomly) selected to attach new node(s)


Note about states
-----------------

* 'NONE' state is written once on shutdown and updated in the GUI (may be seen
  briefly at startup)
* 'STARTING' is written once at startup and is updated very quickly after
* 'WAITING' is written twice every (10) seconds until a state change
* 'CONFIG' is written only on a cfg change event (both up and down)
* 'CONNECTED' is written once every (33) seconds until a state change
* the tray icon only changes if the state message changes from previous state
