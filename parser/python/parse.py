import yaml
import io
from prettyprinter import cpprint

with open("specs/0.1/api.yaml", 'r') as stream:
    model = yaml.safe_load(stream)

cpprint(model)

version = model.get('version')

kresources = list(model.get('resources').keys())
kmodels = list(model.get('models').keys())
kapis = list(model.get('apis').keys())
kendpoints = list(model.get('endpoints').keys())

cpprint(version)
cpprint('apis: ' + str(kapis))
cpprint('endpoints: ' + str(kendpoints))
cpprint('models: ' + str(kmodels))
cpprint('resources: ' + str(kresources))
