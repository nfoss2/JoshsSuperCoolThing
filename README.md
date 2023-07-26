# JoshsSuperCoolThing
This repo is for your (Josh's) hopefully very cool birthday/graduation present. We hope you (Josh) like it!

## Purpose
We hope that this project will help you choose your coffee order each day like Lona used to. Calling `python coffee.py` will output a randomly generated hot or cold coffee order. You can also generate new orders if you don't like the generated order. If you really enjoyed an order you can set it as a favorite to increase the odds that the same order will be generated again (repeatedly favoriting an order will continue to increase the odds of generating an order again).

## Usage
To start a dialog about your coffee order run the following command while in the `JoshsSuperCoolThing` directory.

- `python coffee.py`

To immediately generate a hot or cold coffee run one of the following commands while in the `JoshsSuperCoolThing` directory.

- `python coffee.py -hot`

- `python coffee.py -cold`

To indicate that you enjoyed a particular coffee order run the following command in order to increase the frequency that this order is generated.

- `python coffee.py -favorite "<syrup> <coffeeType>"`

## Contribute
If you feel a syrup flavor is missing or you want to add or remove a coffee type, these changes can be made in `orderProb.json`. You can also manually change the weights given to each type of coffee and syrup if you so desire.


