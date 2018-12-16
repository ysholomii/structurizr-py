class CodeElementRole(str):
    """
    Used to represent the role of a code element. A component can have one
    primary code element, and zero or more supporting code elements associated
    with it.
    """
    PRIMARY = "primary"
    SUPPORTING = "supporting"
