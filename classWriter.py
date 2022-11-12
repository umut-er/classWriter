# Format
# class Car
# String brand noGetter (no getter will be created)
# String model noSetter (no setter will be created)
# String carSerialNumber noSetter noGetter (no getter or setter will be created)
# int wheelCount (both getter and setter will be created)

# Setter
# public void setName(){
#    this.name = name
# }

# Getter
# public String getName(){
#    return this.name
# }

# Writes class signature given class name
def write_class(name: str) -> None:
    out.write("public class " + name + "{\n")

# Writes variables with signatures given a list of them
def write_variables(variable_list: list[str]) -> None:
    for variable in variable_list:
        out.write("\tprivate " + variable[0] + " " + variable[1] + ";\n")

# Writes setter for given type and name of a variable
def write_setter(type: str, name: str) -> None:
    out.write("\n\tpublic void set" + name[0].upper() + name[1:] + "(" + type + " " + name + "){\n")
    out.write("\t\tthis." + name + " = " + name + ";\n")
    out.write("\t}\n")

# Writes setter for given type and name of a variable
def write_getter(type: str, name: str) -> None:
    out.write("\n\tpublic " + type + " get" + name[0].upper() + name[1:] + "(){\n")
    out.write("\t\treturn this." + name + ";\n")
    out.write("\t}\n")

# Writes a constructor for a class given the name, a list of all variables and the indexes to be included in the constructor
def write_constructor(class_name: str, variable_list: list[str], indexes: list[str]) -> None:
    # Constructor signature
    out.write("\n\tpublic " + class_name + "(")

    if indexes == ["all"]:
        indexes_variable_list = variable_list
    elif indexes == ["none"]:
        out.write("){}\n")
        return
    else:
        indexes_variable_list = [variable_list[int(index) - 1] for index in indexes]

    first = True # To make the commas correct
    for variable in indexes_variable_list:
        if first:
            first = False
        else:
            out.write(", ")
        out.write(variable[0] + " " + variable[1])
    out.write("){\n")
    for variable in indexes_variable_list:
        out.write("\t\tthis." + variable[1] + " = " + variable[1] + ";\n")
    out.write("\t}\n")
    return

if __name__ == '__main__':
    with open("in.txt", "r") as inp:
        stored_input = list(map(str.split, inp.readlines()))
        class_name: str = stored_input[0][1]
        variable_list: list[str] = []
        constructor_list: list[str] = []
        if ["Constructors:"] in stored_input:
            for variable in stored_input[1:stored_input.index(["Constructors:"])]:
                variable_list.append(variable)            
            for constructor in stored_input[stored_input.index(["Constructors:"]) + 1:]:
                constructor_list.append(constructor)
        else:
            variable_list = stored_input[1:]
        
        with open(stored_input[0][1] + ".java", "w") as out:
            write_class(class_name)
            write_variables(variable_list)

            for tokenized_str in constructor_list:
                write_constructor(class_name, variable_list, tokenized_str)

            for tokenized_str in variable_list:
                if "noSetter" not in tokenized_str:
                    write_setter(tokenized_str[0], tokenized_str[1])
                if "noGetter" not in tokenized_str:
                    write_getter(tokenized_str[0], tokenized_str[1])


            out.write("}\n")
 