0.0.8 (2020-11-03)
------------------
- Changelog.rst: add updates for latest release. [Stephen L Arnold]
- README.rst: add usage notes section for version checking. [Stephen L Arnold]
- Freepn-gtk3-indicator: add version handling, stale version indicator msg. [Stephen L Arnold]
- README.rst: add pointers to fpnd docs, update state notes. [Stephen Arnold]
- Add pointer to screenshots in fpnd readme. [Stephen Arnold]
- Add note about reconfiguration time to README.rst. [Stephen Arnold]
- README.rst: add note about polkit USE flag and cleanup typos. [Stephen Arnold]


0.0.7 (2020-09-18)
------------------
- Freepn-gtk3-indicator: bump version for release/packaging. [Stephen Arnold]
- Freepn-gtk3-indicator: fix all the About strings. [Stephen Arnold]


0.0.6 (2020-09-16)
------------------
- Bump version and remove superfluous menu option. [Stephen Arnold]
- README.rst: add some info on (daemon) state messages. [Stephen Arnold]
- README.rst: sync up with fpnd doc updates, add pointer to Quick Start. [Stephen Arnold]
- Fix stop state and pick up changelog entries. [Stephen Arnold]


0.0.5 (2020-07-31)
------------------
- Freepn-gtk3-indicator: bump version for packaging. [Stephen Arnold]
- Merge pull request #10 from freepn/icon_designs. [Steve Arnold]

  * Set the new alternate connected icon as the default. [Stephen Arnold]
  * Move the new things to the right places. [Stephen Arnold]
  * Delete network-freepn-connected-key-symbolic.svg. [Marianne Cruzat]
  * New key icons. [Marianne Cruzat]
  * New icon update. [Marianne Cruzat]

- Merge pull request #9 from freepn/cleanup. [Steve Arnold]

  * Add new test icon: network-freepn-connected-key2-symbolic.svg. [Stephen Arnold]
  * Add new changelog.rst and remove crufty test icon. [Stephen Arnold]


0.0.4 (2020-07-28)
------------------
- Merge pull request #7 from freepn/icons-and-ui. [Steve Arnold]
  Icons and ui testing, package up for evaluation
- Freepn-gtk3-indicator: fix copyright string in AboutDialog. [Stephen Arnold]
- Put the working icons under hicolor/status, keep fallback names. [Stephen Arnold]
- Install both sets of light/dark icons, swap config/waiting states. [Stephen Arnold]
- Add one more weird test icon and remove crufty ones. [Stephen Arnold]
- Add .gitattributes for default set of text/graphics/project files. [Stephen Arnold]
- Icons: save some test icons for inspection. [Stephen Arnold]
- Freepn-gtk3-indicator: set icon to NONE state on daemon shutdown. [Stephen Arnold]
- Add preferred email address to credits. [Stephen Arnold]
- Add About dialog fallback for runtimedir, make setup.py use app_version. [Stephen Arnold]
- Set default value for new-state (behind the if, over there) [Stephen Arnold]
- Merge pull request #6 from freepn/icon_designs. [Steve Arnold]
  New icon designs (acquiring, connected, error, no-route, offline)
- Updated the original folders and deleted unecessary files (Old designs) [Marianne Cruzat]
- New designs. [Marianne Cruzat]
- New icon designs (acquiring, connected, error, no-route, offline) [Marianne Cruzat]
- Enable label display, set label guide, add renamed test icons. [Stephen Arnold]

  * note the label display is still not fixed-width as the docs say it should be

- Replace high-contrast with light bg and revert to simple icon names. [Stephen Arnold]
- Add high contrast/symbolic icon, reorganize icon dirs, update setup.py. [Stephen Arnold]

  * also replace previous hicolor .svg with correct size (use the one from @mariannecruzat)

- README.rst: minor updates (tray icon state and dependency description) [Stephen Arnold]


