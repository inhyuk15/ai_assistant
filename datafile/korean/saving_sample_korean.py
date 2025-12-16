from datasets import load_dataset
import soundfile as sf

dataset = load_dataset("Bingsu/zeroth-korean", split='train')
print(f"Samples: {len(dataset)}")

# print(dir(dataset))
# print(type(dataset[0]))

sample = dataset[0]

if 'audio' in sample:
    print(sample['text'])
    sf.write('zeroth_test.wav', sample['audio']['array'], sample['audio']['sampling_rate'])