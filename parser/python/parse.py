import yaml
import io
from prettyprinter import cpprint

with open("specs/0.1/api.yaml", 'r') as stream:
    model = yaml.safe_load(stream)

cpprint(model)

