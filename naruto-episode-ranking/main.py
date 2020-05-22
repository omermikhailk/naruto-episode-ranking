from collections import OrderedDict

main_arcs = OrderedDict()
filler_arcs = OrderedDict()
all_arcs = OrderedDict()

with open('arc-breakdown.txt', 'r') as f:
	for line in f:
		arc = line.strip()

		if arc.count('/') == 2:
			# It's a filler arc
			title, ep_range = arc.split('/')[1:]
			ep_range = list(map(int, ep_range.split('.')))
			ep_range = list(range(ep_range[0], ep_range[1] + 1))
			filler_arcs[title] = ep_range
		else:
			# It's a main arc
			title, ep_range = arc.split('/')
			if ep_range.count('+'):
				print(title, ep_range)
				ep_range = ep_range.split('+')
				for i in range(0, len(ep_range)):
					ep_range[i] = ep_range[i].strip()
					ep_range[i] = list(map(int, ep_range[i].split('.')))
					ep_range[i] = list(range(ep_range[i][0], ep_range[i][1] + 1))
				new_ep = []
				for sub in ep_range:
					for ep in sub:
						if ep not in new_ep: new_ep.append(ep)
				ep_range = new_ep[::]
				ep_range.sort()
				print(ep_range)
			else:
				ep_range = list(map(int, ep_range.split('.')))
				ep_range = list(range(ep_range[0], ep_range[1] + 1))
			main_arcs[title] = ep_range
		all_arcs[title] = ep_range
		print(arc)
