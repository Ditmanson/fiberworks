# Creating the reporitory. 
- go to your git hub
- create a repository
- Do not add a readme file if you are initializing from a local directory
> the reason you don't do that is because it might cause merge conflicts you have to deal with
- Once the repository is created github will provide you directions to initilize it.
## From your local directory
- git init
> -b will allow you to initalize with a different branch name other than Main
- git commit -m "first commit"
- git branch -M main
> The -M or -m branch is just so you can rename it
- git remote add origin https://github.com/Ditmanson/test.git
> git remote other options include rename, remove, set-head, set-branches, set-url, get-url, prune
- git push -u origin main
> -u is shorthand for --set-ustream you can also add a -f or --force if github gives you a warning
## Version Control best practices
- Before editing any code, start by checking out the main branch and pull the latest changes
> git checkout main && git pull
- Next create a new branch to work on and check it out, branch name is constraind to a single word
> git checkout -b "edit-some-feture"
```shell
git remote add origin https://github.com/Ditmanson/test.git
```
- After you have finished editing all files, update requirements file if applicable, commit or restore images, push them ti your upstream repository.
```shell
pip3 freeze > requirements.txt
```
```shell
git add <file path>
git add .
git add -a
git add --all
```
```shell
git restore <file path>
git restore <file path>
git restore .
git restore -a
git restore --all
```
```shell
git commit -m "inital message"
git commit -a "amended message"
git commit --amend --no-edit 
```
```shell
git push -u origin main
```
Team CCB's github cheat sheet
[git-cheat-sheet-education.pdf](https://github.com/MayberryKory/CS3300CCB/files/12540901/git-cheat-sheet-education.pdf)
