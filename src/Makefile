PKG = FEP

$(PKG).gfn: $(PKG).inp $(PKG).spec $(PKG)_sample.inp
	gretlcli --makepkg $(PKG).inp


$(PKG).zip: $(PKG).gfn  copy_pdf copy_data
	echo makepkg $(PKG).zip | gretlcli -b -

copy_pdf : ../docs/$(PKG).pdf
	cp -r ../docs/$(PKG).pdf ./

copy_data : ../data/FEPdata.gdt
	cp -r ../data/FEPdata.gdt ./

install: $(PKG).zip
	echo "pkg install $(PKG).zip --local" | gretlcli -b -

tarball : clean
	tar -cvzf ../$(PKG).zip *

clean:
	rm -rf $(PKG).zip $(PKG).gfn
	rm -rf session.inp
	rm -rf ./$(PKG).pdf
	rm -rf ./FEPdata.gdt
