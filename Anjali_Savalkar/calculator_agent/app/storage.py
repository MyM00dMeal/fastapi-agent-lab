

from typing import Dict
calculation_db:Dict[int , dict]={}
current_id=1


def generate_id()->int:
    global current_id
    id=current_id
    current_id+=1
    return id
