import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(page_title="Baseball Stats", layout="wide")
st.title("Stats Dashboard")
st.header("Gabriel Molina Ramirez")

df = pd.read_csv("QualifiedHittersStats2025.csv")

st.divider()

raw_data, graphs, leaderboards = st.tabs([
    "Overview",
    "Visualization",
    "Leaderboards"
])

with raw_data:
    st.write("MLB Hitting Data")
    st.dataframe(df)
    st.divider()
    st.write("Advanced Stats")
    st.dataframe(df.describe())


with graphs:
    st.write("Batting Average vs Home runs")
    fig1 = px.scatter(df,
                      x="Batting Average",
                      y="Home runs",
                      color="Home runs")
    st.plotly_chart(fig1)
    st.write("Relationship between batting average (Hits / At bats) and home runs")

    st.divider()

    st.write("On-base Percentage(OBP) vs Slugging Percentage(SLG)")
    fig2 = px.scatter(df,
                      x = "OBP",
                      y = "SLG",
                      color = "SLG")
    st.plotly_chart(fig2)
    st.write("Relationship between On-base percentage (how much a batter gets on base) and Slug (total number of bases per at-bat")

    st.divider()

    st.write("Barrel Percentage vs On-base Percentage + Slugging Percentage")
    fig3 = px.scatter(df,
                      x = "Barrel%",
                      y = "OPS",
                      color = "OPS")
    st.plotly_chart(fig3)
    st.write("Relationship between Barrel% (exit velocity >= 98mph and launch angle between 26° and 30°) and OPS")

with leaderboards:
    st.subheader("Leaderboards")

    At_bats = df.sort_values(by=["AB"], ascending=False).head(5)
    fig4 = px.bar(At_bats, x = "Player", y = "AB", title = "Most At-bats")
    st.plotly_chart(fig4)

    hits = df.sort_values(by=["H"], ascending=False).head(5)
    fig5 = px.bar(hits, x = "Player", y = "H", title = "Most Hits")
    st.plotly_chart(fig5)

    home_runs = df.sort_values(by=["HR"], ascending=False).head(5)
    fig6 = px.bar(home_runs, x = "Player", y = "HR", title = "Most Home Runs")
    st.plotly_chart(fig6)

    strikeouts = df.sort_values(by=["SO"], ascending=False).head(5)
    fig7 = px.bar(strikeouts, x = "Player", y = "SO", title = "Most Strikeouts")
    st.plotly_chart(fig7)

    walks = df.sort_values(by=["BB"], ascending=False).head(5)
    fig8 = px.bar(walks, x = "Player", y = "BB", title = "Most Walks")
    st.plotly_chart(fig8)

    strikeout_percentage = df.sort_values(by=["K%"], ascending=False).head(5)
    fig9 = px.bar(strikeout_percentage, x = "Player", y = "K%", title = "Highest Strikeout Percentage")
    st.plotly_chart(fig9)

    walk_percentage = df.sort_values(by=["BB%"], ascending=False).head(5)
    fig10 = px.bar(walk_percentage, x = "Player", y = "BB%", title = "Highest Walks Percentage")
    st.plotly_chart(fig10)

    batting_avg = df.sort_values(by=["AVG"], ascending=False).head(5)
    fig11 = px.bar(batting_avg, x = "Player", y = "AVG", title = "Highest Batting Average")
    st.plotly_chart(fig11)

    slug = df.sort_values(by=["SLG"], ascending=False).head(5)
    fig12 = px.bar(slug, x = "Player", y = "SLG", title = "Highest Slug")
    st.plotly_chart(fig12)

    on_base_percentage = df.sort_values(by=["OBP"], ascending=False).head(5)
    fig13 = px.bar(on_base_percentage, x = "Player", y = "OBP", title = "Highest On-Base Percentage")
    st.plotly_chart(fig13)

    on_base_slug = df.sort_values(by=["OPS"], ascending=False).head(5)
    fig14 = px.bar(on_base_slug, x = "Player", y = "OPS", title = "Highest On-Base + Slug")
    st.plotly_chart(fig14)

    weighted_on_base_avg = df.sort_values(by=["wOBA"], ascending=False).head(5)
    fig15 = px.bar(weighted_on_base_avg, x = "Player", y = "wOBA", title = "Highest Weighted On-Base Average")
    st.plotly_chart(fig15)

    la_sweet_spot_percentage = df.sort_values(by=["LA Sweet-Spot %"], ascending=False).head(5)
    fig16 = px.bar(la_sweet_spot_percentage, x = "Player", y = "LA Sweet-Spot %", title = "Highest LA Sweet-Spot %")
    st.plotly_chart(fig16)

    barrel_percentage = df.sort_values(by=["Barrel%"], ascending=False).head(5)
    fig17 = px.bar(barrel_percentage, x = "Player", y = "Barrel%", title = "Highest Barrel Percentage")
    st.plotly_chart(fig17)

    hard_hit_percentage = df.sort_values(by=["Hard Hit %"], ascending=False).head(5)
    fig18 = px.bar(hard_hit_percentage, x = "Player", y = "Hard Hit %", title = "Highest Hard Hit Percentage")
    st.plotly_chart(fig18)

    whiff_percentage = df.sort_values(by=["Whiff %"], ascending=False).head(5)
    fig19 = px.bar(whiff_percentage, x = "Player", y = "Whiff %", title = "Highest Whiff Percentage")
    st.plotly_chart(fig19)

    swing_percentage = df.sort_values(by=["Swing %"], ascending=False).head(5)
    fig20 = px.bar(swing_percentage, x = "Player", y = "Swing %", title = "Highest Swing Percentage")
    st.plotly_chart(fig20)
    


