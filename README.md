# Collage papers to image

This repository helps convert a pdf to a collage image containing the pages of the pdf.

Below is an example of a collage created for [this paper](https://arxiv.org/pdf/1602.04506v1.pdf):

![Example collage image](https://github.com/ranjaykrishna/collage/blob/master/paper.jpg "Example collage image")


## Usage

Dependencies:
imagemagick - ```sudo apt-get install imagemagick```

Terminal command:
```
python collage.py -paper paper.pdf -num-pages 8
```

Below are explanation for the 
```
-paper is the path to the pdf that you want to collage
-num-pages is the number of pages to extract and collage
-timeout determines how long to wait for the convert script before quitting.
```
