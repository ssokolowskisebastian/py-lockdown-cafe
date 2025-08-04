from app.errors import VaccineError, NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(cafe: Cafe, friends: list) -> str:
    masks_to_buy = 0
    vaccine_error = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotWearingMaskError as e:
            masks_to_buy += 1
        except VaccineError as e:
            vaccine_error += 1
    if vaccine_error > 0:
        return f"All friends should be vaccinated"
    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"
