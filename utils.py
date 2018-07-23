
def load_gain_data(gain_data_file = 'gain_data.txt'):
    '''
    load the gain map:
        [('-30', 0x2072), ...]
    '''
    f = open(gain_data_file)
    result = [] 
    for line in f.readlines():
        if line.strip():
            key, value = line.split('\t')
            result.append([key, eval(value)])
    f.close()
    return result
