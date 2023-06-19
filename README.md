<div align="center">

<h1><b>Termslime</b></h1>

<p>Termslime displays images in your terminal with true colors.</p>

<p>
    <img src="https://img.shields.io/pypi/v/termslime.svg">
    <img src="https://img.shields.io/pypi/pyversions/termslime.svg">
    <img src="https://img.shields.io/github/last-commit/garyzbm/termslime">
</p>

</div>


## Contents

+ [Requirements](#requirements)
+ [Installation](#installation)
+ [Usage](#usage)
+ [Credits](#credits)


## Requirements

+ A terminal emulator with true color support.
+ Python >= 3.7.


## Installation

Install with [pipx](https://pypa.github.io/pipx/) (recommended):
```shell
pipx install termslime
```

Or install with pip:
```shell
pip install termslime
```


## Usage

```
usage: tslime [-h] [-hl HEIGHTLIMIT] [-wl WIDTHLIMIT] [-bp BEGINPADDING] [-ep ENDPADDING] [-lp LEFTPADDING] path

Termslime displays images in your terminal with true colors. Project home page: https://github.com/garyzbm/termslime

positional arguments:
  path                  path to an image file or a directory containing image files

options:
  -h, --help            show this help message and exit
  -hl HEIGHTLIMIT, --heightLimit HEIGHTLIMIT
                        maximum number of lines of blocks to display the image in the terminal
  -wl WIDTHLIMIT, --widthLimit WIDTHLIMIT
                        maximum number of blocks per line to display the image in the terminal
  -bp BEGINPADDING, --beginPadding BEGINPADDING
                        number of empty lines before the image
  -ep ENDPADDING, --endPadding ENDPADDING
                        number of empty lines after the image
  -lp LEFTPADDING, --leftPadding LEFTPADDING
                        number of empty spaces at the beginning of each line of the image
```


## Credits

This project is greatly inspired by [this post](https://lucamug.medium.com/terminal-pixel-art-ad386d186dad).

The following projects are crucial to the development of this project:
+ [colorful](https://github.com/timofurrer/colorful)
+ [pillow](https://python-pillow.org)
+ [poetry](https://python-poetry.org)


---
*<p align="center">This project is published under [MIT](LICENSE).<br>A [Gary Zhang](https://github.com/garyzbm) project.<br>- :tada: -</p>*