def study_schedule(permanence_period, target_time):
    try:
        result = 0

        for hours in permanence_period:
            init, end = hours
            if (init <= target_time <= end):
                result += 1
        return result
    except TypeError:
        return None
