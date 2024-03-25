import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# st.set_page_config(layout="wide")  ###########

# st.title("SF Trees")
# st.write(
#     "This app analyses trees in San Francisco using"
#     " a dataset kindly provided by SF DPW"
# )
# trees_df = pd.read_csv("trees.csv")
# # option 1
# # col1, col2, col3 = st.columns((1,1,1))
# # option 2
# # col1, col2, col3 = st.columns((10, 10, 10))
# # option 3
# # col1, col2, col3 = st.columns(3)三个一样


# # first_width = st.number_input("First Width", min_value=1, value=1)
# # second_width = st.number_input("Second Width", min_value=1, value=1)
# # third_width = st.number_input("Third Width", min_value=1, value=1)
# # col1, col2, col3 = st.columns((first_width, second_width, third_width))
# # with col1:
# #     st.write("First column")
# # with col2:
# #     st.write("Second column")
# # with col3:
# #     st.write("Third column")
# # col1.write('First column')
# # col2.write('Second column')
# # col3.write('Third column')

# # df_dbh_grouped = pd.DataFrame(trees_df.groupby(["dbh"]).count()["tree_id"])
# # df_dbh_grouped.columns = ["tree_count"]
# # col1, col2, col3 = st.columns(3)
# # with col1:
# #     st.line_chart(df_dbh_grouped)
# # with col2:
# #     st.bar_chart(df_dbh_grouped)
# # with col3:
# #     st.area_chart(df_dbh_grouped)


# owners = st.sidebar.multiselect("Tree Owner Filter", trees_df["caretaker"].unique())
# if owners:
#     trees_df = trees_df[trees_df["caretaker"].isin(owners)]
# df_dbh_grouped = pd.DataFrame(trees_df.groupby(["dbh"]).count()["tree_id"])
# df_dbh_grouped.columns = ["tree_count"]
# st.line_chart(df_dbh_grouped)


trees_df = pd.read_csv("trees.csv")
trees_df["age"] = (
        pd.to_datetime("today") - pd.to_datetime(trees_df["date"])
    ).dt.days
owners = st.sidebar.multiselect("Tree Owner Filter", trees_df["caretaker"].unique())
st.title("SF Trees")
st.write(
    "This app analyses trees in San Francisco using"
    " a dataset kindly provided by SF DPW. The "
    "histogram below is filtered by tree owner."
)
st.write("The current analysis is of trees owned by {}".format(owners))
graph_color = st.sidebar.color_picker('Graph Colors')
if owners:
    trees_df = trees_df[trees_df["caretaker"].isin(owners)]
df_dbh_grouped = pd.DataFrame(trees_df.groupby(["dbh"]).count()["tree_id"])
df_dbh_grouped.columns = ["tree_count"]
col1, col2 = st.columns(
    2
)  # 上 这第一部分将做以下工作：1。它会加载树的数据集。 2.它根据我们的数据集中的日期列添加了一个年龄列。 3.它在侧边栏上创建一个选择小部件。 4.它根据侧边栏进行过滤。
# st.line_chart(df_dbh_grouped)
# trees_df = trees_df.dropna(subset=["longitude", "latitude"])
# trees_df = trees_df.sample(n=1000, replace=True)
# st.map(trees_df)
with col1:
    st.write("Trees by Width")
    fig_1, ax_1 = plt.subplots()
    ax_1 = sns.histplot(trees_df["dbh"],color=graph_color)
    plt.xlabel("Tree Width")
    st.pyplot(fig_1)
with col2:
    st.write("Trees by Age")

    fig_2, ax_2 = plt.subplots()
    ax_2 = sns.histplot(trees_df["age"])
    plt.xlabel("Age (Days)")
    st.pyplot(fig_2)
st.write("Trees by Location")
trees_df = trees_df.dropna(subset=["longitude", "latitude"])
trees_df = trees_df.sample(n=1000, replace=True)
st.map(trees_df)
