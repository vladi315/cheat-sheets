## Env management with conda

**Best practices:**

- First install as much as possible with conda, then with pip. Avoid switching between conda and pip.
- Interpreter must be in active environment

List of all installed libraries:
  `conda list oder pip list`

List the history of each change to the current environment
  `conda list --revisions`

Install specific version of package
  `conda install <matplotlib>=<1.4.3>`

Restore environment to a previous revision (change revision number)
  `conda install --revision 2`

Update all conda packages to latest version (drops old constraints and builds new constraints)
  `conda update --all`

Update conda itself      
  `conda update -n base -c defaults conda`

Create new conda environment      
  `conda create --name envname`

Create new conda environment with python x.y   
  `conda create --name envname python=3.7`

Delete conda env      
  `conda remove --name ciaraEnv_transferLearning --all`

Add another channel to conda to search for   
  `conda config --append channels conda-forge`

Activate environment envname
  `activate envname`

See all environments 
  `conda env list`

Update pip      
  `python -m pip install --upgrade pip `

#### handling requirements.txt

Exporting all conda and pip **requirements**   
  `pip list --format=freeze > requirements.txt`

Better alternative for minimal requirements   
  `pipreqs /path/to/project`

Install pip packages from requirements.txt   
  `pip install -r requirements.txt`

## Jupyter     

Installing packages in Jupyter

  ```py
  import sys
  !conda install --prefix {sys.prefix} numpy

  import sys
  !{sys.executable} -m pip install numpy 
```

## Debugging

Inline debugger (ipdb for jupyter pdb for native python):

```py
  !pip install -Uqq ipdb
  import ipdb

  %pdb on
  ipdb.set_trace()  Sets breakpoint
  pp vars(testvar) Get all variables of the object testvar and prettyprint
  pp dir(testvar)  Get the structure of the object testvar and prettyprint
  %pdb off
```

>control with: Continue Step Next Quit Help l(ist) (shows code) unt(il) (Without argument, continue execution until the line with a number greater than the current one is reached.)

## Documentation

##### Docstring format

def add(num1, num2):
    """
    Add up two integer numbers.

    This function simply wraps the ``+`` operator, and does not
    do anything interesting, except for illustrating what
    the docstring of a very simple function looks like.

    Parameters
    ----------
    num1 : int
        First number to add.
    num2 : int
        Second number to add.

    Returns
    -------
    int
        The sum of ``num1`` and ``num2``.

    See Also
    --------
    subtract : Subtract one integer from another.

    Examples
    --------
    >>> add(2, 2)
    4
    >>> add(25, 0)
    25
    >>> add(10, -10)
    0
    """
    return num1 + num2

# Useful functionalities

#### Decorators

can be used to modify a function and to perform custom code before and after.

```py
  def my_decorator(func):
      def wrapper():
          print("Something is happening before the function is called.")
          func()
          print("Something is happening after the function is called.")
      return wrapper

  @my_decorator # @my_decorator is an easier way of saying "say_whee = my_decorator(say_whee)"
  def say_whee():
      print("Whee!")
```

> >>> say_whee() yields:
Something is happening before the function is called.
Whee!
Something is happening after the function is called.

### attribute self

 Attribute self is used in method to receive the intstance of the class inside a method. Self is passed automatically to methods in python, but not received automatically., e.g.:
  class food():

```py
    # init method or constructor
    def __init__(self, fruit, color):
    self.fruit = fruit
    self.color = color

    def show(self):
    print("fruit is", self.fruit)
    print("color is", self.color )

    apple = food("apple", "red")
    grapes = food("grapes", "green")

    apple.show()
    grapes.show()

self.cache
```

### magic methods

are defined internally in python, but can be overwritten. E.g.

```py
__init__() most common magic methodd
  class Person:
    def __init__(self, name, salary):
      self.name = name
      self.salary = salary
    #overriding magic method
    def __gt__(self, other):
      return self.salary > other.salary

  obj1 = Person('John', 4500)
  obj2 = Person('Natasha', 6000)
  print(obj1.name, 'earns more than', obj2.name, '-', obj1 > obj2)
  ```
