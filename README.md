# CSC 360 (in progress)

Wyatt Walsh         @WW-CSC

Martiniano Montero  @MartiMontero

Jeronimo Augurusa   @Scopexx0

## Instructions for downloading

Clone the proyect

```
git clone https://github.com/Scopexx0/CSC-360.git

git checkout -b not_main
```

Create virtual environment (windows) (CMD)
```
C:/>python -m venv c:/pathtothevenv
C:/>c:/pathtothevenv/scripts/activate.bat
```

Create virtual environment (Linux)
```
python3 -m venv venv
source venv/bin/activate
```

Download the libraries
```
pip install -r requirements.txt
```

### THIS IS A TEST

This project aims to design a simple yet effective
application that allows students and faculty to effectively plan their meals for up to a week.
The application will allow users to choose how many meals they wish to plan for, this could
be from a single meal on a day or up to a week in advance. When the user has selected how
many meals they are planning they will be asked about any dietary requirements that they
might have. Then they will be asked if they have any nutritional goals that they are aiming
for, for example, total calories. This program will inform users that it is not a weight loss
program and doesn’t guarantee any changes. Once a user has selected the number of meals to
plan for and any goals, they will begin building meals from foods available at meal times. If a
user selects an item that is against their dietary requirements or goal they will be notified by a
warning message but will still be able to put that item on their plate. If the user doesn’t know
what they want then the program will provide options for the user to meet their requirements
or suggest an entire meal if they haven’t selected any items. Once a user has completed
selecting their meal/meals then they will be shown the nutritional breakdown of their
meal/meals in a list with a total for major food nutrient groups as well as the calorie count.
This will be complemented by a pie chart that will provide a visual representation of the
totals of all of the nutrients. An option to show each meal's nutrients and calorie count
separately will be available if the user chooses more than one meal to plan.
