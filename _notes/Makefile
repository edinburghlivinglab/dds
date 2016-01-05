lecturedir := ../lectures
HTML := $(patsubst %.md, %.html, $(wildcard *.md))


all: $(HTML)

install:
	cp $(MD) $(installdir)

%.html : %.md
	pandoc -t revealjs -V theme=sky -s $< -o $@ 

clean:
	rm $(HTML)






