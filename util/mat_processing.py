# Imports
from scipy.io import loadmat
import datetime
import numpy as np

def matlab_datenum_to_date(matlab_dn):
    return datetime.date.fromordinal(int(matlab_dn) - 366)

def compute_wiki_age(photo_year, birth_datenum):
    photo_date = datetime.date(photo_year, 7, 1)
    birth_date = matlab_datenum_to_date(birth_datenum)
    delta = photo_date - birth_date
    return delta.days / 365.2425


def process_matfile(file_name):
    # Load the data
    data = loadmat(file_name)['wiki'][0, 0]
    data_dict = {key: data[key] for key in data.dtype.names}

    # Convert data into filename-based dictionary
    filename_dict = {}

    for i in range(len(data_dict['full_path'][0])):
        # Remove invalid faces
        if np.isinf(data_dict['face_score'][0][i]) or not np.isnan(data_dict['second_face_score'][0][i]):
            continue

        filename = data_dict['full_path'][0][i][0]
        filename_dict[filename] = {
            'dob': data_dict['dob'][0][i],
            'photo_taken': data_dict['photo_taken'][0][i],
            'gender': data_dict['gender'][0][i],
            'name': data_dict['name'][0][i],
            'face_location': data_dict['face_location'][0][i],
            'face_score': data_dict['face_score'][0][i],
            'second_face_score': data_dict['second_face_score'][0][i],
            'approx_age': compute_wiki_age(data_dict['photo_taken'][0][i], data_dict['dob'][0][i])
        }

    return filename_dict