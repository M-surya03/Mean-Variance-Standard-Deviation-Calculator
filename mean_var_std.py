import numpy as np

def calculate(*args  ):
    if len(args) == 1 and isinstance(args[0], list):
        data = args[0]
    else:
        data = list(args)

    if len(data) != 9:
        raise ValueError("List must contain nine numbers.")

    array = np.array(data).reshape(3, 3)

    calculations = {
        'mean': [np.mean(array, axis=0).tolist(), np.mean(array, axis=1).tolist(), np.mean(array)],
        'variance': [np.var(array, axis=0).tolist(), np.var(array, axis=1).tolist(), np.var(array)],
        'standard deviation': [np.std(array, axis=0).tolist(), np.std(array, axis=1).tolist(), np.std(array)],
        'max': [np.max(array, axis=0).tolist(), np.max(array, axis=1).tolist(), np.max(array)],
        'min': [np.min(array, axis=0).tolist(), np.min(array, axis=1).tolist(), np.min(array)],
        'sum': [np.sum(array, axis=0).tolist(), np.sum(array, axis=1).tolist(), np.sum(array)]
    }
    for key, value in calculations.items():
        return f"{key}: {value}"


# Example usage:
output = calculate([0,1,2,3,4,5,6,7,8])
print(output)