from flask import Flask, request, render_template
import anagramssolver

app = Flask(__name__)

@app.route('/')
def home():
 return render_template('home.html')

@app.route('/results')
def results():
 base_word = request.args.get('base word', '')
 num_letters = request.args.get('number of letters', '')
 print(num_letters)

 # run algo here put in base_word and num_letters
 result_set = anagramssolver.main(base_word, num_letters)
 print('result set: ' + str(result_set))
 return render_template('results.html', base_word=base_word, answers=result_set)



# GREET_HTML = """
#  <html><body>
#      <h2>The word {0} can be stolen in these ways!</h2>
#      {1}
#  </body></html>
#  """

if __name__ == "__main__":
 # Launch the Flask dev server
 app.run(host="localhost", debug=True)
