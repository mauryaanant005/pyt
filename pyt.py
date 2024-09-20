import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from pathlib import Path
import feedparser
import os

# Load dataset
dataset = pd.read_csv("t20_wc.csv")

def load_css():
    css_file = Path("styles.css")
    if css_file.exists():
        with open(css_file, "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load CSS
load_css()


# Create a navbar using streamlit-option-menu
# st.markdown(
#     """
#     <style>
#     .nav {
#         width: 100%; /* Adjust this value to set the navbar width */
#         height: 100px;
#     }
#     .nav-item {
#         flex-grow: 1; /* Distributes the menu items evenly across the navbar */
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# Your option menu with horizontal orientation
selected = option_menu(
    menu_title=None,
    options=["Home", "Quiz", "Search", "CricSet", "About", "Contact"],
    icons=["house", "clipboard", "check-circle", "envelope","phone"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    # styles={
    #     "container": {"padding": "0!important", "background-color": "#f0f2f6"},
    #     "nav-link": {"font-size": "16px", "text-align": "center", "margin": "0px", "--hover-color": "#eee"},
    #     "nav-link-selected": {"background-color": "#afafda"},
    # }
)

# Load the dataset once and store it in session state
if 'df' not in st.session_state:
    st.session_state['df'] = pd.read_csv('mens_t20_world_cup_quiz.csv')

# Show content based on selection
if selected == "Home":
    
   st.title(" ✨ Welcome to Our page ✨")
   st.markdown("---------")
   video_url = "video.mp4"
   st.image(["img30.jpg"])
   st.markdown("INDIA ARE T20 WORLD CHAMPIONS 🏆 AFTER 17 YEARS! It's been a long, long wait for India and they now join West Indies and England as the only three teams to have won the Men's T20 World Cup two times. You really couldn't ask for more, what a grand finale we have had here in Barbados and both sides gave it their all! The Indian players are up in ecstasy and the playing field is flooded by the dugout. The crowd is at the top of its lungs and it's another heartbreak for South Africa, they simply couldn't get it done. Rohit Sharma is down in tears, as he was after the 2023 World Cup final - but this time, these are tears of joy. You really have to hand it to the Indian side, they were down and out but what redemption this is for the Men in Blue.")
   
   st.image(["img2.jpg"])
   st.markdown(
        "The ICC Men's T20 World Cup (formerly the ICC World Twenty20) is the Twenty20 International cricket tournament, organised by the International Cricket Council (ICC) since 2007. The event has generally been held every two years. In May 2016, the ICC put forward the idea of having a tournament in 2018, with South Africa being the possible host,[2] but the ICC later dropped the idea of a 2018 edition at the conclusion of the 2017 ICC Champions Trophy.[3] The 2020 edition of the tournament was scheduled to take place but due to the COVID-19 pandemic, the tournament was postponed until 2021, with the intended host changed to India. The 2021 ICC Men's T20 World Cup was later relocated to the United Arab Emirates (UAE) and Oman[4] due to problems relating to the COVID-19 pandemic in India, taking place 5 years after the previous (2016) iteration."
    )
   st.image(["img10.jpg"])
   st.markdown(
        "The International Cricket Council's executive committee votes for the hosts of the tournament after examining bids from the nations which have expressed an interest in holding the event. After South Africa in 2007, the tournament was hosted by England, the West Indies and Sri Lanka in 2009, 2010 and 2012 respectively. Bangladesh hosted the tournament in 2014.[38] India hosted the tournament in 2016. After a gap of five years, India won the hosting rights of 2021 edition as well, but due to COVID-19 pandemic the matches were played in Oman and the United Arab Emirates."
    )
   st.video(video_url, start_time=0)
   st.markdown("The ICC Men's T20 World Cup (formerly the ICC World Twenty20) is the Twenty20 International cricket tournament, organised by the International Cricket Council (ICC) since 2007.")
    
   st.markdown("""
<hr style="border: 1px solid #ddd;">
<div style="text-align: center; font-size: 14px; color: #000;">
    <p>&copy; 2024 Your Company Name. All rights reserved.</p>
    <p><a href="https://www.yourcompany.com" target="_blank">Visit our website</a> | <a href="https://www.yourcompany.com/privacy" target="_blank">Privacy Policy</a> | <a href="https://www.yourcompany.com/terms" target="_blank">Terms of Service</a></p>
    <p>Follow us on: <a href="https://twitter.com/yourcompany" target="_blank">Twitter</a> | <a href="https://linkedin.com/company/yourcompany" target="_blank">LinkedIn</a></p>
    <p>Contact us: <a href="mailto:support@yourcompany.com">support@yourcompany.com</a></p>
</div>
""", unsafe_allow_html=True)
   
elif selected == "Quiz":
          if 'df' not in st.session_state:
           st.session_state['df'] = pd.read_csv('t20_wc.csv')
           st.markdown("""
             <style>
             /* Global styles */
             body {
                 font-family: 'Arial', sans-serif;
                 background-color: #f4f4f4;
                 color: #333;
             }
             
             /* Margin and padding for the Streamlit app */
             .stApp {
                 margin: 20px;
             }
         
             /* Custom button styles */
             .stButton button {
                 background-color: #AFAFDA;
                 color: white;
                 border: none;
                 padding: 10px 20px;
                 text-align: center;
                 text-decoration: none;
                 font-size: 16px;
                 margin: 4px 2px;
                 cursor: pointer;
                 border-radius: 4px;
                 transition: background-color 0.3s ease;
             }
         
             /* Button hover effect */
             .stButton button:hover {
                 background-color: white;
                 color: #AFAFDA;
                 border: 2px solid #AFAFDA;
             }
         
             /* Markdown content styling */
             .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
                 color: #333;
                 font-family: 'Arial', sans-serif;
             }
         
             .stMarkdown h1 {
                 font-size: 24px;
                 border-bottom: 2px solid #4CAF50;
                 padding-bottom: 10px;
                 margin-bottom: 20px;
             }
         
             .stMarkdown h2 {
                 font-size: 20px;
                 margin-bottom: 10px;
             }
         
             .stMarkdown h3 {
                 font-size: 18px;
                 margin-bottom: 10px;
             }
         
             .stMarkdown p {
                 font-size: 16px;
                 margin-bottom: 10px;
                 line-height: 1.6;
             }
         
             /* Custom selectbox styles */
             .stSelectbox select {
                 background-color: #fff;
                 border: 1px solid #ddd;
                 border-radius: 4px;
                 padding: 10px;
                 font-size: 16px;
                 transition: border-color 0.3s ease;
             }
         
             .stSelectbox select:hover {
                 border-color: #aaa;
             }
         
             /* Custom radio button styles */
             .stRadio div {
                 margin-bottom: 10px;
                 padding: 5px;
             }
         
             /* Write section styles */
             .stWrite {
                 font-size: 18px;
                 line-height: 1.6;
                 margin-top: 20px;
                 color: #333;
             }
             </style>
""",          unsafe_allow_html=True)
         
            
   #          Initialize quiz function
          def initialize_quiz():
             st.session_state['question_index'] = 0
             st.session_state['score'] = 0
             st.session_state['selected_answer'] = None
             st.session_state['questions'] = st.session_state['df'].sample(n=min(len(st.session_state['df']), 10)).reset_index(drop=True)
             st.session_state['user_answers'] = []
         
   #       Function to handle next question
          def next_question():
             correct_answer = st.session_state['questions'].loc[st.session_state['question_index'], 'Answer']
             if st.session_state['selected_answer'] == correct_answer:
                 st.session_state['score'] += 1
             st.session_state['user_answers'].append({
                 'question': st.session_state['questions'].loc[st.session_state['question_index'], 'Question'],
                 'user_answer': st.session_state['selected_answer'],
                 'correct_answer': correct_answer
             })
             st.session_state['question_index'] += 1
             st.session_state['selected_answer'] = None  # Reset selection for the next question
         
   #       Function to display each question with multiple choice options
          def display_question():
             question = st.session_state['questions'].loc[st.session_state['question_index'], 'Question']
             options = [st.session_state['questions'].loc[st.session_state['question_index'], f'Option {i}'] for i in range(1, 5)]
         
             st.markdown(f"*Question {st.session_state['question_index'] + 1}:* {question}")
         
             # Use selectbox for the options
             st.session_state['selected_answer'] = st.selectbox(
                 "Select your answer:",
                 ["Select an answer"] + options,  # Add a default option
                 index=0
             )
         
             # Disable the next button until a valid answer is selected
             if st.session_state['selected_answer'] != "Select an answer":
                 if st.button("Next"):
                     next_question()
         
   #       Function to display the quiz results
          def display_results():
             st.write(f"Quiz Completed! Your score: {st.session_state['score']} out of {len(st.session_state['questions'])}.")
             st.write("### Your Answers and Correct Answers:")
             for answer in st.session_state['user_answers']:
                 st.write(f"*Question:* {answer['question']}")
                 st.write(f"*Your Answer:* {answer['user_answer']}")
                 st.write(f"*Correct Answer:* {answer['correct_answer']}")
                 st.write("---")
         
   #       Main section
          if 'question_index' not in st.session_state or st.session_state.get('restart_quiz', False):
             initialize_quiz()
             st.session_state['restart_quiz'] = False
         
          if st.session_state['question_index'] < len(st.session_state['questions']):
             display_question()
          else:
             display_results()
         
          if st.button("Restart Quiz"):
             st.session_state['restart_quiz'] = True
             st.experimental_rerun()

elif selected == "Search":
    st.title("Search records")
    player_name = st.text_input("Enter the player name")
    if player_name:
        results = dataset[dataset['Player Of The Match'] == player_name]
        if not results.empty:
            st.write(results)

    team_name = st.text_input("Enter the team name")
    if team_name:
        results = dataset[dataset['Winner Team'] == team_name]
        if not results.empty:
            st.write(results[['Result', 'Venue']])

    match_bw = st.text_input("Enter the team names")
    if match_bw:
        between = dataset[dataset['Match Between'] == match_bw]
        if not between.empty:
            st.write(between[['Winner Team', 'Winning Team Score', 'Losing Team', 'Losing Team Score']])
        else:
            st.write("No results found for the entered team names.")

    date = st.text_input("Enter the date of the match")
    if date:
        time = dataset[dataset['Date'] == date]
        if not time.empty:
            st.write(time[['Match Between', 'Winner Team', 'Losing Team','Group/Semi Final/Final']])

elif selected == "CricSet":

    def fetch_rss_feed(url):
        try:
            feed = feedparser.parse(url)
            if feed.bozo == 1:  # bozo indicates there's a problem parsing the feed
                st.error(f"Failed to parse feed: {feed.bozo_exception}")
                return None
            return feed
        except Exception as e:
            st.error(f"Error fetching the RSS feed: {str(e)}")
            return None
    
    # RSS feed for live scorecards
    rss_url1 = "https://static.cricinfo.com/rss/livescores.xml"
    
    # Fetch and display match scorecards
    st.title("Match Scorecards")
    feed = fetch_rss_feed(rss_url1)
    
    if feed:
        for entry in feed.entries[:11]:  # Limit to 5 entries
            st.subheader(entry.title)
            
            # Display summary if available
            if 'summary' in entry:
                st.write(entry.summary)
            
            # Display link to full scorecard
            st.write(f"[Read more]({entry.link})")
            st.markdown("---")
    else:
        st.write("No scorecards available at the moment.")
    
    
    # RSS feed for latest cricket news
    rss_url2 = "https://sportstar.thehindu.com/cricket/feeder/default.rss"
    
    # Fetch and display cricket news
    st.title("Latest Cricket News")
    feed = fetch_rss_feed(rss_url2)
    
    if feed:
        for entry in feed.entries[:15]:  # Limit to 10 latest news
            # Display title and description
            st.subheader(entry.title)
            
            if 'description' in entry:
                st.write(entry.description)
    
            # Check for media content (image or thumbnail)
            cover_image_url = None
            if hasattr(entry, 'media_content'):
                cover_image_url = entry.media_content[0].get('url')  # Media content image
            elif hasattr(entry, 'media_thumbnail'):
                cover_image_url = entry.media_thumbnail[0].get('url')  # Thumbnail image
    
            # Display cover image if available
            if cover_image_url:
                st.image(cover_image_url, use_column_width=True)
    
            # Display summary and link to full story
            st.write(f"[Read more]({entry.link})")
            st.markdown("---")
    else:
            st.write("No cricket news available at the moment.")

elif selected == "About":
   st.subheader("This website provides a detailed analysis of the T20 World Cup from 2007 to 2021. It offers comprehensive records for each World Cup, represented through various plots such as bar plots, pie plots, histograms, scatter plots, and line plots. We utilized powerful Python libraries, including NumPy for numerical operations, pandas for data manipulation, matplotlib for plotting, and Streamlit for creating interactive web applications. Additionally, the site includes interactive features that allow users to filter and explore the data in more depth.")
   st.markdown("---")
   st.write("We offer insights, statistics, and historical data about the tournament and its key moments.")
   st.markdown("Location : Mumbai 🗺️")
   st.header("Our Team")
       
           # Contact details of the team members
   st.subheader("Anant Maurya")
   st.markdown("""
           - **GitHub Profile:** [mauryaanant005](https://github.com/mauryaanant005)        
           - **Role:** Full Stack Developer
           """)
       
   st.subheader("Anas Malkani")
   st.markdown("""
           - **GitHub Profile:** [ANASMALKANI189](https://github.com/ANASMALKANI189)
           - **Role:** Data Scientist
           """)
       
   st.subheader("Rayyan Bhati")
   st.markdown("""
           - **GitHub Profile:** [RAYYAN2906](https://github.com/RAYYAN2906)
           - **Role:** Developer
           """)
       
   st.subheader("Manas Londhe")
   st.markdown("""
           - **GitHub Profile:** [GamerMANAS09](https://github.com/GamerMANAS09)
           - **Role:** Developer
           """)

  
   



elif selected == "Contact":
       st.markdown("""
        <style>
        body {
            background-color: #f5f5f5;
            font-family: 'Arial', sans-serif;
        }
        # .form-container {
        #     background-color: #ffffff;
        #     padding: 20px;
        #     border-radius: 10px;
        #     box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        #     width: 80%;
        #     margin: auto;
        # }
        .form-title {
            color: black;
            font-size: 24px;
            font-weight: bold;
            text-align: center;
        }
        .submit-btn {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
        }
        .submit-btn:hover {
            background-color: #45a049;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Main content
       st.markdown("<div class='form-container'>", unsafe_allow_html=True)
    
       st.markdown("<div class='form-title'>Feedback & Data Collection Form</div>", unsafe_allow_html=True)
       
       # CSV file to store the data
       csv_file = 'feedback_data.csv'
       
       # Form with custom widgets
       with st.form(key='data_form'):
           # Text input for name
           name = st.text_input("What's your name?")
       
           # Slider for rating the experience
           experience_rating = st.slider("Rate your experience with our platform", min_value=1, max_value=10)
       
           # File upload (e.g., upload a feedback document or image)
           uploaded_file = st.file_uploader("Upload a file (optional)")
       
           # Text area for additional comments
           comments = st.text_area("Any additional comments?")
       
           # Submit button
           submit_button = st.form_submit_button(label="Submit", help="Submit your responses")
       
       if submit_button:
           st.markdown(f"### Thank you for your feedback, {name}!")
           st.markdown(f"Your experience rating: **{experience_rating} / 10**")
           st.markdown(f"Additional Comments: **{comments}**")
       
           # Save data to CSV file
           if not os.path.exists(csv_file):
               # Create file with headers if it doesn't exist
               with open(csv_file, 'w') as f:
                   f.write('Name,Experience Rating,Comments,Uploaded File\n')
       
           with open(csv_file, 'a') as f:
               file_name = uploaded_file.name if uploaded_file is not None else "No file"
               f.write(f'{name},{experience_rating},{comments},{file_name}\n')
               st.markdown("### Your responses have been saved!")
       
           if uploaded_file is not None:
               st.markdown("Uploaded File:")
               st.write(uploaded_file.name)
       else:
           st.markdown("Fill out the form and submit your feedback.")
    
           st.markdown("</div>", unsafe_allow_html=True)
           st.markdown("---")
    
