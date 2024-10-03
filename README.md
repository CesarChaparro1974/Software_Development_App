# webapppjt
Hello, welcome to the project about car sells advertisements app.
The purpose of this project is to make an app to users can use it and interact with it to decide what car they want to purchase according to their preferences.

# if you want to launch the app on your local machine:
Python libraries are saved in requirements.txt file.
The information about the app's structure is saved on the app.py file which starts the Streamlit app.
To execute the main python file to launch the Streamlit app, use Streamlit run command followed by the path to the main file (Streamlit run app.py).

Prerequisites:
- Python 3.x
- Install dependencies: pip3 install -r requirements.txt
- Run the app: Streamlit run app.py

# libraries
Libraries imported on this project:
- pandas: To be used for data manipulation and analysis.
- streamlit: To build a user-friendly interface for a web application.
- plotly.express: To create visualizations.
- numpy as np: To work with numerical data and its functionalities.

# files
The 2 files that contain the main data for the projects are:
1. EDA.ipynb file which contains the coding for importing the data set, processing the dataset and analysis steps with visualizations.
2. app.py file which contains the code where the app is made. 

# launching the app outside the local machine:
To launch the project follow the next steps:
1. Go to: https://webapppjt.onrender.com/
1a. On the right upper corner you will find settings for the app, I made a custom setting of the page that you can select by clickinig, **custom setting**. It will be dark blue background and different colors.
2. Once you are inside the app you can choose different parameters in order to purchase your car based on your preferences.
3. Move the slider to the desired position or range in order to dislay the results based on your odometer parameter.
4. Since most of the cars are 12.000 km on the data base, to simplify the action there is a clickbox that you can use to display only cars with those km.
5. There is a side bar where you can select type of transmission you prefer to have on your car, by clicking on the option 'manual', 'automatic' or 'other', you can filter the list of models and their prices for each selection.
By 'other' is meant that the transmission can be continuously variable, semi-automatic, etc.
5. Based on your preferences, you can see various visualizations that display each category, or filter you made.
6. In the bottom of the page you can see an outline of the recommended cars based on your paramters.
7. Have a good shopping!

--END OF FILE--
