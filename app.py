from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home_page():
    formatted_string = ''
    string_to_render = ''
    if request.method == 'POST':
        value = request.form.get('format_text')
        string_to_render = request.form['input']
        if value == "U_case":
            formatted_string += string_to_render.upper()
        elif value == "L_case":
            formatted_string += string_to_render.lower()
        elif value == "C_case":
            formatted_string += string_to_render.capitalize()
        elif value == "R_punctuatuons":
            punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
            new_str = ""
            for i in string_to_render:
                if i not in punc:
                    new_str += i
            formatted_string +=new_str
        elif value == "remo_space":
            remo_e_spaces = " ".join(string_to_render.split())
            formatted_string += str(remo_e_spaces)
        elif value == "Wcount":
            formatted_string += str(len(string_to_render.split()))
        elif value == "Lcount":
            formatted_string += str(len(string_to_render))
        
    return render_template('index.html', output = formatted_string, input = string_to_render)


if __name__ == '__main__':
    app.run(debug=True)