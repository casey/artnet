todo
----

- [x] fetch:      grab raw data from artscene.textfiles.com
- [ ] extract:    grab the folders of interest
- [ ] clean:      remove anything that isn't an archive
- [ ] unpack:     unpack all archives
- [ ] tidy:       remove anything that isn't 80 column cp 437 with
                  recognized color escape sequences
- [ ] sort:       move files into some kind of orderly heirarchy
                  sorted by group, year, color vs no color, ascii only
                  vs code page 437
- [ ] tokenize:   map multi-byte escape sequences to braille or a
                  unicode private use area
- [ ] render:     write something which will print them to the terminal
- [ ] compile:    turn into fixed-size training data sets
- [ ] preprocess: torch-rnn preprocessing step
- [ ] train:      train (tweak parameters)
- [ ] sample:     take samples (prime with blank line + linefeed?)
- [ ] rasterize:  turn into pngs
