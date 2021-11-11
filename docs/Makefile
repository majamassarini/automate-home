# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SPHINXGHERKIN ?= sphinx-gherkindoc
SOURCEDIR     = source
BUILDDIR      = build
OUTGHERKINDIR = "$(SOURCEDIR)"/features
INGHERKINDIR  = ../home/features/


# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile gherkindoc

gherkindoc:
	rm -rf $(OUTGHERKINDIR)
	@$(SPHINXGHERKIN) "$(INGHERKINDIR)" "$(OUTGHERKINDIR)"


# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile gherkindoc
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
