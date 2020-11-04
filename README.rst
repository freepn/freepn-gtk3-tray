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
and query the Ubuntu geoip location server.  The tray icon appearance will
update to show the current state of the network daemon.

Functionally this app does (almost) nothing without having the above fpnd_
package installed, however, the latest freepn-gtk3-tray packages now depend
on the appropriate fpnd_ packages (for both Ubuntu and Gentoo).

This app also depends on PyGobject, a GTK+3 desktop environment, and the associated
gobject introspection libraries.  The minimal package deps are currently used
in the freepn-gtk3-tray ebuild and deb packages linked below.

Lastly, the fpnd_ package will install the polkit rules required for the
daemon controller commands used in the the GUI app.


More Docs for FreePN tools
==========================

* `DNS Privacy`_ - DNS and your online privacy
* `DNS Setup`_ - Local DNS setup
* `fpnd Quick Start`_ - Quick install and setup instructions
* `fpnd Release Notes`_ - fpnd Software Version Description (latest release)


.. _DNS Privacy: https://github.com/freepn/fpnd/blob/master/README_DNS_privacy.rst
.. _DNS Setup: https://github.com/freepn/fpnd/blob/master/README_DNS_setup.rst
.. _fpnd Quick Start: https://github.com/freepn/fpnd#quick-start
.. _fpnd Release Notes: https://github.com/freepn/fpnd/blob/master/README_0.9.0-release-notes.rst


Getting Started
===============

Pre-install
-----------

See the Quick Start section of the fpnd_ readme file and install the PPA_
for Ubuntu or the `freepn-overlay`_ for Gentoo.


.. _PPA: https://launchpad.net/~nerdboy/+archive/ubuntu/embedded
.. _freepn-overlay: https://github.com/freepn/freepn-overlay


Install
-------

Following the PPA or overlay install, use the appropriate package manager to
install the packages for your distro:

* Gentoo - ``sudo emerge freepn-gtk3-tray``
* Ubuntu - ``sudo apt-get install freepn-gtk3-indicator``

Then make sure your local user is a member of the ``fpnd`` group.

.. note:: For Gentoo be sure and enable the ``polkit`` USE flag for ``fpnd``
          so you get proper permissions.


Usage
-----

Select FreePN Tray Control from the Applications View or the Internet menu in
your desktop of choice, eg, Gnome, Unity, Xfce, etc.  You can also add it to
your session startup or run it from an X terminal to get some debug output::

  $ freepn-gtk3-indicator

You can also see some screenshots of the icons and menu in `this section`_ of
the fpnd README file.


.. _fpnd: https://github.com/freepn/fpnd
.. _this section: https://github.com/freepn/fpnd#some-screenshots


Usage Notes
-----------

Starting with the ``fpnd-0.9.7`` and ``freepn-gtk3-tray-0.0.8`` releases,
both packages include version detection and handling for the ``fpnd``
daemon component. This adds a new 'UPGRADE' state message and a GUI
indicator message triggered if the installed ``fpnd`` version is too
old or otherwise incompatible with the running infra node version.
The latest version of ``fpnd`` adds the running version to the initial
"node announce" message, which is checked against the minimum compatible
version (currently ``0.9.6``) and then accepted if the user node version
is greater-than or equal-to the minimum "base" version.

In the event of a version error, newer user nodes will log the error,
update the state message, and then shut down (daemon status is "crashed").
If using the newer GUI release, there will be a corresponding indicator
pop-up message.  However, older versions can only write the error message
to the ``fpnd`` log file, so you would need to search the log file for
the string ``UPGRADE_REQUIRED``, eg::

  $ grep UPGRADE_REQUIRED /var/log/fpnd/fpnd.log

(or just ``/var/log/fpnd.log`` on Gentoo)

Since there is no version error handler in older versions of ``fpnd``
your node will appear to be "stuck" in the ``WAITING`` state and will be
blocked for at least 15 minutes; the answer is **upgrade your system**
and try connecting again.


User Node State
===============

In addition to the commands used to control fpnd daemon, the tray GUI
displays the current daemon state using both the icon and labels, but
exactly how they are displayed depends on both the desktop environment
and the default theme and icons.  Desktop environments using gnome shell
should display the labels in the status bar next to the icon, but in
other desktops the labels may appear as (mouse-over) tool-tips.

Each "state" has a corresponding label and tray icon:

* when ``fpnd`` daemon is stopped: state message is 'NONE'
* when the daemon is started: state is 'WAITING' before moon is queried
* if the daemon version is incompatible: state is 'UPGRADE' then shuts down
* after moon query is successful: state changes to 'STARTING'
* after announce/cfg messages are sent: state is 'WAITING'
* valid reply to cfg message triggers state change to 'CONFIG'
* both networks up and correct (exit) route triggers 'CONNECTED' state

The user node should stay in the 'CONNECTED' state until user shutdown of the
daemon, in which case it returns to the stopped 'NONE' state.  Several events
(mostly external) will cause the user node state to change *temporarily* from
the 'CONNECTED' state to a short sequence of 'WAITING' and 'CONFIG' states, as
well as a possible 'ERROR' state, before returning to the 'CONNECTED' state
(where "short" is typically a minute or less).


State change events
-------------------

* starting and stopping of the daemon are user-initiated events
* an 'UPGRADE' event is generated if the ``fpnd`` version is incompatible
* a 'CONFIG' events is generated after successful startup
* 'CONFIG' events are also generated if:

  + user node's upstream peer goes offline
  + user node's upstream route goes bad (peer is "wedged")
  + user node's downstream peer sends a bad route msg
  + user_node is attached to exit node and network closure is triggered
  + user node is (randomly) selected to attach new node(s)

.. note:: The transition time for a reconfiguration event should be no more
          than two or three minutes *maximum*, so if your state is "stuck"
          on WAITING or CONFIG for longer than three minutes or so, stopping
          and starting again should get you connected to a fresh peer.


About state message updates
---------------------------

* state messages are written by fpnd_ to ``/run/fpnd/fpnd.state`` and consumed
  by the GUI
* the tray icon and status only changes if the state message changes from previous state
* 'NONE' state is written once on shutdown and updated in the GUI (may be seen
  briefly at startup)
* 'STARTING' is written once at startup and is updated very quickly after
* 'WAITING' is written twice every (10) seconds until a state change
* 'CONFIG' is written only on a network change event (both up and down)
* 'CONNECTED' is written once every (33) seconds until a state change
* 'UPGRADE' is written once before auto-shutdown
