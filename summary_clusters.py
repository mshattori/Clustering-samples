
clusters = [{'id': i, 'count': 0, 'label_counts': {}} for i in range(23)]
with open('data_set/cluster_label.csv', 'r') as c_file:

    for l in c_file.readlines():
        cluster_id, label = l.rstrip().split(',')
        cluster = clusters[int(cluster_id)]
        cluster['count'] += 1
        label_counts = cluster['label_counts']
        label_counts.setdefault(label, 0)
        label_counts[label] += 1

clusters = sorted(clusters, key=lambda cat: cat['count'], reverse=True)

with open('data_set/cluster_summary.csv', 'w') as s_file:
    for cluster in clusters:
        label_counts = cluster['label_counts']
        label_counts_list = [{'label': label, 'count': label_counts[label]} for label in label_counts.keys()]
        label_counts_list = sorted(label_counts_list, key=lambda counts: counts['count'], reverse=True)

        values = [cluster['id'], cluster['count']]
        for counts in label_counts_list:
            values.append(counts['label'])
            values.append(counts['count'])

        values = map(str, values)
        line = ','.join(values)
        s_file.write(line + '\n')




