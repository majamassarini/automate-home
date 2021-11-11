#!/bin/bash

# Be sure tikz latex extension is installed
# Be sure to have latexpdf
# Be sure to have convert from ImageMagik without policy
# otherwise remove policy like
# sudo mv /etc/ImageMagick-6/policy.xml /etc/ImageMagick-6/policy.xmlout

START_DOCUMENT="\documentclass[preview]{standalone}
\usepackage[landscape]{geometry}
\usepackage{tikz-uml}
\\begin{document}
\input{"
END_DOCUMENT="}
\\end{document}
"

for file in `ls source/latex/ | grep -i tex`; do
  echo -n "$START_DOCUMENT" > /tmp/$file.tex
  echo -n "latex/$file" >> /tmp/$file.tex
  echo -n "$END_DOCUMENT" >> /tmp/$file.tex
  cd source
  pdflatex -interaction=nonstopmode /tmp/$file.tex
  convert $file.pdf $file.png
  pdf2svg $file.pdf $file.svg
  mv -f $file.png latex/
  mv -f $file.svg latex/
  rm $file.aux $file.log $file.pdf
  cd ..
done
