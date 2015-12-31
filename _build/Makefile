installdir := ../course_docs

INDEX := index.md
PAGES := $(INDEX) $(MD) 

HANDBOOK := handbook.md
PDF := $(HANDBOOK:md=pdf)
#PDF := $(patsubst %.md, %.pdf, $(HANDBOOK))

PANDOC := /usr/local/bin/pandoc

ci: install
	git ci -m "updated handbook" $(installdir)/$(PDF)

install: pdf
	mv $(PDF) $(installdir)

pdf: $(PDF)

$(PDF): $(PAGES)
	$(PANDOC) --latex-engine=xelatex --template=latex.template --number-sections $^ -o $(PDF)




