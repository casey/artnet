todo
----

- [x] fetch:      grab raw data from artscene.textfiles.com
- [ ] extract:    unpack all archives
- [ ] tidy:       remove anything that isn't 80 column cp 437 with
                  recognized color escape sequences
- [ ] sort:       move files into some kind of orderly heirarchy
                  sorted by group, year, color vs no color, ascii only
                  vs code page 437, how much whitespace, how much text,
                  attempt to use heuristics to identify styles
- [ ] tokenize:   map multi-byte escape sequences to braille or a
                  unicode private use area. emit (character,color) pairs
                  train separate neural networks on color and characters
                  and then combine
- [ ] render:     write something which will print them to the terminal
- [ ] compile:    turn into fixed-size training data sets
- [ ] preprocess: torch-rnn preprocessing step
- [ ] train:      train (tweak parameters)
- [ ] sample:     take samples (prime with blank line + linefeed?)
- [ ] rasterize:  turn into pngs

- explore:
  - partial training
  - different paremeters
  - priming
  - alternative color schemes

- add noise for final presentation
- better gallery and presentation for images
