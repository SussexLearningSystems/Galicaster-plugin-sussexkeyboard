Sussexkeyboard Plugin
=====================

Uses onboard to display an on screen keyboard.

Configuration of onboard via dconf tools is separate from the plugin, some useful dconf settings are:

::

  [org/gnome/desktop/interface]
  toolkit-accessibility=true

  [org/onboard/auto-show]
  enabled=true
  hide-on-key-press=false

  [org/onboard/lockdown]
  disable-preferences=true
  disable-quit=true
  disable-touch-handles=true

  [org/onboard/window/landscape]
  dock-expand=false

  [org/onboard/window]
  docking-enabled=true
  force-to-top=true

  [org/onboard]
  show-status-icon=false
  show-tooltips=false
  start-minimized=true
  system-theme-tracking-enabled=false
  use-system-defaults=false
  xembed-onboard=true


It may also be sensible to customise and set a layout (org/onboard/layout), 'Phone' works but the
menus can be confusing when latching pages and allowing the use of emojis may be undesirable.