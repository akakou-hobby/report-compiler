# report-compiler
The app compiles a MarkDown file into a PDF.

## dependencies
- nix

## usage

First, ensure the ipafont package is installed on your system.

```/etc/nixos/configuration.nix
  fonts = {
    fonts = [
      pkgs.ipafont
      # ...
```

Then, launch application:

```sh
git clone https://github.com/akakou-hobby/report-compiler/
cd report-compiler/
sh main.sh
```
