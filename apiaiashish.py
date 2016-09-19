import os.path
import sys
import json
try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai

CLIENT_ACCESS_TOKEN = 'ACCESSTOKENFOR API>AI'


def main(mytext):
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

    request = ai.text_request()

    request.lang = 'en'  # optional, default value equal 'en'

    # request.session_id = "<SESSION ID, UBIQUE FOR EACH USER>"

    request.query = mytext

    response = request.getresponse()
    string = response.read().decode('utf-8')
    json_obj = json.loads(string)
    return json_obj


if __name__ == '__main__':
    main()
