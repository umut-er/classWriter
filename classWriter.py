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

def write_class(name: str) -> None:
    out.write("public class " + name + "{\n")

def write_variables(variable_list: list[str]) -> None:
    for variable in variable_list:
        out.write("\tprivate " + variable[0] + " " + variable[1] + ";\n")

def write_setter(type: str, name: str) -> None:
    out.write("\n\tpublic void set" + name[0].upper() + name[1:] + "(" + type + " " + name + "){\n")
    out.write("\t\tthis." + name + " = " + name + ";\n")
    out.write("\t}\n")

def write_getter(type: str, name: str) -> None:
    out.write("\n\tpublic " + type + " get" + name[0].upper() + name[1:] + "(){\n")
    out.write("\t\treturn this." + name + ";\n")
    out.write("\t}\n")


if __name__ == '__main__':
    with open("in.txt", "r") as inp:
        stored_input = list(map(str.split, inp.readlines()))
        with open(stored_input[0][1] + ".java", "w") as out:
            write_class(stored_input[0][1])
            write_variables(stored_input[1:])

            for tokenized_str in stored_input[1:]:
                if "noSetter" not in tokenized_str:
                    write_setter(tokenized_str[0], tokenized_str[1])
                if "noGetter" not in tokenized_str:
                    write_getter(tokenized_str[0], tokenized_str[1])
            out.write("}\n")
 