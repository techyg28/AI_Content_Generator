from flask import Flask, render_template, request
import config
import aicontent

def page_not_found(e):
  return render_template('404.html'), 404


app = Flask(__name__) #initializing the web app
app.config.from_object(config.config['development'])
app.register_error_handler(404, page_not_found)


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', **locals())



@app.route('/product-description', methods=["GET", "POST"]) 
def productDescription():

    if request.method == 'POST':
        submission = request.form['productDescription']
        query = "Generate a detailed product description for: {}".format(submission)
        openAIAnswerUnformatted = aicontent.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n','<br>')
        prompt = 'AI Suggestions for {} are:'.format(submission)
        
        # openAIAnswer = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

    return render_template('product-description.html', **locals())



@app.route('/job-description', methods=["GET", "POST"])
def jobDescription():

    if request.method == 'POST':
        submission = request.form['jobDescription']
        query = "Generate a detailed product description for: {}".format(submission)
        openAIAnswerUnformatted = aicontent.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n','<br>')
        prompt = 'AI Suggestions for {} are:'.format(submission)
        # openAIAnswer = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

    return render_template('job-description.html', **locals())



@app.route('/tweet-ideas', methods=["GET", "POST"])
def tweetIdeas():

    if request.method == 'POST':
        submission = request.form['tweetIdeas']
        query = "Generate a detailed product description for: {}".format(submission)
        part1 = aicontent.openAIQuery('Generate a tweet on the subject: {}. \n'.format(submission))
        part2 = aicontent.openAIQuery('Generate twitter hashtags for: {}'.format(submission))
        openAIAnswer = """
        {} {}
        <br>
        {}
        """.format(submission,part1,part2)
        prompt = 'AI Suggestions for {} are:'.format(submission)
        # openAIAnswer = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

    return render_template('tweet-ideas.html', **locals())



@app.route('/cold-emails', methods=["GET", "POST"])
def coldEmails():

    if request.method == 'POST':
        submission = request.form['coldEmails']
        query = "Write a cold email to potential clients about: {}".format(submission)
        openAIAnswerUnformatted = aicontent.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n','<br>')
        prompt = 'AI Suggestions for {} are:'.format(submission)
        # openAIAnswer = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

    return render_template('cold-emails.html', **locals())



@app.route('/social-media', methods=["GET", "POST"])
def socialMedia():

    if request.method == 'POST':
        submission = request.form['socialMedia']
        query = "Generate a Facebook Ad Copy for our product {}".format(submission)
        openAIAnswerUnformatted = aicontent.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n','<br>')
        prompt = 'AI Suggestions for {} are:'.format(submission)
        # openAIAnswer = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

    return render_template('social-media.html', **locals())


@app.route('/business-pitch', methods=["GET", "POST"])
def businessPitch():

    if request.method == 'POST':
        submission = request.form['businessPitch']
        query = "Generate a business idea pitch for: {}".format(submission)
        openAIAnswerUnformatted = aicontent.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n','<br>')
        prompt = 'AI Suggestions for {} are:'.format(submission)
        # openAIAnswer = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

    return render_template('business-pitch.html', **locals())


@app.route('/video-ideas', methods=["GET", "POST"])
def videoIdeas():

    if request.method == 'POST':
        submission = request.form['videoIdeas']
        query = "Generate YouTube Video topic ideas on {}".format(submission)
        openAIAnswer = aicontent.openAIQuery(query)
        # openAIAnswer = openAIAnswerUnformatted.replace('\n','<br>')
        prompt = 'AI Suggestions for {} are:'.format(submission)

        # openAIAnswer = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

    return render_template('video-ideas.html', **locals())


@app.route('/video-description', methods=["GET", "POST"])
def videoDescription():

    if request.method == 'POST':
        submission = request.form['videoDescription']
        query = "Write a detailed Youtube Video description for the following topic {}".format(submission)
        openAIAnswerUnformatted = aicontent.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n','<br>')
        prompt = 'AI Suggestions for {} are:'.format(submission)
        # openAIAnswer = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

    return render_template('video-description.html', **locals())










if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True) # run app in debud mode with port 8888