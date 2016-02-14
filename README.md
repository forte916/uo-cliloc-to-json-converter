# UO Cliloc to JSON Converter

PHP scritps to convert Ultima Online Cliloc files to JSON, back and forth, to create custom clilocs.

### Three simple steps to create your own translated clilocs:

1. Copy, from the UO folder, the clilocs you want to edit/compare and paste them inside `input` folder. (Ex: *Cliloc.enu* and *Cliloc.deu*)
2. Run `convert_cliloc_to_json.php` (using php through command line), to generate the `Cliloc.json` inside `json` folder, then change all cliloc entries you want on this json file and save it.
3. Run `convert_json_to_cliloc.php` (using php through command line), to generate the updated clilocs inside `output` folder. Then copy the cliloc (in this example, *Cliloc.deu*) back to the UO folder, ovewriting the old one. So next time you login the game, you'll see the translation updated.

### Requirements

- PHP 5.4+