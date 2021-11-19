# Tkinter-Application

The ojective of this application is to view the life cycle of material and identify what stage a product is in terms of weight and numbers. 
Tkinter and Sqlite3 libraries are used to make the frontend and the backend respectively.

Tkinter is a very useful library to create a windows application. One can automate work by creating basic windows application using python. 

I have created this same project using Flask 
https://github.com/Ameya-Soparkar/Material-Flask-Application

Linkedin link to the video of this application.
https://www.linkedin.com/posts/ameya-soparkar-b12251125_tkinter-python-sqlite3-activity-6785130632944128000-QsTL

Different tabs shows materials at various positions. Processing, Plating, Material Ready are different stages.

1. The first tab allows to add the material name and the weight in the input. Send to Processing button triggers sql command and makes changes in the database. Here we have added material 4 and 100 kg.

![Capture1](https://user-images.githubusercontent.com/65128477/142652788-70b010f0-3128-456f-a46b-e1ff6dac8c7d.PNG)

2. All the other tabs consists the listbox which is available in Tkinter library. It can be made interactive. View all button triggers a sqlite3 querry and it fetches list of tupels as rows. When you select a row in the listbox we can access the information using get method and is displayed in the lable tab. Thus making us easier to read. Send to plating button will make changes in two tables the processing and the plating table. 

![Capture2](https://user-images.githubusercontent.com/65128477/142652792-5765f461-a6c4-4859-916d-0ee34c6e65ea.PNG)

![Capture3](https://user-images.githubusercontent.com/65128477/142652801-309c1035-8468-4725-8548-d4c5e646d353.PNG)

3. By sending 25 kg to plating both the listbox shows the update.
![Capture4](https://user-images.githubusercontent.com/65128477/142652810-1b9f3029-c2ae-4cdf-8d57-c6b1b462864e.PNG)


![Capture5](https://user-images.githubusercontent.com/65128477/142652827-570eeb6a-7360-46fa-916d-52081c489db1.PNG)

4. When the material is send to company it needs to be send as numbers rather than in kgs. So accordingly changes are made in the database based on the numbers of the material send.

![Capture6](https://user-images.githubusercontent.com/65128477/142652847-3280cffe-fa0f-4942-9ce1-74fc23ec12aa.PNG)




