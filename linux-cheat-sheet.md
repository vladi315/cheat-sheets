##Linux
search all files for a search term
`find . -print | grep -i searchterm123`

list all processes
`ps -a`

search for a process
`ps -ef | grep -i rosmaster`


check disk usage (alternatively use gnome-disks)
`df -h `

find string "foo" in large file input.txt	
`echo | grep -E "foo" input.txt`

Monitor memory usage
`htop`

Update all packages
```
sudo apt update
apt list --upgradable
sudo apt upgrade
```
check available packages for ubuntu under: 
https://packages.ubuntu.com/


Resolve package installation conflicts with
`sudo aptitude install packagename`

change access rights for group or user 
(r: 400, w: 200, x: 100), group (r: 40, w: 20, x: 10) and others (r: 4, w: 2, x: 1) --> 444 gives read rights to everyone --> 555 gives read and execute permissions to everyone
```
chmod u+w filename
chmod g+w filename
chmod g-wx filename
chmod o+w filename
chmod o-rwx foldername

chmod 444 header
```

change owner
`chown bin filename`

change group
`chgrp bin filename`

## text editing
copy content of one file to another file
`cat originalfile.txt >> newfile.txt`

display first 10 lines of a file
`head -10 input.txt`

display last 10 lines of a file
`tail -10 input.txt`

save first lines of a input file to another output file
`head -10 input.txt > output.txt`

consolidate two output streams to one
`( head -10 input.txt ; echo '=====' ) > output.txt`
	



##git 
clone specific branch from repo
```
git clone -b <branchname> <remote-repo-url>
```
or nitialize new git repo locally
```
git init
```

afterwards open github repo, and link by
```
git remote add origin git@github.com:vladi315/test.git
git branch -M main
git push -u origin main
```

**open Pull request:**
1. git fetch --all	-all fetches changes from all remote repositories
2. make new branch	git checkout -b new_branch
3. git status
4. add changes		git add test
5. commit		git commit -m "commit message"
6. git status
7. define where to push to with -u and push
`git push -u origin new_branch`
8. open PR

**Remove all untracked changes**
```
git clean -nfd		to see what will be deleted
git clean -fd		to execute deletion
```

**see branch tree in cli:** 
`git log --all --decorate --oneline --graph`

##Flask 
Run flask apps from cli
```
$ export FLASK_APP=hello.py
$ flask run
 * Running on http://127.0.0.1:5000/
```