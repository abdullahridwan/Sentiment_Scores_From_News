from vaderFile import sentiment_scores
from GNews import get_search, clear_search
import streamlit as st
import pandas as pd
import datetime


#period, start_date, end_date, target)

st.markdown("# Let's choose a topic!")
start_date = st.date_input("Start Date for Search",  datetime.date(2019, 7, 6))
start_time = start_date.strftime("%m/%d/%Y")

end_date = st.date_input("End Date for Search",  datetime.date(2019, 7, 6))
end_time = end_date.strftime("%m/%d/%Y")

target = st.text_input("Type in something youre interested in!", "None")

#@st.cache

st.markdown("# Let's see the results!")
titles, links = get_search(start_time, end_time, target)
scores = [sentiment_scores(title) for title in titles]
all_info = {
    "Titles": titles,
    "Scores": scores,
    "Links": links
}
df = pd.DataFrame(all_info)

st.markdown("## Total Counts")
diff_counts = df["Scores"].value_counts()
st.write(diff_counts)
st.bar_chart(diff_counts)


st.markdown("## Data")
option = st.radio(
"Choose a sentiment",
('Positive', 'Negative', 'Neutral'))
new_df = df[df['Scores']==option]
st.dataframe(new_df)

#sentiment_scores("i hate apples")
