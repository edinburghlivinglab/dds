installdir := ../slides
NEW := week2-1.md
#HTML := $(patsubst %.md, %.html, $(wildcard *.md))
HTML := $(patsubst %.md, %.html, $(NEW))


# OPTIONS := --variable theme=sky --variable revealjs-url="../assets/reveal.js"  --standalone
OPTIONS := --variable revealjs-url="../assets/reveal.js"  --standalone

all: $(HTML)


%.html : %.md
	pandoc --smart -t revealjs $(OPTIONS) $< -o $@
	cp $@ $(installdir)



#install: $(HTML)
#	cp $(HTML) $(installdir)

clean:
	rm $(HTML)

