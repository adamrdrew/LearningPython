# List Comprehensions
These replace methods on Enumerables in Ruby like `each()` or `map()` or `select()`. Comprehensions are Python's way of letting you do stuff with members of iterables or subsets of iterables:

```python
>>> names = ("Berlioz", "Ziggy", "Jonesy")
(Name) for Name in names]>>> [print(Name) for Name in names]
Berlioz
Ziggy
Jonesy
```
Comprehensions can also have conditionals:
```python
>>> [print(Name) for Name in names if Name != "Adam"]
Berlioz
Ziggy
Jonesy
Roddy
```
Comprehensions return lists so they can be used to map, filter, etc:
```python
>>> names = ("Berlioz", "Ziggy", "Jonesy", "Adam", "Roddy")
>>> j = [Name for Name in names if Name != "Adam"]
>>> type(j)
<class 'list'>
>>> print(j)
['Berlioz', 'Ziggy', 'Jonesy', 'Roddy']
```
Now for the good shit: comprehensions can be nested `mindblown.gif`
```python
>>> titles = ("Dr.", "Mr.")
>>> names = ("Berlioz", "Ziggy", "Jonesy", "Adam", "Roddy")
>>> [[Title + " " + Name for Name in names] for Title in titles]
[['Dr. Berlioz', 'Dr. Ziggy', 'Dr. Jonesy', 'Dr. Adam', 'Dr. Roddy'], ['Mr. Berlioz', 'Mr. Ziggy', 'Mr. Jonesy', 'Mr. Adam', 'Mr. Roddy']]
```
From a Ruby background that looks a little *off* to me, but it works. And it's fucking powerful.

Now for the really, really good shit: Combine list comprehension with functions as object:
```python
>>> def Nice(Name):
...     print("Hi " + Name + " nice to meet you!")
...
>>> def Mean(Name):
...     print("Damn " + Name + " I hate you")
...
>>> Greetz = (Nice, Mean)
>>> names = ("Berlioz", "Ziggy", "Jonesy", "Adam", "Roddy")
>>> [[Greet(Name) for Name in names] for Greet in Greetz]
Hi Berlioz nice to meet you!
Hi Ziggy nice to meet you!
Hi Jonesy nice to meet you!
Hi Adam nice to meet you!
Hi Roddy nice to meet you!
Damn Berlioz I hate you
Damn Ziggy I hate you
Damn Jonesy I hate you
Damn Adam I hate you
Damn Roddy I hate you
```
Now that's what the fuck I'm talking about.

