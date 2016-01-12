installdir := ../slides
HTML := $(patsubst %.md, %.html, $(wildcard *.md))
PDF := $(patsubst %.md, %.pdf, $(wildcard *.md))

# OPTIONS := --variable theme=sky --variable revealjs-url="../assets/reveal.js"  --standalone
OPTIONS := --variable revealjs-url="../assets/reveal.js"  --standalone

all: $(HTML) install

# pdf: $(PDF)

%.html : %.md
	pandoc --smart -t revealjs $(OPTIONS) $< -o $@


# %.pdf : %.md
# 	pandoc -t beamer -s $< -o $@ 


install:
	mv $(HTML) $(installdir)

clean:
	rm $(HTML) $(PDF) 

