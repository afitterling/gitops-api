import yaml
import io
from prettyprinter import cpprint

with open("specs/api_v0.1.yaml", 'r') as stream:
    data_loaded = yaml.safe_load(stream)

cpprint(data_loaded)