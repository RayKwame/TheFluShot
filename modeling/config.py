import logging
import parsenvy

logger = logging.getLogger(__name__)

# mlflow
# sometimes when saving links in text.. there is a new line .. strip removes that
try:
    TRACKING_URI = open(".mlflow_uri").read().strip()
except:
    TRACKING_URI = parsenvy.str("MLFLOW_URI")

EXPERIMENT_NAME_multilabel = "TheFluShot_multilabel"
EXPERIMENT_NAME_h1n1 = "TheFluShot_H1N1"
EXPERIMENT_NAME_seasonal = "TheFluShot_seasonal"
EXPERIMENT_NAME_multiclass = "TheFluShot_multiclass"