import json
import os
os.environ["DATASETS_AUDIO_BACKEND"] = "soundfile"

from datasets import load_dataset
import soundfile as sf

def load_sentence(slurp_id: int) -> str:
    json_data = {}
    with open("dataset.jsonl", encoding="utf-8") as f:
        json_data = {o["slurp_id"]: o["sentence"] for o in map(json.loads, f)}
        
    return json_data[slurp_id]

    

dataset = load_dataset("yhfang/slurp_dataset_audio", split='train')

unique_ids = dataset.unique('slurp_id')
print(len(unique_ids))

sample = dataset[0]

if 'audio' in sample:
    print(f"Sampling rate: {sample['audio']['sampling_rate']}")
    print(f"Array shape: {sample['audio']['array'].shape}")
    slurp_id = sample['slurp_id']
    intent_id = sample['intent']
    
    print(f"slurp_id: {slurp_id}")
    print(f"intent_id: {intent_id}")
    print(f'sentence: {load_sentence(slurp_id)}')
    
    sf.write('slurp_test.wav', sample['audio']['array'], sample['audio']['sampling_rate'])