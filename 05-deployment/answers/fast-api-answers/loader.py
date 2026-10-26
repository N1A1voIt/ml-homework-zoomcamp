import pickle
from pathlib import Path
def load_model():
    MODEL_PATH = Path(__file__).with_name("pipeline.bin")
    with MODEL_PATH.open("rb") as model_file:
        pipeline = pickle.load(model_file)
        return pipeline
