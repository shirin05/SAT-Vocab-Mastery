# SAT-Vocab-Mastery
SAT Vocabulary Mastery Platform

### What does it do?

My full stack web app provides multiple choice questions where the student must choose the correct definition and match it to the word provided. Students can customise the level of difficulty they'd like to study at. If struggling with a question, there is a hints section, the student can click on this to view synonyms for the word as a method of helping them figure out the correct answer.

### What problem does this solve?

Looking back when I was studying for the SAT, the apps available were never free. This creates an unfair advantage for students who can afford to pay for those apps. My platform uses a list of almost 300 words, recommended by PrepScholar - a top SAT prep website, and allows students to effectively learn the words in the form of a quiz. This solution increases accessibility and reduces inequality due to financial backgrounds. 

### What did I use to create this?

JavaScript, Python, SQLite, HTML/CSS, NLTK, Flask. Code is extremely well commented throughout.

#### Usage:

python3 app.py in terminal

### What is the thought process behind the user interface?

The user interface strives to embody a sophisticated clean look. Calming colours like gradient navy blues and gentle silver/whites are chosen to optimise the platform for it's purpose - studying. Soothing, slow, and miniature snowflake falling animations are used to keep the students focus and stop them from mentally wandering off. The font is sharp and chosen to harness a polished web page and avoid a cluttered look. Hovering the mouse over any of the buttons gets them to change colour to green, this is done as a user guidance mechanism and to enhance the interactivity of the platform. 

### What are the most relevant errors to be aware of? Also including new things I learnt.
1. Circular imports --> two modules trying to import each other.
2. When working with NLTK for the first time, you need certain downloads / certificates depending on what is already installed.
3. The data from PrepScholar needs a little bit of pruning first so you can easily work with it.
4. If you add extra columns to the csv file, make sure the database file recieves the updates to reflect this.
5. For help with flask refer to this guide --> https://python-adv-web-apps.readthedocs.io/en/latest/flask.html


<img width="1440" alt="Screenshot 2024-08-21 at 14 57 12" src="https://github.com/user-attachments/assets/de2021c9-251c-4549-8ebf-9962192d0529">
<img width="1440" alt="Screenshot 2024-08-21 at 14 57 25" src="https://github.com/user-attachments/assets/b1c8b098-156c-48d1-acb1-1b736a9e70d5">
<img width="1440" alt="Screenshot 2024-08-21 at 14 57 43" src="https://github.com/user-attachments/assets/fe93ac9d-b289-42be-aa06-b49815442c77">







