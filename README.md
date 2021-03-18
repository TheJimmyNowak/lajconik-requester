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
  "title": "str 20 255",
  "description": "str 255",
  "gameMaster": {
    "id": 2
  },
  "maxPlayerNumber": "int 8",
  "minAge": "int 66",
  "minSkill": "int 5 255",
  "availableTimeslots": "dictlist id 3 int 1 2",
  "rpgSystem": "int 255",
  "streamable": true,
  "sidenotes": "int 255",
  "publiclyAvailable": true
}
```

Where there is `str 20 255`, the application will insert a string from 20 to 255. If you don't want to specify minimal
length you can simply type `str 255` so string will be from 0 to 255.
</br></br>
`dictlist id 3 int 1 2` will generate something like this this:

```json
"avaibleTimeSlots": [
    {"id": 2},
    {"id": 1},
    {"id": 1}
]
```

The `id 3 int 1 2` mean that script will generate list with 3 dicts where key name will be `id` and value will be
integer in range from 1 to 2

3. Make `data.txt`

```bash
touch /templates/example-template/data.txt
```

To that file simply insert URL that you want to test.

```
http://localhost:8080/api/v1/rpg-sessions
```

## POST

After you create your template you can run your first POST request! Simply type.

```bash
python main.py number_of_requests path_to_template POST
```

For example:

```bash
python main.py 2000 /templates/example-template/ POST
```

### Methods GET, DELETE, PUT, PATCH are also implemented! 
