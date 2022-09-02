import csv
import csv_correction_defs as corr

def main():
    with open("phonebook_raw.csv") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    corr.len_correction(contacts_list)
    corrected_list = corr.combining_phonebook(contacts_list)

    with open("phonebook.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(corrected_list)

if __name__ == '__main__':
    main()