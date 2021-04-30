import streamlit as st



# Load EDA Pkgs
import pandas as pd

# Load Data Viz pkg
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
import plotly.express as px



desc_temp = """
			### This is the area where the insights could e written
			This dataset contains the sign and symptoms data of newly diabetic or would be diabetic patient.
			#### Insights
				- https://archive.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction+dataset.
			#### Action
				- EDA Section: Exploratory Data Analysis of Data
				- ML Section: ML Predictor App

			"""

# Load Data
@st.cache
def load_data(data):
	df = pd.read_csv(data)
	return df

def run_eda_app():
	st.subheader("From Exploratory Data Analysis")
	# df = pd.read_csv("data/diabetes_data_upload.csv")
	df = load_data("data/diabetes_data_upload.csv")
	df_encoded = load_data("data/diabetes_data_upload_clean.csv")
	freq_df = load_data("data/freqdist_of_age_data.csv")
	# st.dataframe(df)

	submenu = st.sidebar.selectbox("Submenu",["Descriptive","Plots"])
	if submenu == "Descriptive":
		st.dataframe(df)

		with st.beta_expander("Data Types"):
			st.dataframe(df.dtypes)

		with st.beta_expander("Descriptive Summary"):
			st.dataframe(df_encoded.describe())

		with st.beta_expander("Class Distribution"):
			st.dataframe(df['class'].value_counts())
			fig = plt.figure()
			sns.countplot(df['class'])
			st.pyplot(fig)

		with st.beta_expander("Gender Distribution"):
			st.dataframe(df['Gender'].value_counts())
			fig = plt.figure()
			sns.countplot(df['Gender'])
			st.pyplot(fig)

	



	elif submenu == "Plots":
		st.subheader("Plots")


		# Layouts
		col1, col2 = st.beta_columns([2,1])


		with col1:
			# Gender Distribution
			with st.beta_expander("Dist Plot of Gender"):
				# Using Seaborn
				fig = plt.figure()
				sns.countplot(df['Gender'])
				st.pyplot(fig)

				gen_df = df['Gender'].value_counts().to_frame()
				gen_df = gen_df.reset_index()
				gen_df.columns = ["Gender Type", "Counts"]
				# st.dataframe(gen_df)

				# Using Plotly Express
				p1 = px.pie(gen_df,names='Gender Type',values="Counts")
				st.plotly_chart(p1,use_container_width = True)

			# For Class Distribution
			with st.beta_expander("Dist Plot of Class"):
				fig = plt.figure()
				sns.countplot(df['class'])
				st.pyplot(fig)




		with col2:
			with st.beta_expander("- Gender Distribution"):
				st.dataframe(gen_df)

			with st.beta_expander("- Class Distribution"):
				# cl_df = df['class'].value_counts().to_frame()
				# st.dataframe(cl_df)
				st.dataframe(df['class'].value_counts())

		# Freq Dist
		with st.beta_expander("Frequency Dist of Age"):
			st.dataframe(freq_df)
			p2 = px.bar(freq_df,x='Age',y='count')
			st.plotly_chart(p2, use_container_width = True)

		# Outlier Detection
		with st.beta_expander("Outlier Detection Plot"):
			fig = plt.figure(figsize=(20,10))
			sns.boxplot(df['Age'])
			st.pyplot(fig)

			p3 = px.box(df,x='Age', color='Gender')
			st.plotly_chart(p3, use_container_width = True)

			st.write(desc_temp)


		# Correlation Plot
		with st.beta_expander("Correlation Plot"):
			corr_matrix = df_encoded.corr()
			fig = plt.figure(figsize=(20,10))
			sns.heatmap(corr_matrix,annot=True)
			st.pyplot(fig)

			p4 = px.imshow(corr_matrix)
			st.plotly_chart(p4)



					


				

























	