from flask import Flask, request, render_template
import anagramssolver

app = Flask(__name__)

@app.route('/')
def home():
 return render_template('home.html')

HOME_HTML = """
 <html><body>
     <h2>Welcome to the Anagram Solver!</h2>
     <form action="/greet">
         What word would you like to steal? <input type='text' name='base word'><br>
         How many letters are you willing to add on? <input type='text' name='number of letters'><br>
         <input type='submit' value='Continue'>
     </form>
 </body></html>"""

@app.route('/greet')
def greet():
 base_word = request.args.get('base word', '')
 num_letters = request.args.get('number of letters', '')
 print(num_letters)
 if base_word == '' or num_letters == '':  # if there was no base word given
    base_word = 'Fill out all the info please!'  # you gotta give a base word!
    result_set = 'Please try again!'
    return GREET_HTML.format(base_word, result_set) #CHANEGE THIS

 # run algo here put in base_word and num_letters
 result_set = anagramssolver.main(base_word, num_letters)
 print('result set: ' + str(result_set))
 return render_template('greet.html', base_word=base_word, answers=result_set)



# GREET_HTML = """
#  <html><body>
#      <h2>The word {0} can be stolen in these ways!</h2>
#      {1}
#  </body></html>
#  """

if __name__ == "__main__":
 # Launch the Flask dev server
 app.run(host="localhost", debug=True)
