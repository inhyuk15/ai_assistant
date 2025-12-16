### pre setting for mac os
```bash
brew install ffmpeg
export DYLD_LIBRARY_PATH=/opt/homebrew/lib:$DYLD_LIBRARY_PATH

python saving_sample.py
python test_whisper.py
```

- To find the real matching "slurp_id" in the saving_sample.py

- check "https://github.com/pswietojanski/slurp"
and this is already downloaded in datafile/dataset.jsonl
### Note: i think this jsonl is quite old.<br> so it misses some slurp_id, not covering all of data.
