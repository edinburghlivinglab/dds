installdir := ../slides
HTML := $(patsubst %.md, %.html, $(wildcard *.md))


# OPTIONS := --variable theme=sky --variable revealjs-url="../assets/reveal.js"  --standalone
OPTIONS := --variable revealjs-url="../assets/reveal.js"  --standalone

all: $(HTML)


%.html : %.md
	pandoc --smart -t revealjs $(OPTIONS) $< -o $@
	cp $< $(installdir)



install: $(HTML)
	cp $(HTML) $(installdir)

clean:
	rm $(HTML)

