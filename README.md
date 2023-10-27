<b> Welcome to Quiz Master, a fun and interactive quiz game built in Python using the Pygame library Streamlit. </b> 

You can try out the game here =======> https://quiz-master.streamlit.app/ 

<i> This README will provide you with all the information you need to understand the game's objective, rules, technology stack, and setup instructions. </i> 

<b> Game Objective and Rules </b>

The objective of this game is to answer the most questions correctly. Each round will have ten questions that will come from categories and difficulty levels of your choosing. Take your time as you answer the questions. There is no time limit. Above all else, have fun! You have full autonomy over the questions you receive. 
		
<i> Step 1: Select a Category </i>

You will start the game by selecting the category you want your questions to be randomly generated from. These categories could range from Entertainment to Science. Please select a category that would provide the most enjoyable experience for this round. After the game starts, you can change your category if you desire for each question. 

When a category has been selected, the first question and corresponding answer choices will appear. You will have the opportunity to change your category after previewing a question. 

<i> Step 2: Select the Level of Difficulty </i> 

For the best experience, you should select the difficulty level after selecting the category. The first question will default to the easy difficulty level. The levels of difficulty range from Easy to Medium to Hard. Please be sure to pick a level of difficulty that would provide the most enjoyable experience for you. If you change from the default difficulty level, the question will change to reflect the new chosen level. 

----------------------------------------------------------------------------

Please review the question before you submit your answer. When an answer has been submitted, it will count towards your final score. You will not be able to go back and change the difficulty level or category for any previous question. 

Most importantly, challenge yourself and your friends and have fun! Correct answers will be displayed for every wrong answer. At the end of the game, your score will be revealed. To start a new round, please refresh the page. 

<i> <b> Will you be the next Quiz Master? Play this game and find out!  </b> </i> 



<b> Technology Stack </b>

The Quiz-Master game is developed in Python language and uses “Pygame” as its primary library. Pygame is one of the most popular open-source Python libraries that is primarily used for creating 2-D games and other related applications. It provides a convenient and easy-to-use set of functions and tools for developing games, and it is built on top of the SimpleDirectMedia Layer. Several Pygame packages were used in developing the application, which includes random, time and altair. Random package is used to generate random numbers, which is useful for selecting questions at random. The time package is used to control the flow of the game, like delaying the next question until the specified time or till the user answers the question. Altair package is used to create interactive charts, which are used to display player scores and other information about the game.

There are a few other packages used, such as Streamlit, is used for creating the user interface of the game. It allows for easy web app development with Python. Requests package used for making HTTP requests. JSON library is used for encoding and decoding JSON data. Other general libraries like datetime, pandas, numpy, and plotly are used. 

The modules and functions used in the game development are discussed below:

The code begins with import statements to bring in the necessary libraries and packages.

get_category(): This function fetches all the available quiz categories from the Open Trivia Database API and returns them as a dictionary.

get_question(): Based on the selected category and difficulty, it returns a list of questions.

initialize_session_state(): It initializes the game state, which includes the current question index and player score, using Streamlit’s session state.

update_score(): This function compares the player's choice with the correct answer and updates the player's score accordingly. If the player's choice matches the correct answer, the score is incremented. Streamlit components like "st.success" and "st.error" are used to provide feedback to the player

UI Setup: The code sets up the user interface using Streamlit. It allows the user to select a quiz category, difficulty level, and provides options to answer questions and navigate through the quiz.

calculate_score(): This function includes most of the functionality of the application. It calculates the player’s score by comparing their choices with the correct answer and then updates the session. This part has Streamlit’s UI components for creating the game, such as st.title, st.subheader, st.sidebar, st.radio, and st.button. Inside the function, it compares player_choice with correct_answer and decides whether to increase the player's score or not. The updated player score is stored in Streamlit’s session state so that it persists across different questions in the game.

Category Selection: A Streamlit select box allows the user to choose from among the various categories that the code has retrieved.

Selection of Difficulty Level: Using a choose box, the user may select between three difficulty levels: easy, medium, and hard.

Question Fetching: Questions are retrieved from the API based on the chosen category and level of difficulty. The "quiz_questions" list is where these questions are processed and kept.

Question Display: The code controls how questions are shown, letting the player choose their response by pressing a radio button.

Answer Submission: The "calculate_score" function is triggered when the player submits an answer.

Getting Around the Quiz: After submitting an answer, the code shows the next question, allowing players to move around the quiz. The quiz ends and the final score is shown once every question has been answered.



<b> Setup Instructions </b>

👨🏻‍💻 How to run the app? 

Step 1: Clone the repo 

Step 2: Create virtual environment: 'python -m venv ' 

Step 3: Activate the environment: '\Scripts\activate' 

Step 4: Install the dependencies: pip install -r requirements.txt 

step 5: Run it on local host: 'streamlit run QuizMaster.py' 

The Dashboard can be accessed via following link: https://quiz-master.streamlit.app/

<b> Credits & Acknowledgements </b>

Streamlit v1.27.0
https://streamlit.io | Copyright 2023 Snowflake Inc. All rights reserved.

Numpy v1.19.1
https://numpy.org/ | Harris, C.R., Millman, K.J., van der Walt, S.J. et al. Array programming with NumPy. Nature 585, 357–362 (2020). DOI: 10.1038/s41586-020-2649-2. (Publisher link).

Panda v1.2.0
https://pandas.pydata.org/docs/index.html | 2023 pandas via NumFOCUS, Inc. Hosted by OVHcloud.

Plotly v4.9.0
https://plotly.com/graphing-libraries/ | Copyright © 2023 Plotly. All rights reserved.

Requests v2.24.0
https://requests.readthedocs.io/en/latest/ | ©MMXVIX. A Kenneth Reitz Project.

Altair v5
https://altair-viz.github.io/index.html | © Copyright 2016-2023, Vega-Altair Developers.


<b> Reflection from the Project </b>

Throughout the course of our project, we made several decisions, some of which turned out to be effective, while others didn't quite hit the mark. Our journey involved various stages, from initial organization and team management to design and project development. Reflecting on this process, we encountered both challenges and successes that taught us valuable lessons.
First, we recognized the importance of breaking our project into manageable segments, each aligning with our individual expertise. This approach allowed us to efficiently allocate tasks and responsibilities. We aimed to maintain clear communication by scheduling weekly meetings to provide updates and address any issues. However, it wasn't always smooth sailing due to our team member’s differing schedules and commitments. Some of us had different work hours and commitments, making in-person meetings challenging. To overcome this, we heavily relied on digital communication tools like Teams and email to facilitate rescheduling, ensuring everyone was on the same page.

One key decision that worked well for us was choosing GitHub as our collaboration platform. We opted for GitHub because it was a familiar tool to all of us. While our levels of experience with the platform varied, our shared knowledge created a common ground that promoted efficient collaboration. GitHub enabled us to stay updated on each team member's contributions, making it easy to manage the project. To enhance our teamwork and document sharing, we also utilized Google Drive, which proved invaluable as we began crafting our project's readme file. When it came to designing and developing our project, we initially envisioned a setup where players had complete control over the number of questions in each round. However, as we delved deeper into the project and encountered challenges, we realized this might not be the best approach. We still wanted to provide users with autonomy, but we also recognized the importance of delivering a quality product. After discussions and troubleshooting, we made the decision to standardize each round with ten questions. This choice struck a balance between user control and the project's quality. Instead of focusing on the number of questions, we empowered users to choose the difficulty level and category, giving them a sense of ownership over their experience.

Looking back, our journey was marked by its share of successes and setbacks. The challenges of coordinating meetings among a group with varying schedules tested our ability to adapt and rely on digital platforms. While we initially aimed for complete user autonomy in question selection, we learned that sometimes, compromising for the sake of a better project outcome is essential.
One key lesson that emerged from our experience was the value of flexibility and adaptability. In the dynamic world of project development, it's crucial to remain open to change and adjust your approach when necessary. We also learned the importance of leveraging tools and platforms that the team is familiar with to streamline collaboration and ensure a smooth workflow.

Overall, our project's design and development process was a journey of discovery, growth, and adaptation. It demonstrated the significance of effective team communication, embracing familiar tools, and finding a balance between user autonomy and project quality. These lessons will undoubtedly serve us well in future endeavors, as we continue to refine our skills and approaches in the ever-evolving world of project management and development.
