var = {"scoop": "demo", "foo":"bar"}
def gen_vars(vars):
    result = {}
    for key,value in vars.items():
        tf_var_name = f"TF_VAR_{key}"
        result[tf_var_name] = value
    return result

print(gen_vars(var))