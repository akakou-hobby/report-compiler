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
    python311
    python311Packages.pywebview
    python311Packages.pyqtwebengine
    python311Packages.pyqt5
    python311Packages.pygobject3
    python311Packages.gst-python
    gobject-introspection
     gsettings-desktop-schemas
  ];
}
