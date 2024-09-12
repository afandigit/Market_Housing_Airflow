![sale-sold-hand-signature-c4f2784a22e29601b6011a9e268398ec](https://github.com/afandigit/Market-Housing/assets/106676180/0d9a697a-564c-4dc6-a102-55e689372542)

<h1>Market Housing Project</h1>
<br/>
<hr/>



<h2>Overview</h2>

I am using the Scrapy Framework to scrape datasets from websites offering real estate listings for sales and rentals. The goal is to analyze this data and develop a Machine Learning model that suggests listings to clients based on their preferences and financial capabilities.

This involves extracting relevant features from the listings, such as location, price, property type, and amenities, and using these features to train a recommendation system.

The system will leverage data analysis, data science techniques, and business intelligence to provide personalized and financially feasible real estate options for clients.

This project aims to enhance the user experience and optimize the property search process, ultimately driving better business outcomes for real estate platforms.



<h2>Features</h2>

- Web Scraping : Scrapy Framework. [Done]
- Data Cleaning. [Done]
- Data Analysis - Explore and Visualize data : Python libraries - Microsoft Power BI. [Done]
- MERN Stack. [Current step ...]
- Data Preparation for Machine Learning : Data standardization and preprocessing. [Future step ...]
- Machine Learning. [Future step ...]
- Deploy the trained recommendation model in real time. [Future step ...]



<h2>Dataset</h2>

I have been scraping this dataset using the Scrapy framework for several days, totaling more than 50 hours, from two real estate websites in Morocco (Avito and Mubawab). Each website has its specific Spider. This initial data scraping is to kickstart the data cleaning process, which I plan to automate in the future. My goal is to scale this dataset to include the most common real estate websites worldwide. Currently, the dataset contains over 14,000 records, with each record representing data scraped from an individual real estate ad.

<h3>Dataset description</h3>

<table>
  <thead>
    <tr>
      <th> Column Name </th>
      <th> Description </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>advertisement_url</b></td>
      <td>Which is the full URL of the page in the website on which i retrieve detailed information on the current real estate announcement.</td>
    </tr>
    <tr>
      <td><b>title</b></td>
      <td>The title of the property advertisement.</td>
    </tr>
    <tr>
      <td><b>publication_date</b></td>
      <td>The date the advertisement was published by its owner.</td>
    </tr>
    <tr>
      <td><b>price</b></td>
      <td>The price of the property (in DH = Moroccan DirHam : the official monetary currency of Morocco).</td>
    </tr>
    <tr>
      <td><b>location</b></td>
      <td>The exact location of the property.</td>
    </tr>
    <tr>
      <td><b>description</b></td>
      <td>Detail parts of the property.</td>
    </tr>
    <tr>
      <td><b>complete_description</b></td>
      <td>Complete description of the property established by its owner.</td>
    </tr>
    <tr>
      <td><b>features_list</b></td>
      <td>A liste of The property type (Apartment, House, Villa, farmhouse, ...), property state, number of floors ...</td>
    </tr>
    <tr>
      <td><b>insert_date</b></td>
      <td>The Date the current announcement was scrapped.</td>
    </tr>
  </tbody>
</table>


<h2>Data Cleaning - Using Power BI & Python</h2>
<i>Notice : the powerBI file is available above ...</i>
<img align="right"  width="400" src="https://github.com/afandigit/Market-Housing/assets/106676180/7a45a64d-03f2-4039-9b12-15126ab828eb" alt="cleaning" /> 



<h4>Cleaning Process .... </h4>

1. First step i commit is that i **remove** duplicates records, so as not to distort our analysis in the future. *Because in practice, some people repost their real estate ads multiple times on these websites, causing them to appear multiple times for visitors*.
- Results : we found 3848 duplicate records.
2. Cleaning **advertisement_url** column --> Adding "website_name" column based on current column and Visualizing the number of records per website name.
3. Cleaning **title** column --> Adding three new columns based on the current one and supported by **feature_list** and **price** columns; 'ad_type' column, 'property_type' column and 'property_surface' column + Analyzing all titles by counting the most appeared words + analyzing the new 'property_surface' column.
   1. **Ad_type column** is gonna indicate the type of advertisment; *Sale*, *Rental* or *Vocation Rental*.
      - if you notice bellow in the Analysis part, specificly in the visual which describe the count of words, we found in title or description columns that the ad owner might write the type of ad properly like "rental" or "appartment for sale" but i found a lot of mistake in termes of grammers, so i decide to deeply analyse the title and description ... and after that analysis i create normalize dictionnaries of words for each type that a person might enter.
   2. **property_type column** indicate one of these categories, *Apartments*, *Villas and Riads*, *Houses*, *Rooms*, *Land and Farms*, *Desks*, *Flatsharing*, *Warehouses* or *Other Real Estate*.
      - Sometime the price of rentals real estate expressed as "xxxx DH par jour", "xxxx DH/jour", "xxxx DH/night", "xxxx DH/day" ... so based on the price we could classify the ad as vacation rental category.
   3. **property_surface column** indicate the surface of the property (m²).
      - we check title first, then features list then description for surface format, which is " xxxx m²" or "xxx م". in some cases, the ad owner dont mension the unit "m²" which make it hard for me to scrap it, but after deep analysis i found that these kind of pepole indicate their surface are in feature list in the "Surface habitable" category, for example : "[ ...... ;Âge du bien;Neuf;<b>Surface habitable;55</b>;Étage;4; ....]".
4. Cleaning **publication_date** and **insert_date** column --> Adding year, month, day of publication columns based on current column.
   - sometimes when we start the scrap we encounter some ads that are published in the current day and the publication date is mentionned as "publié aujourd'hui, but while the spider continue scrapping ads, we encounter for some ads that publish day was yesterday or even some couple of days ago or months, so we need to store as well the date of scrap 'insert_date' to calculate later the real date of the publication, which is the diffirence between them."
5. Cleaning **price** column --> adding 'property_price', 'price_currency', 'price per priod (for rental ad)' columns based on the current one.
6. Cleaning **location** column --> i keep this column but i clean it.
    - sometimes i notice that there is some unnecessary details in the location an this is can distort out analysis after, for example some ads have 'Secteur Touristique à Agadir' as location but othors have 'Agadir' and there are the same location but couputer consider them different. so we need to remove the unnecessary details on them.
    - usually ads owners do not spell well the location (city) name well, for example :
     - 'laäyoune' --> 'laayoune'
     - 'asilah' --> 'assilah'
     - 'béni yakhlef' --> 'Ben Yakhlef'
     - etc...
   - so i have created manually a disctionnary to normalize all cities names that are not correctly wrotten by ads owner. then i used a json file which include all cities name in frensh and arabic version, so i can transform all arabic cities name to frensh. 
7. Cleaning **features_list** column --> Adding 'number of rooms' column, cause it is one of the most meaningful insight from this list of property descriptions is: the number of rooms, after what we extract earlier.




<h2>Data Analysis</h2>

* Avito 25.73% higher than Mubawab in terms of records in this dataset. and the most 

<img src="https://github.com/afandigit/Market-Housing/assets/106676180/4e6a8771-a4e2-4c3d-a378-90da1ed2cd31" />

and in term of property type, appartments is the biggest category sold or rent in the Moroccan market. 

<img src="https://github.com/afandigit/Market-Housing/assets/106676180/55152bfc-1718-4657-98ea-0bce946d3be0" />
<br/>
<h3 style="color:red;">Chart Improvement ... </h3>
<br/>
<p>I used the datastorytelling rule to make my graphic capable of conveying the message in less than 5 seconds.</p>
<br/>
<p>Instead of using a Chart Line to compare the number of ads over time, we use the slop graphic, which shows the degree of variation over time in terms of the number of scrapped ads.</p>

<img src="https://github.com/afandigit/Market-Housing/assets/106676180/3ef899eb-e592-4ebc-a3c2-4d1dbe3c7040" />
<br/>
<img src="https://github.com/afandigit/Market-Housing/assets/106676180/ddfb7548-d1df-4b3b-ba2e-71972573bd1c" />

<br/>
* The majority of properties have a surface area between 50 m² and 175 m².
<br/>

<img src="https://github.com/afandigit/Market-Housing/assets/106676180/ca22cafb-6a2b-49f1-8e9e-0d3bd9c687b3" />

* The average room number in this dataset is:
<br/>

<img src="https://github.com/afandigit/Market-Housing/assets/106676180/6c326945-3f2d-4231-b212-786d3f4fbb4e" />

<h3> Dashboard number 1 </h3>
<p> In this dashboard, i compare the statistics measures between the two website Avito and Mubawab, including Max sale of a specific type of real etate, in our case here for <b>apartments</b> per website and per location, but in our case here we just select the max sale of apartments in all Morocco that have the surface betwwen 100 and 200 m².</p>


<img src="https://github.com/afandigit/Market-Housing/assets/106676180/42c5bd84-58c4-4fd2-944d-619c93bd787b" />

<br/>
<p>In Sale category, we notice that Avito is the best market to search for apartement for sale cause of the down average compare to the Mubawab market. and also for the rentals or vacation rentals apartments.</p>

<br/>
<p>BUT !!! if we select <b>agadir</b> apartments that have between 100 and 120 m² in their surface for example, we notice that Mubawab has best prices compares to Avito in terms of Rental or Sales but Avito still good if we wanna rent an apartment for Vacations.</p>
<br/>
<img src="https://private-user-images.githubusercontent.com/106676180/337988846-eaf75bad-793e-419a-9619-eec19bcc63e2.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTc5NDg5MDMsIm5iZiI6MTcxNzk0ODYwMywicGF0aCI6Ii8xMDY2NzYxODAvMzM3OTg4ODQ2LWVhZjc1YmFkLTc5M2UtNDE5YS05NjE5LWVlYzE5YmNjNjNlMi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwNjA5JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDYwOVQxNTU2NDNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0xMThhYzYzZDFhYjk4MTIxNTljODQzNmZiYTZlZjhkOWI1YTA4N2Q4OWNkMzgxYmE1ZWVkZjY2YjdlNDU1MDEwJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.Hf9p_IxR4wtZy3QaLmb_EC8euN0XGFXEmNJn8Q4jdcc" />
<br/><br/>

<h3> Dashboard number 2 </h3>
<p>This dashboard gives you a general idea of the property market in terms of surface area and average room for each type of property in each city.</p>
<br/>
<img src="https://github.com/afandigit/Market-Housing/assets/106676180/d30dab2e-057c-4a4e-aa09-d1ca0e815053"/>

<br/><br/>
<h3> Dashboard number 3 </h3
<p> If I want to invest my money, I can easily choose where and from which platform I can buy for a lower price with the same features. </p>
<img src="https://github.com/afandigit/Market-Housing/assets/106676180/9b7a151b-d49e-4f84-b602-2685839b8f47"/>
<br/>
<h3 style="color:red;">Chart Improvement ... </h3>
<br/>
<p>There's more information than meets the eye in this graphic and the message isn't clear in terms of the price difference between the two platforms so I can decide quickly where I can invest my money.</p>
<br/>
<p>I reduced the noise level and used the data storytelling rule to improve the transmission of messages to the audience in less than 5 seconds.</p>
<h4 style="color:red;"> From this chart </h4>
<br/>
<img src="https://github.com/afandigit/Market-Housing/assets/106676180/dc54e7ef-11d4-4a7e-a78b-1cae9ab4447d"/>
<br/>
<h4 style="color:red;"> To this chart </h4>
<br/>
<img src="https://github.com/afandigit/Market-Housing/assets/106676180/3af10d41-c902-419e-a0b4-a258f95dc147"/>
<br/>
<h4 style="color:red;"> To this chart </h4>
<br/>
<img src="https://github.com/afandigit/Market-Housing/assets/106676180/4f229a78-a647-46ab-bc9b-e19bc2a45505"/>
<br/><br/>
<h3> Dashboard number 4 </h3>
<img src="https://github.com/afandigit/Market-Housing/assets/106676180/a7d40856-9e66-4628-ab16-f19bf99bc77b"/>


<br/><br/>
<h3> Dashboard number 5 </h3>
<img src="https://github.com/afandigit/Market-Housing/assets/106676180/04af35c6-f207-4fe7-a757-71fc0cc64478"/>)


<br/><br/>
<h3> Dashboard number 6 </h3>
<img src="https://github.com/afandigit/Market-Housing/assets/106676180/4ae8f922-1d8a-4a70-b7b0-8277b511d16e"/>


<br/><br/>
<h3> Dashboard number 6 </h3>
<img src="https://github.com/afandigit/Market-Housing/assets/106676180/1800867a-acf6-4748-a5eb-16bd67d67110)"/>

<br/><br/>
<h3> For more details, and if you would like to try out the above dashboards interactively, please download the PowerBI file provided in the files section above ...</h3>

