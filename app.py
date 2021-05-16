# Core pkgs
import streamlit as st
import streamlit.components.v1 as stc

# Import Our Mini Apps
from eda_app import run_eda_app
from ml_app import run_ml_app



html_temp = """
		<div style="background-color:#3872fb;padding:10px;border-radius:10px">
		<h1 style="color:white;text-align:center;">Early Stage DM Risk Data App </h1>
		<h4 style="color:white;text-align:center;">Diabetes </h4>
		</div>
		"""
 
desc_temp = """
			### Early Stage Diabetes Risk Predictor App
			This dataset contains the sign and symptoms data of newly diabetic or would be diabetic patient.
			#### Veri Kaynağı
				- https://archive.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction+dataset.
			#### Uygulama İçeriği
				- EDA Section: Exploratory Data Analysis of Data
				  - EDA-Keşfedici Veri Analizi
				- ML Section: Machine Learning Predictor App
				  - ML-Makine Öğretisi

			"""



def main():
	# st.title("Early Stage DM Risk Data App (DEMO)")
	st.title("Diyabet Risk Tespit Aplikasyonu (DEMO)")
	st.caption("Mevcut uygulama tanı amaçlı değildir. Teşhis için lütfen doktorunuza başvurunuz.")
	# stc.html(html_temp)
	st.sidebar.image('togaylogogri.jpg')


	menu = ["Ana","EDA-Keşfedici Veri Analizi","ML-Makine Öğretisi","Hakkında"]
	choice = st.sidebar.selectbox("Menu", menu)

	if choice == "Ana":
		st.subheader("Ana")
		st.write(desc_temp)

	elif choice == "EDA-Keşfedici Veri Analizi":
		run_eda_app()

	elif choice == "ML-Makine Öğretisi":
		run_ml_app()

	else:
		st.subheader("Hakkında")
		st.text('10-02-2021 - Togay Tunca')






if __name__ == '__main__':
	main()