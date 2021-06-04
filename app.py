from flask import Flask, render_template, request

import math

app = Flask(__name__)

@app.route("/")
def index():
    # first_number = float(input("Enter first number: "))
    # second_number = float(input("Enter second number: "))
    # third_number = float(input("Enter third number: "))

    # 

    # if(delta < 0):
    #     print("There is no answer with these numbers.")
    # elif(delta == 0):
    #     answer = (-second_number / 2 * first_number) + (math.sqrt(delta) / 2 * first_number)
    #     print(f"answer is: {answer}")
    # else:
    #     answer1 = (-second_number / 2 * first_number) + (math.sqrt(delta) / 2 * first_number)
    #     answer2 = (-second_number / 2 * first_number) - (math.sqrt(delta) / 2 * first_number)
    #     print(f"Answer one is: {answer1}\nAnswer two is: {answer2}")

    return render_template("base.html")
        
@app.route("/answer")
def answer():
    first_number = float(request.args.get("firstNumber"))
    second_number = float(request.args.get("secondNumber"))
    third_number = float(request.args.get("thirdNumber"))

    delta = (second_number ** 2) - (4 * first_number * third_number)

    if(delta < 0):
        answer = ".این معادله جوابی ندارد"
        return render_template("answer.html", answer=answer)
    elif(delta == 0):
        answer = (-second_number / 2 * first_number) + (math.sqrt(delta) / 2 * first_number)
        return render_template("answer.html", answer=answer)
    else:
        answer1 = (-second_number / 2 * first_number) + (math.sqrt(delta) / 2 * first_number)
        answer2 = (-second_number / 2 * first_number) - (math.sqrt(delta) / 2 * first_number)
        return render_template("answer.html", answer1=answer1, answer2=answer2)

if __name__ == "__main":
    app.run(debug=True)
