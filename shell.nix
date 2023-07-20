# This defines a function taking `pkgs` as parameter, and uses
# `nixpkgs` by default if no argument is passed to it.
{ pkgs ? import <nixpkgs> {} }:

# This avoids typing `pkgs.` before each package name.
with pkgs;

# Defines a shell.
mkShell {
  # Sets the build inputs, i.e. what will be available in our
  # local environment.
  buildInputs = [ 
    haskellPackages.pandoc
    haskellPackages.pandoc-crossref
    texlive.combined.scheme-full
    ipafont
    libGL
    gtk3
    gtkmm3
    webkitgtk
    python310
    python310Packages.pywebview
    python310Packages.pyqtwebengine
    python310Packages.pyqt5
    python310Packages.pygobject3
    python310Packages.gst-python
    gobject-introspection
     gsettings-desktop-schemas
     shadow
     xorg.xhost
  ];
}
