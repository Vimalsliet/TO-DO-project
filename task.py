# Complete code
import sys


def help():
	sa = """Usage :-
$ ./task add 2 hello world    # Add a new item with priority 2 and text "hello world" to the list
$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order
$ ./task del INDEX            # Delete the incomplete item with the given index
$ ./task done INDEX           # Mark the incomplete item with the given index as complete
$ ./task help                 # Show usage
$ ./task report               # Statistics """
	sys.stdout.buffer.write(sa.encode('utf8'))


def add(pr,s):
	# a,s=s
	try:
		f = open('task.txt', 'a')

		# l.append([pr,s])

		f.write(s)
		f.write("\n")
		f.close()
		s = '"'+s+'"'
		print(f"Added task: {s} with priority {pr}" )
	except:
		print("Cooll")


def ls():
	try:

		nec()
		l = 1 #len(d)
		k = len(d)

		for i in range(k):
			sys.stdout.buffer.write(f"{l}. {d[l]} [{l}]".encode('utf8'))
			sys.stdout.buffer.write("\n".encode('utf8'))
			l = l+1

	except Exception as e:
		raise e


def deL(no):
	try:
		no =int(no)
		nec()
		with open("task.txt", "r+") as f:
			lines = f.readlines()
			f.seek(0)
			for i in lines:
				if i.strip('\n') != d[no]:
					f.write(i)
			f.truncate()
		print(f"Deleted task #{no}")

	except Exception as e:
		print(f"Error: task with index #{no} does not exist. Nothing deleted.")


def done(no):
	try:

		nec()
		no = int(no)
		f = open('completed.txt', 'a')
		st = d[no]
		f.write(st)
		f.write("\n")
		f.close()
		print(f"Marked item as done.")
	
		with open("task.txt", "r+") as f:
			lines = f.readlines()
			f.seek(0)
			for i in lines:
				if i.strip('\n') != d[no]:
					f.write(i)
			f.truncate()
		
	except:
		print(f"Error: no incomplete item with index #{no} exists.")


def report():
	nec()
	try:
		# print(f'Pending : {len(d)}')
		sys.stdout.buffer.write(f'Pending : {len(d)}'.encode('utf8'))
		sys.stdout.buffer.write("\n".encode('utf8'))
		c=1
		for i in d.items():
			# print(f"{c}. {i[c]} [{c}] ")
			sys.stdout.buffer.write(f"{c}. {i[c]} [{c}]".encode('utf8'))
			sys.stdout.buffer.write("\n".encode('utf8'))
			c+=1

		sys.stdout.buffer.write("\n".encode('utf8'))
		c = 1
		nf = open('completed.txt', 'r')
		for line in nf:
			line = line.strip('\n')
			don.update({c: line})
			c = c+1

		sys.stdout.buffer.write(f'Completed : {len(don)}'.encode('utf8'))
		sys.stdout.buffer.write("\n".encode('utf8'))

		c = 1
		for line in don.items():
			# print(f'{line[0]}. {line[1]}')
			sys.stdout.buffer.write(f'{line[0]}. {line[1]}'.encode('utf8'))
			sys.stdout.buffer.write("\n".encode('utf8'))
			c = c+1
		
	except:
		print(
			f'Pending : {len(d)} \n Completed : {len(don)}')


def nec():
	try:
		
		f = open('task.txt', 'r')
		c = 1
		tmp=""
		for line in f:
			line = line.strip('\n')
			tmp=line
			# line='_'.join(tmp[1:])
			d.update({c: line})
			c = c+1
		# print(d,tmp[0])
		
	except:
		sys.stdout.buffer.write("There are no pending tasks!".encode('utf8'))


if __name__ == '__main__':
	try:
		d = {}
		priority_task={}
		l=[]
		don = {}

		args = sys.argv
		if(args[1] == 'del'):
			args[1] = 'deL'
		if(args[1] == 'add' and len(args[2:]) == 0):
		# if(args[1] == 'add'):
			sys.stdout.buffer.write(
				"Error: Missing tasks string. Nothing added!".encode('utf8'))

		elif(args[1] == 'done' and len(args[2:]) == 0):
			sys.stdout.buffer.write(
				"Error: Missing NUMBER for marking tasks as done.".encode('utf8'))

		elif(args[1] == 'deL' and len(args[2:]) == 0):
			sys.stdout.buffer.write(
				"Error: Missing NUMBER for deleting tasks..".encode('utf8'))
		else:
			globals()[args[1]](*args[2:])

	except Exception as e:

		s = """Usage :-
$ ./task add 2 hello world    # Add a new item with priority 2 and text "hello world" to the list
$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order
$ ./task del INDEX            # Delete the incomplete item with the given index
$ ./task done INDEX           # Mark the incomplete item with the given index as complete
$ ./task help                 # Show usage
$ ./task report               # Statistics """
		# print(args)
		sys.stdout.buffer.write(s.encode('utf8'))

