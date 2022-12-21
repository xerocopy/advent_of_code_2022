from collections import deque
import re


CD_RE = re.compile(r'\$ cd (.+)')
LS_RE = re.compile(r'\$ ls')
DIR_RE = re.compile(r'dir (.+)')
FILE_RE = re.compile(r'(\d+) (.+)')


class Directory:
	def __init__(self, name, parent):
		self.name = name
		self.parent = parent
		self.entries = {}
		self.total_size = 0

	def prettyprint(self, pad=''):
		print(f'{pad}- {self.name} (dir, total_size={self.total_size})')
		for name, entry in sorted(self.entries.items()):
			child_padding = pad + '  '
			if isinstance(entry, int):
				print(f'{child_padding}- {name} (file, size={entry})')
			else:
				entry.prettyprint(child_padding)

	@staticmethod
	def parse(lines):
		root_dir = Directory(name='/', parent=None)
		current_dir = root_dir

		lines = deque(lines)
		while lines:
			line = lines.popleft()

			cd_match = CD_RE.match(line)
			ls_match = LS_RE.match(line)
			if cd_match:
				target = cd_match.group(1)
				if target == '/':
					current_dir = root_dir
				elif target == '..':
					current_dir = current_dir.parent
				else:
					current_dir = current_dir.entries[target]

			elif ls_match:
				while lines:
					line = lines.popleft()
					dir_match = DIR_RE.match(line)
					file_match = FILE_RE.match(line)
					if dir_match:
						name = dir_match.group(1)
						new_dir = Directory(name=name, parent=current_dir)
						current_dir.entries[name] = new_dir
					elif file_match:
						size, name = int(file_match.group(1)), file_match.group(2)
						current_dir.entries[name] = size
					else:
						lines.appendleft(line)
						break

		return root_dir

	def assign_total_sizes(self):
		total = 0
		for name, entry in self.entries.items():
			if isinstance(entry, int):
				total += entry
			else:
				entry.assign_total_sizes()
				total += entry.total_size

		self.total_size = total


with open('input7.txt') as input_file:
	lines = input_file.readlines()

root_directory = Directory.parse(lines)
root_directory.assign_total_sizes()
root_directory.prettyprint()

total = 0

pending = deque()
pending.append(root_directory)

while pending:
	item = pending.popleft()
	if isinstance(item, Directory):
		pending.extend(item.entries.values())

		if item.total_size < 100000:
			total += item.total_size

print(total)