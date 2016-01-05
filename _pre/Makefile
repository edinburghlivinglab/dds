skeldir := ../course_docs
installdir := ../pages


PRE := $(wildcard *.pre)
MD := $(patsubst %.pre, %.md, $(PRE))

GPP := /opt/local/bin/gpp

all: $(MD)
	mv $< $(installdir)

%.md : %.pre
	$(GPP) -H -o $@ $<






