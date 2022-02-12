# IDE
I use Visual Studio Code and WSL so getting that set up correctly was a must. Not only do I want Code and WSL to work together well, I want full python debugging and code sense as well as integration with pipenv. Easy!

1. Install VSCode and WSL. Ensure that the `Windows Subsystem for Linux` and `Windows Virtualization Platform` Windows features are installed.
2. In VSCode install the `Remote - WSL` plugin. This is what allows full WSL integration
3. Open WSL, open a directory with some Python code in it, and then run `code .`. The remote server for WSL will install, VSCode will launch, and connect to the Remote
4. Install the `Python` VSCode module. VSCode will give you 2 options: Install and Remote. Do both.

At this point you've got VSCode and WSL working together brilliantly with full debugging, remote execution - the whole 9. Now get it working with `pipenv`

1. Open a directory in WSL that contains a `pipenv` project or create one
2. Run `pipenv shell`
3. Run `code .`
4. Note the path that `pipenv` spits out with your virtualenv in it. Something like `. /home/adam/.local/share/virtualenvs/Labler-g2iOj0In/bin/activate`
5. In VSCode at the bottom near the left you'll see the Python version its using, something like `Python 3.10.2`. Click that and then from the Command Pallette that pops up select the version of Python that shows the same `pipenv` virtualenv ID, something like `Python 3.10.2 (Labler-g2iOj0In)`

At this point you've got WSL, VSCode, Python, and `pipenv` all working together like natural pals!

## Links
* [Microsoft's VSCode + WSL page](https://docs.microsoft.com/en-us/windows/wsl/tutorials/wsl-vscode)
* [Pipenv Virtual Environments](https://pipenv.pypa.io/en/latest/install/#:~:text=%E2%98%A4%20Pragmatic%20Installation%20of%20Pipenv%C2%B6%20If%20you%20have,user%20installsallow%20for%20installation%20into%20your%20home%20directory.)
* [How to solve Pylance missing imports](https://dev.to/climentea/how-to-solve-pylance-missing-imports-in-vscode-359b)