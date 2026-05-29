VALID_TRANSITIONS = {
    "TODO":["IN_PROGRESS"],
    "IN_PROGRESS":["REVIEW"],
    "REVIEW":["IN_PROGRESS","DONE"],
    "DONE":[]
}


def is_valid_transition(current_status,new_status):
    allowed = VALID_TRANSITIONS.get(current_status,[])
    return new_status in allowed