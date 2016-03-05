installdir := ../slides
NEW := week8-1.md 
ALLHTML := $(wildcard *.html)
HTML := $(patsubst %.md, %.html, $(NEW))


# OPTIONS := --variable theme=sky --variable revealjs-url="../assets/reveal.js"  --standalone
OPTIONS := --variable revealjs-url="../assets/reveal.js"  --include-in-header="style.css" --standalone

all: $(HTML)


%.html : %.md
	pandoc --smart -t revealjs $(OPTIONS) $< -o $@
	cp $@ $(installdir)



#install: $(HTML)
#	cp $(HTML) $(installdir)

clean:
	-rm $(ALLHTML)

