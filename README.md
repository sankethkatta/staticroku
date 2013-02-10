# staticroku

Self-Hosted Heroku for Static Apps

## On Your Server:

Works with any Ubuntu Server.

```
git clone https://github.com/sankethkatta/staticroku.git
cd staticroku
./install_static.py
```

##Local Computer:

```
git clone <username>@<servername>:/opt/git/app.git my_site_name
cd my_site_name
echo "HELLO WORLD" > index.html

git add index.html
git commit -m 'index file'
git push
```
