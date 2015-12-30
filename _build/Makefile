PAGES := prep.md fast_hack.md digging_deeper.md slow_hack.md reporting.md
HANDBOOK := handbook.md
PDF := $(patsubst %.md, %.pdf, $(HANDBOOK))

PANDOC := /usr/local/bin/pandoc


pdf: $(PAGES)
	$(PANDOC) -s -V geometry:margin=1in --number-sections $^ -o $(PDF)




