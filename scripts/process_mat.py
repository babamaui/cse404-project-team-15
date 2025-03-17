from scipy.io import loadmat

def process_matfile(file_name):
    mat_data = loadmat(file_name)

    wiki_data = mat_data['wiki'][0, 0]      # Extract the one element in the (1,1) array

    # Convert to a dictionary for easier access
    wiki_dict = {key: wiki_data[key] for key in wiki_data.dtype.names}

    # Each value is a 2D array, the first index is what contains the data (only 1 index in the array)
    print(wiki_dict["full_path"][0].squeeze())

    # # Extract the data of 5 people
    # sample_size = 5
    # sample_data = {
    #     "dob": wiki_dict["dob"][:sample_size].squeeze(),
    #     "photo_taken": wiki_dict["photo_taken"][:sample_size].squeeze(),
    #     "full_path": wiki_dict["full_path"][:sample_size].squeeze(),
    #     "gender": wiki_dict["gender"][:sample_size].squeeze(),
    #     "face_score": wiki_dict["face_score"][:sample_size].squeeze(),
    # }

    # for i in range(sample_size):
    #     print(f"Person {i+1}:")
    #     print(f"  DOB: {sample_data['dob'][i]}")
    #     print(f"  Photo Taken: {sample_data['photo_taken'][i]}")
    #     print(f"  Full Path: {sample_data['full_path'][i]}")
    #     print(f"  Gender: {sample_data['gender'][i]}")
    #     print(f"  Face Score: {sample_data['face_score'][i]}")
    #     print("-" * 40)  # Separator for readability

def main():
    file_name = "./data/wiki.mat"
    process_matfile(file_name)

if __name__ == "__main__":
    main()