Key Differences between Python 2 and Python 3
Here are some key differences between Python 2 and Python 3 that can make the new version of the language less confusing for new programmers to learn:

Print: In Python 2, “print” is treated as a statement rather than a function. There is no need to wrap the text you want to print in parentheses, although you can if you want. This can be confusing, as most other actions in Python use functions that require the arguments to be placed inside parentheses. It can also lead to unexpected outcomes if you put parentheses around a comma-separated list of items that you want to print. In contrast, Python 3 explicitly treats “print” as a function, which means you have to pass the items you need to print to the function in parentheses in the standard way, or you will get a syntax error. Some Python 2 programmers find this change annoying, but it can help to prevent mistakes.

Integer Division: Python 2 treats numbers that you type without any digits after the decimal point as integers, which can lead to some unexpected results during division. For example, if you type the expression 3 / 2 in Python 2 code, the result of the evaluation will be 1, not 1.5 as you might expect. This is because Python 2 assumes that you want the result of your division to be an integer, so it rounds the calculation down to the nearest whole number. In order to get the result 1.5, you would have to write 3.0 / 2.0 to tell Python that you want it to return a float, that is, to include digits after the decimal point in the result. Python 3 evaluates 3 / 2 as 1.5 by default, which is more intuitive for new programmers.

List Comprehension Loop Variables: In previous versions of Python, giving the variable that is iterated over in a list comprehension the same name as a global variable could lead to the value of the global variable being changed — something you usually don’t want. This irritating bug has been fixed in Python 3, so you can use a variable name you already used for the control variable in your list comprehension without worrying about it leaking out and messing with the values of the variables in the rest of your code.

Unicode Strings: Python 3 stores strings as Unicode by default, whereas Python 2 requires you to mark a string with a “u” if you want to store it as Unicode. Unicode strings are more versatile than ASCII strings, which are the Python 2 default, as they can store letters from foreign languages as well as emoji and the standard Roman letters and numerals. You can still label your Unicode strings with a “u” if you want to make sure your Python 3 code is compatible with Python 2.

Raising Exceptions: Python 3 requires different syntax for raising exceptions. If you want to output an error message to the user, you need to use the syntax:
raise IOError(“your error message”)

This syntax works in Python 2 as well. The following code works only in Python 2, not Python 3:

raise IOError, “your error message”

There are many other examples of slight differences in syntax between Python 2 and Python 3. A cheat sheet of key syntax differences is available from Python-Future to help you write code that is compatible with both versions of Python. In addition to syntax differences, there are other key differences, such as how the two versions of Python handle strings, as described above. Python 3.3 performs at approximately the same speed as Python 2.7, although some benchmarks measure the new language as being much faster.




Application Domains
Python is used across many application domains. Here's a sampling.

The Python Package Index hosts thousands of third party modules for Python.
Web and Internet Development
Serving the Web using Python

Serving the Web using Python

These short screencasts will walk you through the basics of several of the more popular web frameworks for Python.

Learn Django: Create a Wiki in 20 minutes
TurboGears 20 Minute Wiki
Plone Screencasts
Walkthru of a Twisted Webserver (16-min)
Python offers a wide range of choices for web development:

Writing basic CGI scripts.
Frameworks such as Django and TurboGears.
High-end solutions such as Zope.
Advanced content management systems such as Plone.
For custom web solutions and other internet-based applications:

Extensive support for HTML and XML.
E-mail processing.
Processing RSS feeds.
Support for many other Internet protocols.
Database Access
Custom and ODBC interfaces to MySQL, Oracle, MS SQL Server, PostgreSQL, SybODBC, and others are available for free download.
Standard Database API.
Object databases such as ZODB and Durus.
Desktop GUIs
The Tk GUI development library is included with most binary distributions for Python.
wxWidgets
GTK+
Qt via pyqt or pyside
Microsoft Foundation Classes through the win32 extensions
Delphi
Scientific and Numeric
Python is widely used in scientific and numeric computing:

Bioinformatics
Physics
Education
Python is a superb language for teaching programming, both at the introductory level and for more advanced courses.

Education Special Interest Group is a good place to start.
pyBiblio links to many different resources.
The Software Carpentry Course.
Network Programming
In addition to the web and internet support described above, Python also provides support for lower level network programming:

Easy-to-use socket interface.
Twisted Python, a framework for asynchronous network programming.
Software Development
Development Environments for Python

Development Environments for Python

Check out these screencasts for an introduction to the capabilities of some of the many IDEs available for Python. How many you ask? Take a look at the roster of IDEs for Python.

Using Wing IDE Professional
Introduction to Komodo IDE
PyDev (Eclipse) on a Mac
Introducing the PyDev IDE for Eclipse
Python is often used as a support language for software developers, for build control and management, testing, and in many other ways.

SCons for build control.
Buildbot and Apache Gump for automated continuous compilation and testing.
Roundup or Trac for bug tracking and project management.
Roster of Integrated Development Environments.
Game and 3D Graphics
Python is widely used in commercial and hobby game development:

A partial list of games is on the Python Games wiki page.
PyGame and PyKyra are two of the game frameworks available for Python.
List of 3D rendering libraries available for Python.
PyWeek is a semi-annual game programming contest.
