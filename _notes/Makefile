installdir := ../slides
HTML := $(patsubst %.md, %.html, $(wildcard *.md))
PDF := $(patsubst %.md, %.pdf, $(wildcard *.md))

OPTIONS := --variable theme=sky --variable revealjs-url="../assets/reveal.js" --slide-level=1 --standalone

all: $(HTML) install

pdf: $(PDF)

%.html : %.md
	pandoc -t revealjs $(OPTIONS) $< -o $@


%.pdf : %.md
	pandoc -t beamer -s $< -o $@ 


install:
	mv $(HTML) $(installdir)

clean:
	rm $(HTML) $(PDF) 

