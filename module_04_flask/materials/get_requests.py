import time
import re
from typing import List, Optional

from flask import Flask, request

app = Flask(__name__)


def check_date(input_date: str):
    try:
        valid_date = time.strptime(input_date, '%Y%m%d')
        current_date = time.strftime("%Y:%m:%d", time.localtime())
        if valid_date and time.strftime("%Y:%m:%d", valid_date) < current_date:
            return True
    except:
        return False


def check_element_greater_zero(ids_list):
    for element in ids_list:
        if element < 0:
            return False
    return True


def check_protocols(protocols_list):
    for element in protocols_list:
        if element not in {'2G', '3G', '4G'}:
            return False
    return True


def check_prefixes(prefixes_list):
    for element in prefixes_list:
        pattern = "\d{,10}[*]"
        result = re.fullmatch(pattern=pattern, string=element)
        if not result:
            return False
    return True


@app.route(
    "/search/", methods=["GET"],
)
def search():
    cell_tower_ids: List[int] = request.args.getlist(key="cell_tower_id", type=int)
    if not cell_tower_ids:
        return f"You must specify at least one cell_tower_id", 400
    if not check_element_greater_zero(cell_tower_ids):
        return f"'cell_tower_id' must be integer and greater than 0", 400

    phone_prefixes: List[str] = request.args.getlist(key="phone_prefix")
    if not check_prefixes(phone_prefixes):
        return f"'phone_prefix' must consist of ints and end with an '*' (there must be no more than 10 integers)", 400

    protocols: List[str] = request.args.getlist(key="protocol")
    if not check_protocols(protocols):
        return f"protocols can only be '2G', '3G' and '4G'", 400

    signal_level: Optional[float] = request.args.get(key="signal_level", type=float, default=None)

    input_date_from: str = request.args.get(key="date_from", type=str, default=None)
    input_date_to: str = request.args.get(key="date_to", type=str, default=None)

    if not check_date(input_date_from):
        return f"You must enter the 'date_from' correctly", 400
    if not check_date(input_date_to):
        return f"You must enter the 'date_to' correctly", 400
    if input_date_to < input_date_from:
        return f"You must enter the range of dates correctly", 400

    return (
        f"Search for {cell_tower_ids} cell towers. Search criteria: "
        f"phone_prefixes={phone_prefixes}, "
        f"protocols={protocols}, "
        f"signal_level={signal_level}, "
        f"date_from: {input_date_from}, "
        f"date_to: {input_date_to}"
    )


@app.route("/math/", methods=["GET"])
def operate():
    massive: List[int] = request.args.getlist(key="num", type=int)
    summ = 0
    multiply = 1
    for element in massive:
        summ += element
        multiply *= element
    return f'Сумма чисел: {summ}, произведение чисел: {multiply}'


@app.route("/shuffle/", methods=["GET"])
def zipping():
    massive_1: str = request.args.get(key="massive_1", type=str)
    massive_2: str = request.args.get(key="massive_2", type=str)
    result = set()
    for i in range(len(massive_1)):
        for j in range(len(massive_2)):
            result.add(massive_1[i] + massive_2[j])
    return f'{result}'


# отсортированный массив A и число X, и возвращающий число из массива A, максимально близкое к числу X.
# -323,-111,-6,0,89,114,235,777
# num=77
# my_list = [random.randint(-300, 300) for _ in range(random.randint(6, 12))]
# my_num = random.randint(-300, 300)
@app.route("/nearly/", methods=["GET"])
def near():
    massive: str = request.args.get(key="massive", type=str)
    number: int = request.args.get(key="number", type=int)

    try:
        my_list = sorted(list(map(int, massive.split(','))))
    except:
        return f"Only integer numbers must be entered", 400

    if not isinstance(number, int):
        return f"Number must be integer", 400

    best_index = 0
    diff = number - my_list[best_index]
    for index, element in enumerate(my_list[1:]):
        current_diff = number - my_list[index]
        if abs(current_diff) <= abs(diff):
            diff = current_diff
            best_index = index
        else:
            break
    return f'Число из массива, максимально близкое к числу "{number}": {my_list[best_index]}'


if __name__ == "__main__":
    app.run(debug=True)