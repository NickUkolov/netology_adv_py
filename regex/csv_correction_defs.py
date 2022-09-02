import re


def len_correction(csv_list):
    for row in csv_list:
        if len(row) > 7:
            for index in range(7, len(row)):
                if row[index] == '':
                    row.pop(index)
                else:
                    pass


def name_correction(csv_list):
    add_list = []
    for note in csv_list:
        if len(note.split()) == 3:
            for data in note.split():
                add_list.append(data)
        elif len(note.split()) == 2:
            for data in note.split():
                add_list.append(data)
        elif len(note.split()) == 1:
            add_list.append(note)
        elif len(note.split()) == 0:
            add_list.append('None')
    return add_list[:3]


def org_correction(csv_list):
    if 'ФНС' in csv_list or '@nalog.ru' in csv_list:
        return 'ФНС'
    elif 'Минфин' in csv_list or '@minfin.ru' in csv_list:
        return 'Минфин'
    else:
        return 'None'


def profession_correction(csv_list):
    for note in csv_list:
        if len(note.split()) > 3 and all(re.match(r"[а-яА-ЯёЁcC –]", i) for i in note):
            return note
        return 'None'


def phone_correction(csv_list):
    pattern = r'(\+7|8)[\s(]{0,3}(\d{3})[\s)-]{0,3}(\d{3})[-\s]{0,3}(\d{2})' \
              r'[-\s]{0,3}(\d{2})[\s(]{0,3}(доб\.)?[\s]?(\d+)?[\s)]?'
    substitution = r'+7(\2)\3-\4-\5 \6\7'
    result = re.sub(pattern, substitution, csv_list)
    if result:
        return result
    return 'None'


def mail_correction(csv_list):
    if '@' in csv_list:
        return csv_list
    return 'None'


def combine_repeats(original, repeat):
    for note in range(len(original)):
        if original[note] == 'None':
            original[note] == repeat[note]
    return original


def combining_phonebook(csv_list):
    corrected_dict = {}
    for index in csv_list[1:]:
        corrected_row = []
        name = name_correction(index[:3])
        corrected_row.append(name[0])
        corrected_row.append(name[1])
        corrected_row.append(name[2])
        corrected_row.append(org_correction(index[3:]))
        corrected_row.append(profession_correction(index[4:]))
        corrected_row.append(phone_correction(index[5]))
        corrected_row.append(mail_correction(index[6]))
        if name[0] not in corrected_dict:
            corrected_dict[name[0]] = corrected_row
            pass
        elif name[0] in corrected_dict:
            corrected_dict[name[0]] = combine_repeats(corrected_dict[name[0]], corrected_row)
    res = [['lastname', 'firstname', 'surname', 'organization', 'position', 'phone', 'email']]
    for k, v in corrected_dict.items():
        res.append(v)
    return res
