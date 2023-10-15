# json_esquotes

## Description
Handy Python tool for preprocessing JSON data that contains unescaped quotes within string values. It takes a JSON strings as input and transforms it by replacing the double and single quotes within the string values with alternative characters, allowing you to parse the JSON data without errors.


## Key Features:
* Replaces double quotes ` " ` within string values with escaped double quotes ` \" `.
* Replaces single quotes ` ' ` within string values with escaped single quotes ` \' `.
* Outputs the processed JSON as a dictionary.

## Instalation
### Open Terminal
* **Windows:** 
    * <kbd>⊞ Win</kbd> + <kbd>R</kbd>
    * Search: `cmd` 
* **Linux:** 
    * <kbd> Ctrl </kbd> + <kbd> Alt </kbd> + <kbd>T</kbd>

### Create project Folder
   * **Windows:**
     ```cmd
     mkdir %UserProfile%\json_esquotes
     ```
   * **Linux:** 
     ```cmd
     mkdir ~/json_esquotes
     ```

### Clone Repository
   * **Windows:** 
     ```cmd
     git clone https://github.com/franciscomvargas/json_esquotes.git %UserProfile%\json_esquotes
     ```
   * **Linux:** 
     ```cmd
     git clone https://github.com/franciscomvargas/json_esquotes.git ~/json_esquotes
     ```

## Usage:
[Open the terminal](#open-terminal)
   
### Terminal Interface
   * **Windows:** 
     ```cmd
     python3 %UserProfile%\json_esquotes\json_esquotes.py
     ```
   * **Linux:** 
     ```cmd
     python3 ~/json_esquotes/json_esquotes.py
     ```

### CLI Interface
   * **Windows:** 
     ```cmd
     python3 %UserProfile%\json_esquotes\json_esquotes.py <[stdin.txt] >[stdout.json]
     ```
   * **Linux:** 
     ```cmd
     python3 ~/json_esquotes/json_esquotes.py <[stdin.txt] >[stdout.json]
     ```

#### Example
* **STDIN Description:** Any text file with required JSON strings separated by new line, like:
  
  `eg.txt`
  ```
  {"na"me": "Jack O"Sullivan", "id": "1"}
  {"name": "Jack: The "OG" O"Sullivan"", "id": "2"}
  {"test_str": {"1singlechar": "a""a""a", "2singlechars": "a"a"a"a"a"a"a"a"a"}, "id": "3"}
  {'name': 'Jack O'Sullivan, 'id': '4'}
  ```


 * **Windows:** 
   ```cmd
   python3 %UserProfile%\json_esquotes\json_esquotes.py <%UserProfile%\json_esquotes\Assets\eg.txt >%UserProfile%\json_esquotes\eg_out.json && open %UserProfile%\json_esquotes\eg_out.json
   ```
 * **Linux:** 
   ```cmd
   python3 ~/json_esquotes/json_esquotes.py <~/json_esquotes/Assets/eg.txt >~/json_esquotes/eg_out.json && open ~/json_esquotes/eg_out.json
   ```


 * **Result:** 

    `eg_out.json`
    ```
    {"{\"na\"me\": \"Jack O\"Sullivan\", \"id\": \"1\"}": {"na\"me": "Jack O\"Sullivan", "id": "1"}, "{\"name\": \"Jack: The \"OG\" O\"Sullivan\"\", \"id\": \"2\"}": {"name": "Jack: The \"OG\" O\"Sullivan\"", "id": "2"}, "{\"test_str\": {\"1singlechar\": \"a\"\"a\"\"a\", \"2singlechars\": \"a\"a\"a\"a\"a\"a\"a\"a\"a\"}, \"id\": \"3\"}": {"test_str": {"1singlechar": "a\"\"a\"\"a", "2singlechars": "a\"a\"a\"a\"a\"a\"a\"a\"a"}, "id": "3"}, "{'name': 'Jack O'Sullivan, 'id': '4'}": null, "exitcode": 1}
    ```

     
### Optional Arguments
|arg|description|Linux example|
|---|---|---|
|-d|Set Debug ON (additional logs)|`~/json_esquotes/json_esquotes.py -d`|



## [Credits](https://www.reddit.com/r/Python/comments/177704z/json_quote_remover/)
[paraffin](https://www.reddit.com/r/Python/comments/177704z/comment/k4r9brf/?utm_source=share&utm_medium=web2x&context=3)

[Spleeeee](https://www.reddit.com/r/Python/comments/177704z/comment/k4tayrm/?utm_source=share&utm_medium=web2x&context=3)
