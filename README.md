# README

[![CI](https://github.com/BhawickJain/katas.py/actions/workflows/ci.yml/badge.svg)](https://github.com/BhawickJain/katas.py/actions/workflows/ci.yml)

cd
This is a homework assignment completed for a Man Group junior software engineer role.

## Coding Task

__Walkthrough__
 ! I didn't know the algorithm
 | settled on Roulette Selection Method explained by Keith Schwartz
 - basic steps:
 | 1 generate a random number 0,1
 | 2 find the lowest index that bounds the random number
 | 3 return item from `random_nums` array at that index
 - binary search is used to find the index of the culmulative 
 | when an index is greater than or equal to input, keep if smallest, and look for smaller
 | stop when low > high index
 | don't handle situation when `find_index_ceiling` returns -1
 | can't happen if the `probabiltity` array adds to up 1 and PRG is [0,1]
 - design:
 | sane-default: `random.random()` is a default pseudo-random-generate, make testing easier
 | memoization: a culmulative probabiltity array was needed, that is saved an `__init__`
 | classmethod: static methods makes test simpler, and more functional
 - `accurate_enough`:  I noticed that floating approximation error were causing test to fail
 - used exception types to make exceptions easier to read


__Testing Strategy__
 - separated out the deterministic part from the non-deterministic part
 - I assumed `random.random()` is perfect
 - I created a non-random generator function control numbers generated


__What can be improved__
 - real production I have used `numpy.random.choice` or `random.choice`
 - there is a lot of input validation code, a library may have helped here
 - more tests:
 - I don't have any acceptance and integration test.
 - acceptance: time/space complexity performance verification
 - integration: direct non-deterministic 
 - could have written test for helper functions
 - don't handle situation when `find_index_ceiling` returns -1
 - assumptions:
 | my typing assumes an integer array, when an array of any type is permissible
 - my testing does not _feel_  minimal.
 - rogue code:
 | my test imports from `katas`
 | this is my side project which I used boilerplate to run the two files, and left in by accident
 - style:
 | I left in `print(random_number)` which should either be a `DEBUG LOG` or removed
 | unsure my naming of tests, func, vars are pythonic
 | not using LOGGER to raise exceptions with proper log levels


## SQL

__Walkthrough__
 - SQL query steps are split into meaningful intermediate queries
 - Strategy was to reduce the numbers of rows before JOINING
 | as joining is an expensive operation
 - alias names of tables which explicit column names for easier reading

__Testing Strategy__
 - spun up a PostGres Docker image and created query for test data
 - I ran intermediate tables, and check if each stage made sense
 - in production:
 | 1 DBT to write tests
 | 2 caching these intermediate tables

__What can be improved__
 - SQL writing style could be more idiomatic
 - more concise names
 - learn about the costs of each operation
 - potentially a method of poor space complexity; each intermediate is a copy!
 - not written in ORACLE SQL
