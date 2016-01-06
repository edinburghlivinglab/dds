installdir := ../slides
HTML := $(patsubst %.md, %.html, $(wildcard *.md))
PDF := $(patsubst %.md, %.pdf, $(wildcard *.md))

VARS := --variable theme=sky --variable revealjs-url="../assets/reveal.js"

all: $(HTML) install

pdf: $(PDF)

%.html : %.md
	pandoc -t revealjs $(VARS) -s $< -o $@


%.pdf : %.md
	pandoc -t beamer -s $< -o $@ 


install:
	mv $(HTML) $(PDF) $(installdir)

clean:
	rm $(HTML) $(PDF) 

