# Sonic Video Game Sales

Before the turn of the new year, I want to share one data visualization about the sale of the Sonic (the hedgehog) game.  Still using **Streamlit** but there is a little different from the previous one, this time I use a more of custom css styling---not as much as when making (web) applications, of course.


## Dataset

The original dataset can be found at:
[https://www.kaggle.com/gregorut/videogamesales](https://www.kaggle.com/gregorut/videogamesales)

For the sake of this visualization, I've made a few changes and saved it in google spreadsheet format, you can find it at:
[Sonic Video Games Sales](https://docs.google.com/spreadsheets/d/1tESr-18oIksdded9aniQMo2gGCEtOwJWhoQWNdW__Ws/)

## For the file structure:
 - index.py, as the main application to be called  
 - datastream.py, as a link to the data source  
 - styling.py, here I put most of the css styles  
 - vizopt.py, just to simplify writing chart options called in index.py

## For the visualization structure:

- Title  
- Introduction  
- The visualization

For the visualization, there are a few notes. At first, I want to make something like below:
![enter image description here](https://github.com/RFirmansyah/sonic-vg-sales/blob/2261afeac2b191caef10eee6ebb3ba3e875b6fc4/media/initially.png)

but I failed---hahaha---so I did a little workaround and the end result I created a container with 2 columns---I know this might look stupid, but it worked :D 

I didn't explain in detail about the script, it's more or less similar to **[streamlit-uk-exports](https://github.com/RFirmansyah/streamlit-uk-exports)**---in fact it's simpler 

That's all, have a nice holiday and I wish all the best for all of us in the coming new year. 
