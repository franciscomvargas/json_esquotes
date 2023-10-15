import sys, json, re, ast, select

def json_comquotes(raw_json, lone_char_searches=2, debug=False):
    try:
        out_json = json.loads(raw_json)
        return out_json
    except:
        try:
            out_json = ast.literal_eval(raw_json)
            return out_json
        except:
            # prepare raw json from some unwanted scenarios 
            raw_json = raw_json.replace(": '", ":'").replace(", '", ",'").replace("{ '", "{'").replace("[ '", "['").replace("' }", "'}").replace("' }", "'}").replace("''", "' '")
            raw_json = raw_json.replace(': "', ':"').replace(', "', ',"').replace('{ "', '{"').replace('[ "', '["').replace('" }', '"}').replace('" }', '"}').replace('""', '" "')

            # Regex patterns : dq|sq stands for double|single quote
            _re_dq_pattern = r'([\s\w])"([\s\w])'
            _re_dq_sub = r"\1\"\2"
            _re_sq_pattern = r"([\s\w])'([\s\w])"
            _re_sq_sub = r'\1\'\2'
            
            for _lone_char in range(lone_char_searches):
                # Substitute Double Quotes
                if _lone_char == 0:
                    _re_find = re.sub(_re_dq_pattern, _re_dq_sub, raw_json)
                #   > Solve schenarios like ""a"a"a"a"a" since 1st return "a\"a"a\"a"a", second time return a\"a\"a\"a\"a" (Other egs. ["Anything"a"Anything else", "Anything"a"Anythin"g" else"])
                else:
                    _re_find = re.sub(_re_dq_pattern, _re_dq_sub, _re_find)

                # Substitute Double Quotes   > Solve schenarios like 'a'a'a' since 1st return 'a\'a'a', secund time return 'a\'a\'\a' ...
                _re_find = re.sub(_re_sq_pattern, _re_sq_sub, _re_find)

                if debug:
                    sys.stderr.write(f"Iteration #{_lone_char+1}: {_re_find}\n")

                try:
                    out_json = json.loads(_re_find)
                    # Rem space from raw_json.replace("''", "' '").replace('""', '" "')
                    _re_find= _re_find.replace('\\" "', '\\""').replace('\\" \\"', '\\"\\"').replace("\\' '", "\\''").replace("\\' \\'", "\\'\\'")
                    return json.loads(_re_find)
                except Exception as ej:
                    try:
                        out_json = ast.literal_eval(_re_find)
                        # Rem space from raw_json.replace("''", "' '").replace('""', '" "')
                        _re_find= _re_find.replace('\\" "', '\\""').replace("\\' '", "\\''")
                        return ast.literal_eval(_re_find)
                    except Exception as ea:
                        if _lone_char != lone_char_searches-1:
                            continue
                        raise ValueError(f"Json Parse exception: {ej}\nAst Parse exception : {ea}\nUnparsed Result     : {_re_find}")

def get_jsons_cli(debug=False):
    _file_input=False
    _file_output=False

    #Stdout
    if not sys.stdout.isatty():
        # STDOUT DEFINED
        _file_output=True
        log = sys.stderr
    else:
        # STDOUT UNDEFINED
        log = sys.stdout

    if debug:
        log.write("*"*80)
    _exit = False

    #Stdin
    if not sys.stdin.isatty():
        # STDIN DEFINED
        _file_input = True
        req_jsons = [ si.strip() for si in sys.stdin.readlines()]
        if debug:
            log.write(f"Request Stdin: {req_jsons}\n")
    else:
        # STDIN UNDEFINED
        try:
            log.write("Insert your JSON: ('exit' to exit)\n")
            req_jsons = input("")
        except KeyboardInterrupt:
            _exit = True
            pass
        if _exit or req_jsons in ["exit", "Exit", "EXIT"]:
            exit(0)
        else:
            req_jsons = [req_jsons]

            
    return req_jsons, log, _file_input, _file_output


def main(debug=False):
    while True:
        # EXAMPLE
        # req_jsons = ['{"na"me": "Jack O"Sullivan", "id": "1"}', '{"name": "Jack: The "OG" O"Sullivan"", "id": "2"}', '{"name": "Jack: The "OG"", "surname": \'O\'Sullivan\', "id": "3"}', '{"test_str": {"1singlechar": "a""a""a", "2singlechars": "a"a"a"a"a"a"a"a"a"}, "id": "4"}', "{'name': 'Jack O'Sullivan, 'id': '5'}"]
        req_jsons, log, _file_input, _file_output = get_jsons_cli(debug=debug)
        
        _res_jsons = {}
        _res_code = 0
        for req_json in req_jsons:
            try:
                proc_json = json_comquotes(req_json, debug=debug)
                if debug:
                    log.write(f"Raw json      : {req_json}\n")
                    log.write(f"Processed json: {json.dumps(proc_json, indent=2)}\n")
                _res_jsons[req_json] = proc_json
            except Exception as e:
                if debug:
                    log.write("Something went wrong!\n")
                    log.write(f"Raw json      : {req_json}\n")
                    log.write(f"{e}\n\n")
                _res_jsons[req_json] = None
                _res_code += 1
        _res_jsons["exitcode"] = _res_code

        if not _file_output and debug:
            log.write("Results:\n")
        json.dump(_res_jsons, sys.stdout)
        
        if not _file_output:
            log.write("\n")

        if _file_input:
            exit(_res_code)

if __name__ == "__main__":
    # Check if DEBUG is requested in arguments
    DEBUG=False
    if "-d" in sys.argv:
        DEBUG=True
    main(debug=DEBUG)
