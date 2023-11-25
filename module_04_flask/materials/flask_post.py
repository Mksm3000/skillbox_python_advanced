import json
from urllib.parse import unquote_plus

from flask import Flask, request

app = Flask(__name__)


@app.route("/sum", methods=["POST"])
def _sum():
    array1 = request.form.getlist("array1", type=int)
    array2 = request.form.getlist("array2", type=int)

    result = ",".join(str(a1 + a2) for (a1, a2) in zip(array1, array2))

    return f"Array of sums is [{result}]"


@app.route("/sum2", methods=["POST"])
def _sum2():
    form_data = request.get_data(as_text=True)  # важный момент!!!
    request_data = unquote_plus(form_data)  # важный момент!!!

    arrays = {}

    for encoded_chunk in request_data.split("&"):
        key, value = encoded_chunk.split("=")

        arrays[key] = [int(it) for it in value.split(",")]

    result_str = ",".join(
        str(a1 + a2) for a1, a2 in zip(arrays["array1"], arrays["array2"])
    )

    return f"Your result is [{result_str}]"


@app.route("/sum3", methods=["POST"])
def _sum3_json():
    form_data = request.get_data(as_text=True)

    data_object = json.loads(form_data)

    result_str = ",".join(
        str(a1 + a2) for a1, a2 in zip(data_object["array1"], data_object["array2"])
    )

    return f"Your result is [{result_str}]"


@app.route("/shift", methods=["POST"])
def _shift():
    # [1, 2, 3, 5, -8, -6, -1, 0] или [2, 3, 4, 5, 0, 1]
    form_data = request.get_data(as_text=True)
    request_data = unquote_plus(form_data)

    data_string = request_data.split('=')[1]
    data = list(map(int, data_string.split(',')))
    min_value = min(data)
    min_index = int(data.index(min_value))
    shift_data = data[min_index:]+data[:min_index]

    return f"Shift is {min_index}. Shifted list is {shift_data}"


if __name__ == "__main__":
    app.run(debug=True)
