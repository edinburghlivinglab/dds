lecturedir := ../lectures
HTML := $(patsubst %.md, %.html, $(wildcard *.md))


all: $(HTML)

install:
	cp $(MD) $(installdir)

%.html : %.md
	pandoc -t revealjs  -s $< -o $(lecturedir)/$@ 

clean:
	rm $(HTML)






