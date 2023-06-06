from exceptions import NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError
from datetime import datetime


def data_processing(data: dict):
    if data["titles"] < 0:
        raise NegativeTitlesError("titles cannot be negative")

    data_sent = str(data["first_cup"])
    sliced_data_sent = int(data_sent[0:4])

    year_now = str(datetime.now())
    sliced_year = int(year_now[0:4])

    cup_years = [1930]

    for n in cup_years:
        n = n + 4
        if n < sliced_year:
            cup_years.append(n)

    if sliced_data_sent in cup_years:
        total_cups = len(cup_years)
        index_this_cup = cup_years.index(sliced_data_sent)
        possible_cups = total_cups - index_this_cup - 1

        if data["titles"] > possible_cups:
            raise ImpossibleTitlesError(
                "impossible to have more titles than disputed cups"
            )

    else:
        raise InvalidYearCupError("there was no world cup this year")
