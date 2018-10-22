def cal_speeding_ticket(speed, limit):
    if speed <= limit:
        return 0

    percentage = (speed - limit) / speed

    if percentage <= .1:
        return 50
    elif percentage <= .25:
        return 150
    elif percentage <= 1:
        return 400
    else:
        return 2500