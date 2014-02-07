import sys, inspect, timeit

def fromat_timeit(best, number, repeat):
	string = '%d loops, ' % number
	usec = best * 1e6 / number
	
	if usec < 1000:
		string += 'best of %d: %10.2f microseconds per loop' % (repeat, usec)
	else:
		msec = usec / 1000
		if msec < 1000:
			string += 'best of %d: %10.2f milliseconds per loop' % (repeat, msec)
		else:
			sec = msec / 1000
			string += 'best of %d: %10.2f seconds per loop' % (repeat, sec)
	
	return string

def start(answer, t_number = 100, sort = True):
		t_repeat	= 3
		local_vars	= inspect.currentframe().f_back.f_locals
		probN		= sys.argv[0][1:-3]
		prob		= 'e' + probN
		
		if len(sys.argv) > 1:
			funcs = [ prob + '_' + i for i in sys.argv[1:] ]
		else:
			funcs = [ i for i in local_vars if i.startswith(prob) ]
		
		lcs = locals()
		for i in funcs:
			lcs[i] = local_vars[i]
		
		print 'Problem: {}'.format(probN)
		print 'Answer: {}'.format(answer)
		print 'http://projecteuler.net/problem=' + probN
		# print 'best {} of loops {}'.format(t_repeat, t_number)
		print '======================================'
		print
		
		top = []
		for i in funcs:
			if answer == local_vars[i]():
				timed = min(timeit.repeat('{}()'.format(i), repeat = t_repeat, number = t_number, setup="from __main__ import {}".format(i)))
				top.append((timed, i))
			else:
				top.append(('wrong', i))
				
		
		for t, f in (sorted(top) if sort else top):
			print '{}: {}'.format(f, fromat_timeit(t, t_number, t_repeat))
