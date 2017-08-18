NORMAL_CLUSTER_ID = 17

with open("data_set/cluster_label.csv", "r") as c_file:
    labels = []
    t_label = []
    for line in c_file.readlines():
        cluster, label = line.rstrip().split(',')
        labels.append(int(cluster))
        t_label.append(label)

    correct = 0.0
    f_to_a = 0.0
    a_to_f = 0.0
    for i in range(len(labels)):
        if t_label[i] == 'normal.':
            if labels[i] == NORMAL_CLUSTER_ID:
                correct += 1.0
            else:
                a_to_f += 1.0
        else:
            if labels[i] != NORMAL_CLUSTER_ID:
                correct += 1.0
            else:
                f_to_a += 1.0

    # evaluate
    accuracy = correct / len(labels) * 100
    f_positive = a_to_f / len(labels) * 100
    f_negative = f_to_a/ len(labels) * 100
    print "accuracy = %3f %%" % accuracy
    print "false positive = %3f %%" % f_positive
    print "false negative = %3f %%" % f_negative