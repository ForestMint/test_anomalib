from anomalib.data import MVTecAD

from anomalib.models import Patchcore

from anomalib.engine import Engine

# Initialize model and data

datamodule = MVTecAD()

model = Patchcore(

    backbone="wide_resnet50_2",

    layers=["layer2", "layer3"],

    coreset_sampling_ratio=0.1

)

# Train using the Engine

engine = Engine()

engine.fit(model=model, datamodule=datamodule)

# Get predictions

predictions = engine.predict(model=model, datamodule=datamodule)