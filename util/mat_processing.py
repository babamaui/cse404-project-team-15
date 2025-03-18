# Imports
from scipy.io import loadmat

def process_matfile(file_name):
    # Load the data
    data = loadmat(file_name)['wiki'][0, 0]
    data_dict = {key: data[key] for key in data.dtype.names}

    # Convert data into filename-based dictionary
    filename_dict = {}

    for i in range(len(data_dict['full_path'][0])):
        filename = data_dict['full_path'][0][i][0]
        print(filename)
        filename_dict[filename] = {
            'age': data_dict['age'][0][i][0],
            'dob': data_dict['dob'][0][i][0],
            'photo_taken': data_dict['photo_taken'][0][i][0],
            'gender': data_dict['gender'][0][i][0],
            'name': data_dict['name'][0][i][0],
            'face_location': data_dict['face_location'][0][i][0],
            'face_score': data_dict['face_score'][0][i][0],
            'second_face_score': data_dict['second_face_score'][0][i][0]
        }

    return filename_dict