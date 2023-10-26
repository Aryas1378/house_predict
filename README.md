# house_predict
<br>
<h3>Introduction</h3>
The successful execution of this project hinged on a sequence of pivotal actions, including data loading, feature selection, data partitioning, model construction, model evaluation, and data visualization. The integration of a MongoDB database played a vital role, enabling the storage, retrieval, and representation of data within the program's classes.
<div>
  <br>
</div>
<p align="center">
  <img src="https://github.com/Aryas1378/house_predict/assets/55249095/48aca5ca-cd82-417b-81c8-3ce14483b30d" alt="Your Image">
  <br>
  Figure 1 - A flow chart of the project
</p>
<p>
  <br>
</p>
Flowcharts are visual representations of processes or workflows. The above flow chart can make the sequence of the application for predicting house price more undrestandable. Additionally, a Unified Model Language (UML) can describe the whole structure of the source code and present them in at a glance.
<div>
  <br>
</div>
One the most important requirements in structural programming is Object Oriented Programming (OOP). Regarding to Ali, Shakur and Idris (2017) designing UMLs would be a reliable to show OOP. In UML diagrams the classes can show their relation using lines to connect them together (Figure 2). The cooperation between flow chart and UML can help to find out a general and correct overview about the construction of object oriented programming.

<div>
  <br>
</div>

<p align="center">
  <img src="https://github.com/Aryas1378/house_predict/assets/55249095/48e53355-30b6-44ec-b7b3-36061b1e16ab">
  <br>
  Figure 2 - UML class Diagram
</p>



<h2>The Database</h2>
In this project MongoDB has been used as the database manager to load the csv file to train the model. Using MySQL database could be a bit chalenging for these types of projects as when goes to comparing MongoDB and MySQL, it's essential to consider the strengths of each database system. MongoDB, as a NoSQL database, offers unique advantages that set it apart from MySQL, a traditional relational database. To provide a comprehensive understanding, let's examine the strengths of MongoDB by referencing scientific papers and then outline how these strengths differentiate it from MySQL. Firstly, flexibility and Schema-less, "MongoDB's schema-less allows for the storage of unstructured or evolving data. It provides flexibility to developers to work with data without predefined schema constraints." (Alodib, M., et al. (2017))

<div>
  <br>
</div>

<h2>Building The Programme</h2>

<h3>GUI</h3>
In Python code programming, the next step is to proceed with the implementation of my classes, "Prediction" and "GUI.". Regarding to "GUI" class the following elements are included:
<div>
  <br>
</div>
<h4>Main Window</h4>
<p>The main window displays a background image of a house, enhancing the user interface and is a instance of the "TK" class in python and can make it easier to have graphicial interface for users to interact with the GUI.</p>

<div>
  <br>
</div>

<h4>Input Fields</h4>
<p>The GUI provides input fields for three attributes: square footage of living space (sqft_living), square footage of space above (sqft_above), and square footage of the basement (sqft_basement). Users can input these attributes to make house price predictions and these fields are the same columns which used to train the model to predict which will be discussed by the following.</p>

<div>
  <br>
</div>
<h4>Buttons</h4>
<p>There are 3 buttons in GUI framwork which do diffirent action. Firstlt, <strong>"Predict Price",</strong> which is a button trigger can generate house price prediction process based on user inputs. Secondly, 
<strong> "View Decision Tree", </strong> that users can visualize the decision tree model used for prediction. Finally,
<strong> "View Linear Regression", </strong> is available to allows users to view the linear regression model used for prediction.</p>

<div>
  <br>
</div>
<h4>User Authentication</h4>
The GUI includes a login page with fields for username and password. at the first stage, "create_login_page" is going to make the base frame and then locate the frame in the screen using grid pre-built function to modify the x and y values to locate the elements inside the login form. Afterwards, labels for username and password are defined and finally a submition button for it and if the login is successfull, then the login window gets vanished. Fianlly, the "login" inside the scrpites is responsible for checking the credentials which are provided by the user to wether go throw the main GUI of the application desktop. If the crediantials will not match, a dialog message pops up and informs the user. 
<div>
  <br>
</div>

<h3>Predict</h3>
The House Price Prediction class is developed using Python and leverages several libraries such as Pandas, NumPy, Matplotlib, and Scikit-Learn. It is aimed at training machine learning models to predict house prices based on specific attributes. The class contains the following functions:

<div>
  <br>
</div>

<h4>train</h4>
This function is responsible for training a machine learning model using a provided dataset. It almost focuses on the data which has been retrieved from the MongoDB and then try to split the X and y axis which makes to ready to split data into 4 parts (X_train, X_test, y_train, y_test). Finally, the only two parameters X_train and y_train would return back which could be suitable parameters to train and fit our models.

<div>
  <br>
</div>

<h4>read data</h4>
This method is responsible to make a connection to the MongoDB and get the houses collection from database which contains documents and it would convert to a DataFrame type which makes it compatible for our model to train.using this method can help a lot due to OOP techniques, when some kind script is being used continuesly then it should be converted to a method that is just implemented for once and then could be called anywhere anytime within the other methods in the application.

<div>
  <br>
</div>

<h4>Predict DesicionTree</h4>
By using this method, we can draw an image of our rpedicted decision tree using DecisionTreeRegression. The dataset include numerical data and we are not able to apply classification method on it, so DecisionTreeRegression is the best library to be used to generate the decision tree. Feature selection is a good way to increase the accuracy of the decision tree , as a result, four coloumns( sqft_living, sqft_lot, sqft_above, sqft_basement) were selected to train the X axis of the model. And the y axis goes to the "price" only. Spliting the data would happen in a way that the 80 percent of the whole data is for training and the rest of it belongs to testing. Finally, the method will plot the decision tree and evaluate the model by calculating mean square error(MSE).

<div>
  <br>
</div>

<h4>Predict LinearRegression</h4>
Inside this method, like the Predict DecisionTree, feature selection has been happened tosplit X and y axis. To destribute price coloumn equally "log" has imported from numpy to improve the result. Then, an instance is made from LinearRegression to store in an variable and use it for plotting a scatter plot diagram.

<h4>My Predict Price</h4>
As the program aims to predict the price of a house then this is the method which handle it. There is an arguman for user dataframe which contains the information that the user is looking for then training the regression model would happen by chosing 3 coloumns sqft_living, sqft_above and sqft_basement. Finally, passing user dataframe to predict method can generate the price. Dataset contains nominal values for its columns so it makes it required to have only correlated columns to have a better result instead of overfitting the model by using all the columnsand train the model according them.

<div>
  <br>
</div>

# Running The Program

<p align="centre">
  <div style="text-align: center;">
    <img src="https://github.com/Aryas1378/house_predict/assets/55249095/f360c7a9-47d3-47ee-902c-df52cb4d4136">
  </div>
  <br>
  Figure 3 - Login
</p>

<p align="centre">
  <img src="https://github.com/Aryas1378/house_predict/assets/55249095/27c0a750-dda5-4821-bd68-c851c130bcf6">
  <br>
  Figure X - Scatter Plot
</p>


