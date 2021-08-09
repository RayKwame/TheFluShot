# Flu shot acceptance: learning from a previous pandemic

![header image](https://images.unsplash.com/photo-1611689102192-1f6e0e52df0a?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1105&q=80)

Image copyright: Diana Polekhina © unsplash.com

This is the capstone project of the neue fische Data Science Bootcamp. It was a collaborative effort between [Christina Rudolf](https://github.com/christinarudolf), [Raymond Boateng](https://github.com/RayKwame) and [Juliane Berek](https://github.com/julianeberek).


## Introduction

The H1N1 influenza pandemic (also known as swine influenza) was caused by H1N1 influenza virus and affected the world between June 2009 to August 2010 (according to WHO declaration). It was the most recent pandemic prior to COVID19. An estimated 11 - 21% of the global population was affected, with deaths in the U.S. totalling 12,469.

This project aimed to:
- Help to increase vaccination rates for seasonal and pandemic flu in the overall population (this reducing the burden of influenza by decreasing hospitalisations/ deaths)
- Identify factors that determine the chance of getting vaccinated
- Identify groups with lower likelihood for getting vaccinated, in order to target them with promotions
- Determine differences of seasonal vs. H1N1 (pandemic) vaccinations


## Description of dataset

The original data was collected through the National 2009 H1N1 Flu Survey in the U.S. between 2009 - 2010. The current dataset formed part of the DrivenData Challenge ["Flu Shot Learning: Predict H1N1 and Seasonal Flu Vaccines"](https://www.drivendata.org/competitions/66/flu-shot-learning/).

The dataset consists of approximately 27 000 participant responses. The main outcome variables in the dataset:
- whether the participant received the vaccination against the H1N1 flu
- whether the participant received the vaccination against the seasonal flu

The remainder of the dataset consists of [35 categorical variables](https://www.drivendata.org/competitions/66/flu-shot-learning/page/211/), broadly falling into participant demographics, attitudes and knowledge about H1N1 and seasonal flu and vaccination, and healthcare information.

## Hypotheses

We had two main hypotheses we intended to address in our project:

- Some features affect the likelihood of vaccination more than others, e.g. attitudes and knowledge, recommendations by doctors
- H1N1 vaccination is taken more due to the pandemic context 

## Main findings

The main factors related to pandemic response have been visualised in our [dashboard](http://flushot-dashboard.herokuapp.com/).

## Tools and packages used

- Pandas
- Numpy
- Plotly/ Dash 
- Heroku
- SciKit-Learn
- MLFlow
- Random Forest
- ELI5
- Permutation importance
- SHAP
