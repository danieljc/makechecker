main.pdf: main.dvi
	dvipdfm main

main.dvi: main.tex \
	section/*.tex

	latex main
	bibtex main
	latex main
	latex main

read:
	xpdf main.pdf
clean:
	rm -f *.aux *.bbl *.log *.dvi *.bak *.blg
