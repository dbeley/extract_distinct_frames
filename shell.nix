with import <nixpkgs> { };

let
  pythonPackages = python3Packages;
in pkgs.mkShell rec {
  buildInputs = [
    python3
    pythonPackages.pip
    pythonPackages.yt-dlp
    pythonPackages.img2pdf
    pythonPackages.tqdm
    pythonPackages.pillow
    ffmpeg
  ];

}
