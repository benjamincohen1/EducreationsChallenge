from solver import *
from flask import request,Flask,json,Response
import json

"Imports: Imports solver from other file, as well as necessary Flask components"
app=Flask(__name__) #makes the app
@app.route('/', methods = ['POST']) #tells the app it's looking for posts
def api_echo():
    if request.headers['Content-Type'] == 'application/json':  #makes sure we have valid JSON.  JSON should be in the form {'puzzle' : list[lists of ints]}
            j=json.dumps(request.json) #gets JSON and stores it in J
            goodJSON=json.loads(j) #parses it into python dicts
            l=goodJSON['puzzle'] #sets l to the puzzle 
            answer=solvePuzzle(l) #solves L
            r=json.dumps({'solution' : answer})  #puts the answer in JSON
            resp=Response(r) #makes a response with the answer
            return resp #answers!

if __name__ == '__main__':
    app.run()