PAGESDIR := pages
DOCSDIR := course_docs
BUILDIR := _build
PAGES := prep.md fast_hack.md digging_deeper.md slow_hack.md reporting.md
HANDBOOK := handbook.md
PDF := $(patsubst %.md, %.pdf, $(HANDBOOK))

headed := $(addprefix $(PAGESDIR)/, $(PAGES))
headless := $(addprefix $(BUILDIR)/, $(PAGES))	

STRIPPER := _scripts/preprocess.py
PANDOC := /usr/local/bin/pandoc

local:
	bundle exec jekyll serve --config _config.yml,_config_dev.yml
	

headless: $(headed)
	python $(STRIPPER) -v -outdir $(BUILDIR) $^


pdf: headless
	$(MAKE) -C $(BUILDIR)

clean:
	rm -f $(BUILDIR)/*.md


