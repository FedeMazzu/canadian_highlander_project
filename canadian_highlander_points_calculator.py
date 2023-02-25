import sys
def mysplit(s):
    head = s.lstrip('0123456789 ')
    return head

def calc_points(*args, **kwargs):
    points_dic = dict()
    text = Element('test-input').element.value
    with open("/points.txt", encoding='UTF-8') as file:
        for line in file:
            if line == '\n':
                continue
            card = line.lstrip().split(',')
            points_dic[card[0]] = card[1]

    output_points = []

    total_points = 0
    for line in text:
        card = mysplit(line)
        card = card.rstrip()
        if card in points_dic:
            total_points += int(points_dic[card])
            output_points.append(card)
    
    Element('test-output').element.innerText = "total points" + total_points + "/10"
        # for entry in output_points:
        #     print(entry,": ",points_dic[entry])
