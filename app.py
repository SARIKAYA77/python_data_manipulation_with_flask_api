from flask import Flask, request

app = Flask(__name__)


@app.route('/resource', methods=['POST'])
def update_text():
    people_count = 0
    people_log = request.json
    response = ""
    for key, value in people_log.items():
        people_in = sum(list(x["value"] for x in value if value[value.index(
            x)]["type"] == "in"))
        people_out = sum(list(x["value"] for x in value if value[value.index(
            x)]["type"] == "out"))
        people_count = (people_in + people_count) - people_out
        response += "{}: {} kişi girdi, {} kişi çıktı, {}\n".format(
            key, people_in, people_out, "mağaza kapandı" if key == list(
                people_log.keys())[-1] and people_count == 0
            else "{} kişi içeride". format(people_count))
    return response


if __name__ == '__main__':
    app.run()
