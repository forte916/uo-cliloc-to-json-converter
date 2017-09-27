# UO Cliloc to JSON Converter

Python scritps to convert Ultima Online Cliloc files to JSON, back and forth, to create custom clilocs.
This scripts are ported from [original PHP](https://github.com/felladrin/uo-cliloc-to-json-converter) to Python.

    Note: I don't even run origial PHP scripts, but these Python scripts takes very long time.

## Three simple steps to build your translated clilocs

1. Copy, from the UO folder, the clilocs you want to edit/compare and paste them inside `input` folder. (Ex: *Cliloc.enu* and *Cliloc.deu*)
2. Run `convert_cliloc_to_json.py` (using python through command line), to generate the *Cliloc.json* inside `json` folder, then change all cliloc entries you want on this json file and save it.
3. Run `convert_json_to_cliloc.py` (using python through command line), to generate the updated clilocs inside `output` folder. Then copy the cliloc (in this example, *Cliloc.deu*) back to the UO folder, ovewriting the old one. So next time you login the game, you'll see the translation updated.

## Usage Example

```
C:\converter> python convert_cliloc_to_json.py
Reading input\Cliloc.enu... OK!
Reading input\Cliloc.deu... OK!
Done! Cliloc.json has been saved in json folder. You can open and edit it using any text editor.
```

```
C:\converter> python convert_json_to_cliloc.py
Writing output\Cliloc.enu... OK!
Writing output\Cliloc.deu... OK!
Done! Now copy these clilocs to UO folder, overwriting the old ones.
```

## Example of a Cliloc.json file

```json
    {
        "500001": {
            "DEU": "Ich reagiere nicht.",
            "ENU": "I have no reaction to you.",
            "JPN": "何もないよ。"
        },
        "500002": {
            "DEU": "Ich gehe nach Hause.",
            "ENU": "I am going home.",
            "JPN": "家に帰ります。"
        }
    }
```

## Requirements

- python 2.6+
