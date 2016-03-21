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
	rm -f *.log
	./main clean
	find dat/clean -depth -empty -delete

classify:
	rm -rf dat/classified
	mkdir dat/classified
	./main classify

render:
	rm -rf dat/rendered
	mkdir dat/rendered
	./main render

.PHONY: list fetch unpack
