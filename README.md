# lajconik-requester
The app is developed to testing [lajconik-app](https://github.com/lukasz-lesiuk/lajconik-app)
# Install
```bash
git clone https://github.com/miki164/lajconik-requester/edit/master/README.md
cd lajconik-requester
```

# Templates
In main directory make `templates` directory. And inside make another directory here you will make your template files! 
Now you can make your `template.json` and `data.txt`

For example:
1. Make dirs:
```bash
mkdir templates
mkdir /templates/example-template
```
2. Make `template.json`
```bash
touch /templates/example-template/template.json
```
Open that file with your favourite text editor ;) and insert your template.
```json
{
  "title": "str 255",
  "description": "str 255",
  "gameMaster": {
    "id": 2
  },
  "maxPlayerNumber": "int 8",
  "minAge": "int 66",
  "minSkill": "int 255",
  "availableTimeslots": [
    {
      "id": 2
    }
  ],
  "rpgSystem": "int 255",
  "streamable": true,
  "sidenotes": "int 255",
  "publiclyAvailable": true
}
```
Where there is "str 255", the application will insert a string from 0 to 255.

3. Make `data.txt`
```bash
touch /templates/example-template/data.txt
```
To that file simply insert URL that you want to test.
```
http://localhost:8080/api/v1/rpg-sessions
```
## TEMPLATE-POST
After you create your template you can run your first POST request! Simply type.
```bash
python main.py number_of_requests path_to_template TEMPLATE-POST
```

For example:
```bash
python main.py 2000 /templates/example-template/ TEMPLATE-POST
```
