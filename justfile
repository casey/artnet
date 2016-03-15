list:
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$' | xargs

fetch:
	cd dat/raw && wget -mk http://artscene.textfiles.com/artpacks/;:
	cd dat/raw && wget -mk http://artscene.textfiles.com/acid/;:
	cd dat/raw && wget -mk http://artscene.textfiles.com/ice/;:

unpack:
	rm -rf dat/unpacked
	mkdir dat/unpacked
	./main unpack

clean:
	rm -rf dat/clean
	mkdir dat/clean
	./main clean
	find dat/clean -depth -empty -delete

.PHONY: list fetch unpack
