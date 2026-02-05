def sort(width: float, height: float, length: float, mass: float):
    """
    Classify a box based on its dimensions and mass and return a status string.

    Classification rules:
    - A box is considered "bulky" if any single dimension is greater than or equal to 150 cm
        or if the volume (width * height * length) is greater than or equal to1,000,000 cm^3.
    - A box is considered "heavy" if `mass` is greater than or equal to 20 kg.
    - If the box is both bulky and heavy, return "REJECTED".
    - If the box is bulky or heavy (but not both), return "SPECIAL".
    - Otherwise return "STANDARD".

    Parameters
    - width, height, length: numeric dimensions (in cm)
    - mass: numeric mass (in kg)

    Returns
    - str: one of "REJECTED", "SPECIAL", or "STANDARD"
    """
    if width <= 0 or height <= 0 or length <= 0 or mass <= 0:
        raise ValueError(f"All inputs must be greater than 0. Inputs: width={width}, height={height}, length={length}, mass={mass}")
    
    bulky, heavy = False, False
    if (width >= 150 or height >= 150 or length >= 150) or (width * height * length >= 1000000):
        bulky = True
    if mass >= 20:
        heavy = True
    if bulky and heavy:
        return "REJECTED"
    elif bulky or heavy:
        return "SPECIAL"
    return "STANDARD"
