from pydantic import RootModel
from typing import Dict, List

class SexFilters(RootModel[List[Dict]]):
    pass
 
class YearFilter(RootModel[List[Dict]]):
    pass

# # To use filter models the dataframe must be converted to a list of dictionaries using pandas .to_dict(orient='records')  
# df = pd.DataFrame(
#     {
#         'name': ['obinna okey', 'ifeanyi okey', 'Ike ezi'], 
#         'age': [24, 22, 25], 
#         'job': ['AI Analyst Intern', 'Front end developer', 'tECH BRO']
#     }
# )

# df = df.to_dict(orient='records')

# # print(df)
# # filters = Filters.model_validate({'sexcode_filter_result': df}).model_dump_json(indent=4)
# filters = YearFilter.model_validate(df).model_dump_json(indent=4)
# # print(filters)