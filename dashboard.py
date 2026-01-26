import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(page_title="Baseball Stats", layout="wide")
st.title("Major League Baseball Stats Dashboard")
st.header("Gabriel Molina Ramirez")

df = pd.read_csv("QualifiedHittersStats2025.csv")


raw_data, graphs, leaderboards = st.tabs([ #intializes sections/tabs of site
    "Overview",
    "Visualization",
    "Leaderboards"
])

with raw_data: #table with all the data
    st.write("MLB Hitting Data")
    st.dataframe(df, height = 750)



with graphs: #scatter plots showing relationships between picked stats
    st.write("Batting Average vs Home runs")
    df['last_name, first_name'] = df['last_name, first_name'].str.split(', ').str[::-1].str.join(' ') #show name as "first last"
    fig1 = px.scatter(df,
                      x="batting_avg",
                      y="home_run",
                      color="home_run",
                      hover_name="last_name, first_name")
    st.plotly_chart(fig1)
    st.caption("Relationship between batting average (Hits / At bats) and home runs")

    st.divider()

    st.write("On-base Percentage(OBP) vs Slugging Percentage(SLG)")
    fig2 = px.scatter(df,
                      x = "on_base_percent",
                      y = "slg_percent",
                      color = "slg_percent",
                      hover_name="last_name, first_name")
    st.plotly_chart(fig2)
    st.caption("Relationship between On-base percentage (how much a batter gets on base) and Slug (total number of bases per at-bat)")

    st.divider()

    st.write("Barrel Percentage vs On-base Percentage + Slugging Percentage")
    fig3 = px.scatter(df,
                      x = "barrel_batted_rate",
                      y = "on_base_plus_slg",
                      color = "on_base_plus_slg",
                      hover_name="last_name, first_name")
    st.plotly_chart(fig3)
    st.caption("Relationship between Barrel% (exit velocity >= 98mph and launch angle between 26° and 30°) and OPS")

with leaderboards: #graphs that show top 5 batters for each stat
    st.write("Leaderboards")
    stat_select = st.selectbox("Stats: ", ["ab","hit","home_run","strikeout","walk", #user selects stat for graph
                                           "k_percent","bb_percent","batting_avg","slg_percent",
                                           "on_base_percent","on_base_plus_slg","woba","sweet_spot_percent",
                                           "barrel_batted_rate","hard_hit_percent","whiff_percent","swing_percent"])

    leaderboard = df.sort_values(stat_select, ascending=False).head(5)
    shades_blue = ['#0a1a2f', '#0f3c73', "#1e63b1", '#4fa3e2', '#a7d8ff'] #range of blue colors, dark to light
    fig4 = px.bar(leaderboard, #each graph uses a different stat
                  x = stat_select,
                  y = "last_name, first_name",
                  title = f"Top 5 in {stat_select}",
                  orientation = 'h') #horizontal bar graph
    fig4.update_traces(texttemplate='%{x}',
                       textposition='outside', #Add stat value to the right of the bars
                       marker_color = shades_blue) #Add color range
    st.plotly_chart(fig4)
    st.markdown(f"""
    - Bar Graph: MLB hitters with the highest/most {stat_select}
    - Darker Blue indicates higher rank""")




