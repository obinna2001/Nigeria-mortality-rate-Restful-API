from pydantic import BaseModel
from typing import List, Dict

class Summary(BaseModel):
    TotalColumnsAndRows : List[Dict]
    PercentageOfMissingValuesByColumns : List[Dict]

    CategoricalColumnSummaries : List[Dict]
    NumericalColumnSummaries : List[Dict]

# output = Summary.model_validate(
#     {
#         "TotalColumnsAndRows": shape,
#         # "PercentageOfMissingValuesByColumns": percentagemissing_dict
#     }
# ).model_dump_json(indent=4)