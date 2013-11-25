# make PARTY="AFRICAN NATIONAL CONGRESS" OUTFILE="anc"
cmd=sh -c "grep -l '$(PARTY)' *.txt | sort -u | sed 's/txt/pdf/' | tr '\n' ' '"
joined_file=$(OUTFILE)
candidates_file=candidates.pdf
candidates_url=http://www.elections.org.za/content/uploadedFiles/2009%20National%20and%20Provincial%20Election%20candidate%20lists.pdf?n=9511

all: $(OUTFILE).dat

$(candidates_file):
	@echo "Downloading file"
	@curl $(candidates_url) > $(candidates_file) 2> /dev/null

extracted.flag: $(candidates_file)
	@echo "Extracting PDF"
	@pdftk $(candidates_file) burst
	@ls -1 pg_*.pdf | xargs -n 1 pdftotext
	@touch extracted.flag

$(joined_file).txt: extracted.flag
	@echo "Joining party files"
	@pdftk `$(cmd)` cat output "$(joined_file).pdf"
	pdftotext $(joined_file).pdf

$(OUTFILE).dat: $(joined_file).txt
	@echo "Running stats"
	@python ids.py $(joined_file).txt "$(PARTY)" > $(OUTFILE).dat

clean_small:
	@echo "Removing temporary files"
	@rm -f $(joined_file).*

clean:
	@echo "Removed flags"
	@rm -f *.flag
	@rm -f *.pdf
	@rm -f *.txt

