# import streamlit as st
# import pandas as pd
# import numpy as np

# st.title("SF Trees")
# st.write(
#     "This app analyses trees in San Francisco using"
#     " a dataset kindly provided by SF DPW"
# )
# trees_df = pd.read_csv("trees.csv")
# df_dbh_grouped = pd.DataFrame(trees_df.groupby(["dbh"]).count()["tree_id"])
# df_dbh_grouped.columns = ["tree_count"]
# st.line_chart(df_dbh_grouped)
# df_dbh_grouped["new_col"] = np.random.randn(len(df_dbh_grouped)) * 500
# st.line_chart(df_dbh_grouped)


# import streamlit as st
# import pandas as pd
# import numpy as np

# st.title("SF Trees")
# st.write(
#     "This app analyses trees in San Francisco using"
#     " a dataset kindly provided by SF DPW"
# )
# trees_df = pd.read_csv("trees.csv")
# trees_df = trees_df.dropna(subset=["longitude", "latitude"])
# trees_df = trees_df.sample(n=1000)
# st.map(trees_df)

# import streamlit as st
# import pandas as pd
# import plotly.express as px

# st.title("SF Trees")
# st.write(
#     "This app analyses trees in San Francisco using"
#     " a dataset kindly provided by SF DPW"
# )
# st.subheader("Plotly Chart")
# trees_df = pd.read_csv("trees.csv")
# fig = px.histogram(trees_df["dbh"])
# st.plotly_chart(fig)


# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import datetime as dt

# st.title("SF Trees")
# st.write(
#     "This app analyses trees in San Francisco using"
#     " a dataset kindly provided by SF DPW"
# )
# trees_df = pd.read_csv("trees.csv")
# trees_df["age"] = (pd.to_datetime("today") - pd.to_datetime(trees_df["date"])).dt.days
# st.subheader("Seaborn Chart")
# fig_sb, ax_sb = plt.subplots()
# ax_sb = sns.histplot(trees_df["age"])
# plt.xlabel("Age (Days)")
# st.pyplot(fig_sb)

# st.subheader("Matploblib Chart")
# fig_mpl, ax_mpl = plt.subplots()
# ax_mpl = plt.hist(trees_df["age"])
# plt.xlabel("Age (Days)")
# st.pyplot(fig_mpl)


import streamlit as st
import pandas as pd
from bokeh.plotting import figure
st.title('SF Trees')
st.write('This app analyses trees in San Francisco using'' a dataset kindly provided by SF DPW')
st.subheader('Bokeh Chart')
trees_df = pd.read_csv('trees.csv')
scatterplot = figure(title = 'Bokeh Scatterplot')
scatterplot.scatter(trees_df['dbh'], trees_df['site_order'])
scatterplot.xaxis.axis_label = "dbh"
st.bokeh_chart(scatterplot)

