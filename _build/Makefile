installdir := ../course_docs

PAGES := prep.md fast_hack.md digging_deeper.md slow_hack.md reporting.md
HANDBOOK := handbook.md
PDF := $(patsubst %.md, %.pdf, $(HANDBOOK))


PANDOC := /usr/local/bin/pandoc

install: pdf
	mv $(PDF) $(installdir)

pdf: $(PDF)

$(PDF): $(PAGES)
	$(PANDOC) --latex-engine=xelatex --template=latex.template --number-sections  $^ -o $(PDF)




