from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file
from google.genai import types

working_directory = "calculator"

def call_function(function_call_part, verbose=False):
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")
    
    result = ""

    if function_call_part.name == "get_files_info":
        args = function_call_part.args
        result = get_files_info(working_directory, **args)
    if function_call_part.name == "get_file_content":
        args = function_call_part.args
        result = get_file_content(working_directory, **args)
    if function_call_part.name == "write_file":
        args = function_call_part.args
        result = write_file(working_directory, **args)
    if function_call_part.name == "run_python_file":
        args = function_call_part.args
        result = run_python_file(working_directory, **args)
    if result == "":
        return types.Content(
            role="tool",
            parts=[types.Part.from_function_response(
                name=function_call_part.name,
                response={"error": f"Unknown function: {function_call_part.name}"}
            )],
        )
    return types.Content(
        role="tool",
        parts=[types.Part.from_function_response(
            name=function_call_part.name,
            response={"result": result}
        )],
    )
